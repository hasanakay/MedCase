"""
Case Generator Agent
"""
from app.data.demo_cases import get_case_for_topic, get_step_content, get_case_title, DEMO_CASES


class CaseGeneratorAgent:
    def generate(
        self,
        topic: str,
        difficulty: str,
        weak_topics: list[str] | None = None,
        language: str = "en",
    ) -> dict:
        case = get_case_for_topic(topic, difficulty, weak_topics)
        title = get_case_title(case, language)
        scenario_update, question = get_step_content(case, 1, language)
        return {
            "case_id": case["case_id"],
            "case_title": title,
            "scenario_update": scenario_update,
            "opening_question": question,
            "steps": case["steps"],
            "learning_goals": case["learning_goals"],
        }

    def get_case_by_id(self, case_id: str) -> dict | None:
        return DEMO_CASES.get(case_id)
