"""
MedCase Agent — FastAPI backend entry point
"""
from contextlib import asynccontextmanager

from dotenv import load_dotenv
load_dotenv()  # load .env before any other imports that read env vars

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.models import Student, Session, Answer, WeakTopic  # noqa: F401 — registers tables
from app.routers import sessions, students, osce
from app.seed import seed_demo_data

# Create all tables on startup
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup/shutdown lifecycle."""
    # ── Startup ──────────────────────────────────────────────────────────────
    # Safe migration: add language column if it doesn't exist yet
    try:
        from app.database import engine as _engine
        with _engine.connect() as conn:
            sa_text = __import__("sqlalchemy").text
            conn.execute(sa_text(
                "ALTER TABLE sessions ADD COLUMN language TEXT DEFAULT 'en'"
            ))
            conn.commit()
    except Exception:
        pass  # Column already exists

    # Safe migration: add session_type column
    try:
        from app.database import engine as _engine2
        with _engine2.connect() as conn:
            sa_text = __import__("sqlalchemy").text
            conn.execute(sa_text(
                "ALTER TABLE sessions ADD COLUMN session_type TEXT DEFAULT 'standard'"
            ))
            conn.commit()
    except Exception:
        pass  # Column already exists

    # Safe migration: add vitals column
    try:
        from app.database import engine as _engine3
        with _engine3.connect() as conn:
            sa_text = __import__("sqlalchemy").text
            conn.execute(sa_text(
                "ALTER TABLE sessions ADD COLUMN vitals TEXT DEFAULT ''"
            ))
            conn.commit()
    except Exception:
        pass  # Column already exists

    seed_demo_data()


    yield  # Application runs here

    # ── Shutdown ─────────────────────────────────────────────────────────────
    # Nothing to clean up for now


app = FastAPI(
    title="MedCase Agent API",
    description=(
        "Autonomous clinical reasoning tutor for medical students. "
        "This tool is for medical education and simulated clinical reasoning practice only. "
        "It does not provide real patient diagnosis or treatment."
    ),
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sessions.router)
app.include_router(students.router)
app.include_router(osce.router)


@app.get("/health")
def health():
    return {"status": "ok", "service": "MedCase Agent API"}


@app.get("/topics")
def list_topics():
    return {
        "topics": [
            "Pediatric Emergency",
            "Cardiology",
            "Neonatology",
            "Allergy and Anaphylaxis",
            "Trauma / Emergency Surgery",
            "Intoxication / Poisoning",
            "Respiratory Failure",
        ],
        "difficulties": ["Beginner", "Intermediate", "Advanced"],
    }
