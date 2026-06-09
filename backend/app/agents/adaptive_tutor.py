"""
Adaptive Tutor Agent
Decides session flow: continue, change difficulty, or end session.
"""
from app.data.demo_cases import DEMO_CASES

MAX_STEPS = 5  # end session after this many answered steps


class AdaptiveTutorAgent:
    def should_end_session(self, case_id: str, current_step: int) -> bool:
        """Return True when the session has reached the final step."""
        case = DEMO_CASES.get(case_id, {})
        total_steps = len(case.get("steps", []))
        return current_step >= min(MAX_STEPS, total_steps)

    def next_difficulty(self, current_difficulty: str, difficulty_change: str) -> str:
        levels = ["Beginner", "Intermediate", "Advanced"]
        idx = levels.index(current_difficulty) if current_difficulty in levels else 1
        if difficulty_change == "increase":
            idx = min(idx + 1, len(levels) - 1)
        elif difficulty_change == "decrease":
            idx = max(idx - 1, 0)
        return levels[idx]
