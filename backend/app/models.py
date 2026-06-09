from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False, default="Intermediate")
    created_at = Column(String, nullable=False)


class Session(Base):
    __tablename__ = "sessions"

    id = Column(String, primary_key=True, index=True)
    student_id = Column(String, ForeignKey("students.id"), nullable=False)
    topic = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    case_id = Column(String, nullable=False)
    case_title = Column(String, nullable=False)
    language = Column(String, nullable=False, default="en")
    session_type = Column(String, nullable=False, default="standard")  # standard | osce
    vitals = Column(Text, nullable=True, default="")  # JSON string of current patient vitals
    current_step = Column(Integer, default=0)
    status = Column(String, default="active")  # active | completed
    total_score = Column(Integer, default=0)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)



class Answer(Base):
    __tablename__ = "answers"

    id = Column(String, primary_key=True, index=True)
    session_id = Column(String, ForeignKey("sessions.id"), nullable=False)
    step_number = Column(Integer, nullable=False)
    question = Column(Text, nullable=False)
    student_answer = Column(Text, nullable=False)
    score = Column(Integer, default=0)
    is_safe = Column(Integer, default=1)  # 1 = True, 0 = False
    correct_points = Column(Text, default="[]")
    missing_points = Column(Text, default="[]")
    unsafe_points = Column(Text, default="[]")
    weak_topics = Column(Text, default="[]")
    feedback = Column(Text, default="")
    next_question = Column(Text, default="")
    created_at = Column(String, nullable=False)


class WeakTopic(Base):
    __tablename__ = "weak_topics"

    id = Column(String, primary_key=True, index=True)
    student_id = Column(String, ForeignKey("students.id"), nullable=False)
    topic = Column(String, nullable=False)
    frequency = Column(Integer, default=1)
    last_seen = Column(String, nullable=False)
