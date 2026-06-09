"""
Seed script — creates demo student on first startup.
"""
from datetime import datetime, timezone

from app.database import SessionLocal
from app.models import Student


def seed_demo_data() -> None:
    db = SessionLocal()
    try:
        exists = db.query(Student).filter(Student.id == "demo_user").first()
        if not exists:
            db.add(
                Student(
                    id="demo_user",
                    name="Demo Student",
                    level="Intermediate",
                    created_at=datetime.now(timezone.utc).isoformat(),
                )
            )
            db.commit()
    finally:
        db.close()
