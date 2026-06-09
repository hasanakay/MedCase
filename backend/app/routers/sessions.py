"""
Session router — /session endpoints
"""
import json
from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession

from app.database import get_db
from app.models import Session as SessionModel, Answer, Student
from app.schemas import (
    SessionStartRequest, SessionStartResponse,
    AnswerRequest, EvaluationResponse, SessionSummaryResponse,
)
from app.agents.case_generator import CaseGeneratorAgent
from app.agents.examiner import ExaminerAgent
from app.agents.adaptive_tutor import AdaptiveTutorAgent
from app.agents.progress_tracker import ProgressTrackerAgent
from app.data.demo_cases import get_step_content

router = APIRouter(prefix="/session", tags=["session"])

case_generator = CaseGeneratorAgent()
examiner      = ExaminerAgent()
adaptive_tutor = AdaptiveTutorAgent()
progress_tracker = ProgressTrackerAgent()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


@router.post("/start", response_model=SessionStartResponse)
def start_session(body: SessionStartRequest, db: DBSession = Depends(get_db)):
    language = body.language if body.language in ("en", "tr") else "en"

    student = db.query(Student).filter(Student.id == body.student_id).first()
    if not student:
        student = Student(id=body.student_id, name=body.student_id,
                          level=body.difficulty, created_at=_now())
        db.add(student)
        db.commit()

    weak_topics = [wt["topic"] for wt in progress_tracker.get_weak_topics(db, body.student_id)]
    if body.weak_topic_focus:
        weak_topics.insert(0, body.weak_topic_focus)

    case = case_generator.generate(body.topic, body.difficulty, weak_topics, language)

    from app.agents.state_engine import PatientStateEngine
    state_engine = PatientStateEngine()
    baseline_vitals = state_engine.get_baseline_vitals(case["case_id"], language=language)

    session_id = str(uuid4())
    now = _now()
    session = SessionModel(
        id=session_id, student_id=body.student_id,
        topic=body.topic, difficulty=body.difficulty,
        case_id=case["case_id"], case_title=case["case_title"],
        language=language, current_step=1, status="active",
        total_score=0, vitals=json.dumps(baseline_vitals),
        created_at=now, updated_at=now,
    )
    db.add(session)
    db.commit()

    return SessionStartResponse(
        session_id=session_id,
        case_id=case["case_id"],
        case_title=case["case_title"],
        scenario_update=case["scenario_update"],
        question=case["opening_question"],
        vitals=baseline_vitals,
    )


@router.post("/{session_id}/answer", response_model=EvaluationResponse)
def submit_answer(session_id: str, body: AnswerRequest, db: DBSession = Depends(get_db)):
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if session.status == "completed":
        raise HTTPException(status_code=400, detail="Session already completed")

    lang = getattr(session, "language", "en") or "en"
    step_number = session.current_step

    case_data = case_generator.get_case_by_id(session.case_id)
    if not case_data:
        raise HTTPException(status_code=500, detail="Case data not found")

    _, question_text = get_step_content(case_data, step_number, lang)
    if not question_text:
        raise HTTPException(status_code=400, detail="No more steps in this case")

    from app.agents.state_engine import PatientStateEngine
    state_engine = PatientStateEngine()
    current_vitals = json.loads(session.vitals) if getattr(session, "vitals", "") else state_engine.get_baseline_vitals(session.case_id, language=lang)

    evaluation = examiner.evaluate(
        case_id=session.case_id,
        step_number=step_number,
        question=question_text,
        answer=body.answer,
        language=lang,
        current_vitals=current_vitals,
    )

    # Get next step content from static case data
    next_scenario, next_question = get_step_content(case_data, step_number + 1, lang)

    updated_vitals = evaluation.get("vitals", current_vitals)
    session.vitals = json.dumps(updated_vitals)

    now = _now()
    answer_record = Answer(
        id=str(uuid4()), session_id=session_id,
        step_number=step_number, question=question_text,
        student_answer=body.answer,
        score=evaluation["score"],
        is_safe=1 if evaluation["is_safe"] else 0,
        correct_points=json.dumps(evaluation["correct_points"]),
        missing_points=json.dumps(evaluation["missing_points"]),
        unsafe_points=json.dumps(evaluation["unsafe_points"]),
        weak_topics=json.dumps(evaluation["weak_topics"]),
        feedback=evaluation["feedback"],
        next_question=next_question,
        created_at=now,
    )
    db.add(answer_record)

    if evaluation["weak_topics"]:
        progress_tracker.save_weak_topics(db, session.student_id, evaluation["weak_topics"])

    session.current_step = step_number + 1
    session.updated_at = now

    answers = db.query(Answer).filter(Answer.session_id == session_id).all()
    if answers:
        session.total_score = round(sum(a.score for a in answers) / len(answers))

    session_complete = adaptive_tutor.should_end_session(session.case_id, session.current_step - 1)
    if session_complete:
        session.status = "completed"

    db.commit()

    custom_next_scenario = next_scenario

    return EvaluationResponse(
        score=evaluation["score"],
        is_safe=evaluation["is_safe"],
        correct_points=evaluation["correct_points"],
        missing_points=evaluation["missing_points"],
        unsafe_points=evaluation["unsafe_points"],
        weak_topics=evaluation["weak_topics"],
        feedback=evaluation["feedback"],
        next_scenario_update=custom_next_scenario if not session_complete else "",
        next_question=next_question if not session_complete else "",
        difficulty_change=evaluation["difficulty_change"],
        session_complete=session_complete,
        vitals=updated_vitals,
    )


@router.get("/{session_id}/summary", response_model=SessionSummaryResponse)
def get_summary(session_id: str, db: DBSession = Depends(get_db)):
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    summary = progress_tracker.generate_summary(db, session)
    return SessionSummaryResponse(**summary)


@router.get("/{session_id}/resume")
def resume_session(session_id: str, db: DBSession = Depends(get_db)):
    """Return the current state of an active session so the frontend can resume it."""
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    lang = getattr(session, "language", "en") or "en"

    case_data = case_generator.get_case_by_id(session.case_id)
    if not case_data:
        raise HTTPException(status_code=500, detail="Case data not found")

    step = session.current_step
    scenario, question = get_step_content(case_data, step, lang)

    from app.agents.state_engine import PatientStateEngine
    state_engine = PatientStateEngine()
    current_vitals = json.loads(session.vitals) if getattr(session, "vitals", "") else state_engine.get_baseline_vitals(session.case_id, language=lang)

    custom_scenario = scenario

    return {
        "session_id": session.id,
        "case_title": session.case_title,
        "status": session.status,
        "current_step": step,
        "language": lang,
        "scenario_update": custom_scenario,
        "question": question,
        "total_score": session.total_score,
        "vitals": current_vitals,
    }


