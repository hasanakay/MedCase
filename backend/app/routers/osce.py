"""
OSCE router — /osce endpoints
Handles OSCE exam sessions with timed stations.
"""
import json
from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession

from app.database import get_db
from app.models import Session as SessionModel, Answer, Student
from app.schemas import (
    OSCESetSummary, OSCEStartRequest, OSCEStartResponse,
    OSCEStationResponse, OSCEAnswerRequest,
    OSCEStationResult, OSCESummaryResponse,
    ChecklistResult,
)
from app.data.osce_stations import (
    list_osce_sets, get_osce_set, get_osce_station, get_station_content,
)
from app.agents.examiner import ExaminerAgent
from app.agents.progress_tracker import ProgressTrackerAgent

router = APIRouter(prefix="/osce", tags=["osce"])

examiner = ExaminerAgent()
progress_tracker = ProgressTrackerAgent()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


@router.get("/sets", response_model=list[OSCESetSummary])
def list_sets(language: str = "en"):
    """List all available OSCE sets."""
    return [OSCESetSummary(**s) for s in list_osce_sets(language)]


@router.post("/start", response_model=OSCEStartResponse)
def start_osce(body: OSCEStartRequest, db: DBSession = Depends(get_db)):
    """Start a new OSCE session."""
    language = body.language if body.language in ("en", "tr") else "en"

    osce_set = get_osce_set(body.osce_set_id)
    if not osce_set:
        raise HTTPException(status_code=404, detail="OSCE set not found")

    # Ensure student exists
    student = db.query(Student).filter(Student.id == body.student_id).first()
    if not student:
        student = Student(
            id=body.student_id, name=body.student_id,
            level="Intermediate", created_at=_now()
        )
        db.add(student)
        db.commit()

    set_title = osce_set.get(f"title_{language}") or osce_set.get("title_en", "")

    session_id = str(uuid4())
    now = _now()
    session = SessionModel(
        id=session_id,
        student_id=body.student_id,
        topic=set_title,
        difficulty=osce_set["difficulty"],
        case_id=body.osce_set_id,
        case_title=set_title,
        language=language,
        session_type="osce",
        current_step=1,
        status="active",
        total_score=0,
        created_at=now,
        updated_at=now,
    )
    db.add(session)
    db.commit()

    # Get first station
    first_station_data = get_osce_station(body.osce_set_id, 1)
    if not first_station_data:
        raise HTTPException(status_code=500, detail="No stations found in OSCE set")

    first_station = get_station_content(first_station_data, language)

    return OSCEStartResponse(
        session_id=session_id,
        osce_set_id=body.osce_set_id,
        osce_set_title=set_title,
        total_stations=len(osce_set["stations"]),
        first_station=OSCEStationResponse(**first_station),
    )


@router.get("/{session_id}/station/{station_number}", response_model=OSCEStationResponse)
def get_station(session_id: str, station_number: int, db: DBSession = Depends(get_db)):
    """Get a specific station's data for an active OSCE session."""
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if session.session_type != "osce":
        raise HTTPException(status_code=400, detail="Not an OSCE session")

    lang = getattr(session, "language", "en") or "en"
    station_data = get_osce_station(session.case_id, station_number)
    if not station_data:
        raise HTTPException(status_code=404, detail="Station not found")

    content = get_station_content(station_data, lang)
    return OSCEStationResponse(**content)


