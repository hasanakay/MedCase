"""
Progress Tracker Agent
Saves and retrieves weak topics; generates session summaries.
"""
import json
from datetime import date
from uuid import uuid4

from sqlalchemy.orm import Session as DBSession

from app.models import Answer, WeakTopic, Session as SessionModel


class ProgressTrackerAgent:
    # ── Weak topic tracking ───────────────────────────────────────────────────

    def save_weak_topics(
        self,
        db: DBSession,
        student_id: str,
        weak_topics: list[str],
    ) -> None:
        today = date.today().isoformat()
        for topic in weak_topics:
            existing = (
                db.query(WeakTopic)
                .filter(WeakTopic.student_id == student_id, WeakTopic.topic == topic)
                .first()
            )
            if existing:
                existing.frequency += 1
                existing.last_seen = today
            else:
                db.add(
                    WeakTopic(
                        id=str(uuid4()),
                        student_id=student_id,
                        topic=topic,
                        frequency=1,
                        last_seen=today,
                    )
                )
        db.commit()

    def get_weak_topics(self, db: DBSession, student_id: str) -> list[dict]:
        rows = (
            db.query(WeakTopic)
            .filter(WeakTopic.student_id == student_id)
            .order_by(WeakTopic.frequency.desc())
            .all()
        )
        return [
            {"topic": r.topic, "frequency": r.frequency, "last_seen": r.last_seen}
            for r in rows
        ]

    # ── Session summary ───────────────────────────────────────────────────────

    def generate_summary(self, db: DBSession, session: SessionModel) -> dict:
        answers = (
            db.query(Answer)
            .filter(Answer.session_id == session.id)
            .order_by(Answer.step_number)
            .all()
        )

        if not answers:
            return {
                "session_id": session.id,
                "total_score": 0,
                "strong_topics": [],
                "weak_topics": [],
                "recommendations": ["Complete at least one question to get a summary."],
                "recommended_next_case": "Any case",
            }

        total_score = round(sum(a.score for a in answers) / len(answers))

        # Collect all correct and weak points across answers
        all_correct: list[str] = []
        all_weak: list[str] = []
        for a in answers:
            all_correct.extend(json.loads(a.correct_points or "[]"))
            all_weak.extend(json.loads(a.weak_topics or "[]"))

        # Deduplicate preserving order
        seen: set[str] = set()
        strong_topics: list[str] = []
        for t in all_correct:
            if t not in seen:
                seen.add(t)
                strong_topics.append(t)

        seen = set()
        weak_topics: list[str] = []
        for t in all_weak:
            if t not in seen:
                seen.add(t)
                weak_topics.append(t)

        recommendations: list[str] = []
        for wt in weak_topics[:3]:
            recommendations.append(f"Review: {wt}")

        if total_score < 60:
            recommendations.append("Consider repeating a Beginner-level case to build confidence.")
        elif total_score >= 85:
            recommendations.append("You are ready to attempt an Advanced-level case.")

        recommended_next = _recommend_next_case(session.case_id, weak_topics)

        return {
            "session_id": session.id,
            "total_score": total_score,
            "strong_topics": strong_topics[:5],
            "weak_topics": weak_topics[:5],
            "recommendations": recommendations,
            "recommended_next_case": recommended_next,
        }


def _recommend_next_case(current_case_id: str, weak_topics: list[str]) -> str:
    next_case_map = {
        "peds_svt_001": "Unstable Tachycardia Simulation",
        "neonatal_seizure_001": "Neonatal Hypoglycemia Case",
        "anaphylaxis_001": "Anaphylaxis with Shock",
    }
    return next_case_map.get(current_case_id, "Pediatric Emergency — Intermediate Level")
