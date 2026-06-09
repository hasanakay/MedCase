"""
Student router — /student endpoints
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession
from sqlalchemy import func

from app.database import get_db
from app.models import Student, Session as SessionModel
from app.schemas import (
    StudentWeakTopicsResponse,
    WeakTopicItem,
    StudentDashboardResponse,
    SessionListItem,
)
from app.agents.progress_tracker import ProgressTrackerAgent

router = APIRouter(prefix="/student", tags=["student"])

progress_tracker = ProgressTrackerAgent()


@router.get("/{student_id}/weak-topics", response_model=StudentWeakTopicsResponse)
def get_weak_topics(student_id: str, db: DBSession = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    topics = progress_tracker.get_weak_topics(db, student_id)
    return StudentWeakTopicsResponse(
        student_id=student_id,
        weak_topics=[WeakTopicItem(**t) for t in topics],
    )


@router.get("/{student_id}/sessions", response_model=list[SessionListItem])
def get_sessions(student_id: str, db: DBSession = Depends(get_db)):
    """Return all sessions for a student, ordered newest first."""
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    sessions = (
        db.query(SessionModel)
        .filter(SessionModel.student_id == student_id)
        .order_by(SessionModel.created_at.desc())
        .all()
    )
    return [
        SessionListItem(
            session_id=s.id,
            topic=s.topic,
            difficulty=s.difficulty,
            case_title=s.case_title,
            status=s.status,
            total_score=s.total_score,
            current_step=s.current_step,
            language=s.language or "en",
            created_at=s.created_at,
            updated_at=s.updated_at,
        )
        for s in sessions
    ]


@router.get("/{student_id}/dashboard", response_model=StudentDashboardResponse)
def get_dashboard(student_id: str, db: DBSession = Depends(get_db)):
    """Full dashboard data: sessions list + stats + weak topics."""
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    sessions = (
        db.query(SessionModel)
        .filter(SessionModel.student_id == student_id)
        .order_by(SessionModel.created_at.desc())
        .all()
    )

    completed = [s for s in sessions if s.status == "completed"]
    avg_score = (
        round(sum(s.total_score for s in completed) / len(completed), 1)
        if completed
        else 0.0
    )

    topics = progress_tracker.get_weak_topics(db, student_id)

    return StudentDashboardResponse(
        student_id=student_id,
        student_name=student.name,
        average_score=avg_score,
        total_sessions=len(sessions),
        completed_sessions=len(completed),
        sessions=[
            SessionListItem(
                session_id=s.id,
                topic=s.topic,
                difficulty=s.difficulty,
                case_title=s.case_title,
                status=s.status,
                total_score=s.total_score,
                current_step=s.current_step,
                language=s.language or "en",
                created_at=s.created_at,
                updated_at=s.updated_at,
            )
            for s in sessions
        ],
        weak_topics=[WeakTopicItem(**t) for t in topics],
    )