@router.post("/{session_id}/station/{station_number}/answer", response_model=OSCEStationResult)
def submit_station_answer(
    session_id: str,
    station_number: int,
    body: OSCEAnswerRequest,
    db: DBSession = Depends(get_db),
):
    """Submit an answer for an OSCE station and get evaluation."""
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if session.session_type != "osce":
        raise HTTPException(status_code=400, detail="Not an OSCE session")
    if session.status == "completed":
        raise HTTPException(status_code=400, detail="Session already completed")

    lang = getattr(session, "language", "en") or "en"
    station_data = get_osce_station(session.case_id, station_number)
    if not station_data:
        raise HTTPException(status_code=404, detail="Station not found")

    # Evaluate using checklist-based approach
    checklist = station_data.get("checklist", [])
    key_points = station_data.get("key_points", [])
    station_title = station_data.get(f"title_{lang}") or station_data.get("title_en", "")
    task_text = station_data.get(f"task_{lang}") or station_data.get("task_en", "")

    # Use examiner agent for evaluation — pass key_points
    evaluation = examiner.evaluate(
        case_id=session.case_id,
        step_number=station_number,
        question=task_text,
        answer=body.answer,
        language=lang,
    )

    # Checklist evaluation — rule-based matching
    answer_lower = body.answer.lower()
    checklist_results = []
    met_count = 0

    for item in checklist:
        # Simple keyword matching for checklist items
        item_words = item["item"].lower().split()
        # Check if at least 2 significant words from checklist item appear in answer
        significant_words = [w for w in item_words if len(w) > 3]
        matches = sum(1 for w in significant_words if w in answer_lower)
        met = matches >= max(len(significant_words) // 2, 1) if significant_words else False

        checklist_results.append(ChecklistResult(
            item=item["item"],
            category=item["category"],
            met=met,
        ))
        if met:
            met_count += 1

    # Score: blend examiner score with checklist score
    checklist_score = round((met_count / max(len(checklist), 1)) * 100)
    blended_score = round(evaluation["score"] * 0.4 + checklist_score * 0.6)

    # Save answer record
    now = _now()
    answer_record = Answer(
        id=str(uuid4()),
        session_id=session_id,
        step_number=station_number,
        question=task_text,
        student_answer=body.answer,
        score=blended_score,
        is_safe=1 if evaluation.get("is_safe", True) else 0,
        correct_points=json.dumps(evaluation.get("correct_points", [])),
        missing_points=json.dumps(evaluation.get("missing_points", [])),
        unsafe_points=json.dumps(evaluation.get("unsafe_points", [])),
        weak_topics=json.dumps(evaluation.get("weak_topics", [])),
        feedback=evaluation.get("feedback", ""),
        next_question="",
        created_at=now,
    )
    db.add(answer_record)

    # Save weak topics
    weak_topics = evaluation.get("weak_topics", [])
    if weak_topics:
        progress_tracker.save_weak_topics(db, session.student_id, weak_topics)

    # Update session
    osce_set = get_osce_set(session.case_id)
    total_stations = len(osce_set["stations"]) if osce_set else 4

    answers = db.query(Answer).filter(Answer.session_id == session_id).all()
    if answers:
        session.total_score = round(sum(a.score for a in answers) / len(answers))
    session.current_step = station_number + 1
    session.updated_at = now

    if station_number >= total_stations:
        session.status = "completed"

    db.commit()

    return OSCEStationResult(
        station_number=station_number,
        station_title=station_title,
        score=blended_score,
        checklist_results=checklist_results,
        feedback=evaluation.get("feedback", ""),
    )


@router.get("/{session_id}/summary", response_model=OSCESummaryResponse)
def get_osce_summary(session_id: str, db: DBSession = Depends(get_db)):
    """Get the complete OSCE session summary."""
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if session.session_type != "osce":
        raise HTTPException(status_code=400, detail="Not an OSCE session")

    lang = getattr(session, "language", "en") or "en"

    answers = (
        db.query(Answer)
        .filter(Answer.session_id == session_id)
        .order_by(Answer.step_number)
        .all()
    )

    osce_set = get_osce_set(session.case_id)
    set_title = ""
    if osce_set:
        set_title = osce_set.get(f"title_{lang}") or osce_set.get("title_en", "")

    station_results = []
    strong_areas = []
    weak_areas = []

    for a in answers:
        station_data = get_osce_station(session.case_id, a.step_number)
        station_title = ""
        if station_data:
            station_title = station_data.get(f"title_{lang}") or station_data.get("title_en", "")

        # Reconstruct checklist results from answer data
        checklist = station_data.get("checklist", []) if station_data else []
        answer_lower = a.student_answer.lower()
        checklist_results = []
        for item in checklist:
            item_words = item["item"].lower().split()
            significant_words = [w for w in item_words if len(w) > 3]
            matches = sum(1 for w in significant_words if w in answer_lower)
            met = matches >= max(len(significant_words) // 2, 1) if significant_words else False
            checklist_results.append(ChecklistResult(
                item=item["item"], category=item["category"], met=met
            ))

        station_results.append(OSCEStationResult(
            station_number=a.step_number,
            station_title=station_title,
            score=a.score,
            checklist_results=checklist_results,
            feedback=a.feedback,
        ))

        if a.score >= 70:
            strong_areas.append(station_title)
        else:
            weak_areas.append(station_title)

    total_score = round(sum(a.score for a in answers) / max(len(answers), 1)) if answers else 0

    recommendations = []
    for wa in weak_areas[:3]:
        recommendations.append(f"Review and practice: {wa}")
    if total_score >= 80:
        recommendations.append("Excellent OSCE performance! Consider attempting advanced cases.")
    elif total_score < 60:
        recommendations.append("Focus on systematic approaches (ABCDE, structured history taking).")

    return OSCESummaryResponse(
        session_id=session_id,
        osce_set_title=set_title,
        total_score=total_score,
        station_results=station_results,
        strong_areas=strong_areas,
        weak_areas=weak_areas,
        recommendations=recommendations,
    )
