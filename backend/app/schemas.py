from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class SessionStartRequest(BaseModel):
    student_id: str
    topic: str
    difficulty: str  # Beginner | Intermediate | Advanced
    language: str = "en"  # en | tr
    weak_topic_focus: Optional[str] = None


class SessionStartResponse(BaseModel):
    session_id: str
    case_id: str
    case_title: str
    scenario_update: str
    question: str
    vitals: Optional[Dict[str, Any]] = None


class AnswerRequest(BaseModel):
    answer: str


class EvaluationResponse(BaseModel):
    score: int = Field(..., ge=0, le=100)
    is_safe: bool
    correct_points: List[str]
    missing_points: List[str]
    unsafe_points: List[str]
    weak_topics: List[str]
    feedback: str
    next_scenario_update: str
    next_question: str
    difficulty_change: str  # increase | same | decrease
    session_complete: bool = False
    vitals: Optional[Dict[str, Any]] = None



class SessionSummaryResponse(BaseModel):
    session_id: str
    total_score: int
    strong_topics: List[str]
    weak_topics: List[str]
    recommendations: List[str]
    recommended_next_case: str


class WeakTopicItem(BaseModel):
    topic: str
    frequency: int
    last_seen: str


class StudentWeakTopicsResponse(BaseModel):
    student_id: str
    weak_topics: List[WeakTopicItem]


class SessionListItem(BaseModel):
    session_id: str
    topic: str
    difficulty: str
    case_title: str
    status: str  # active | completed
    total_score: int
    current_step: int
    language: str
    created_at: str
    updated_at: str


class StudentDashboardResponse(BaseModel):
    student_id: str
    student_name: str
    average_score: float
    total_sessions: int
    completed_sessions: int
    sessions: List[SessionListItem]
    weak_topics: List[WeakTopicItem]


# ── OSCE Schemas ──────────────────────────────────────────────────────────────

class OSCESetSummary(BaseModel):
    set_id: str
    title: str
    description: str
    difficulty: str
    total_stations: int


class OSCEStartRequest(BaseModel):
    student_id: str
    osce_set_id: str
    language: str = "en"


class OSCEStartResponse(BaseModel):
    session_id: str
    osce_set_id: str
    osce_set_title: str
    total_stations: int
    first_station: "OSCEStationResponse"


class OSCEStationResponse(BaseModel):
    station_id: str
    station_number: int
    title: str
    time_limit_seconds: int
    station_type: str
    patient_scenario: str
    task: str


class OSCEAnswerRequest(BaseModel):
    answer: str
    time_spent_seconds: int = 0


class ChecklistResult(BaseModel):
    item: str
    category: str
    met: bool


class OSCEStationResult(BaseModel):
    station_number: int
    station_title: str
    score: int
    checklist_results: List[ChecklistResult]
    feedback: str


class OSCESummaryResponse(BaseModel):
    session_id: str
    osce_set_title: str
    total_score: int
    station_results: List[OSCEStationResult]
    strong_areas: List[str]
    weak_areas: List[str]
    recommendations: List[str]

