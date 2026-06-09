"""
Examiner Agent
Evaluates a student answer. Returns score, feedback, weak topics.
next_question and next_scenario_update are handled by the session router.
"""
import os
import json
import re

from app.data.demo_cases import DEMO_CASES

LANGUAGE_NAMES = {"en": "English", "tr": "Turkish"}


def _gemini_available() -> bool:
    try:
        import google.genai  # noqa: F401
        return bool(os.getenv("GEMINI_API_KEY"))
    except ImportError:
        return False


EXAMINER_PROMPT = """You are a clinical reasoning examiner for medical students.

IMPORTANT: You must respond ENTIRELY in {language_name}. Every field — feedback, correct_points, missing_points, unsafe_points, weak_topics — must be written in {language_name}.

Evaluate the student answer in the context of this simulated educational case.

Available Tools:
- Use `lookup_guideline` to search clinical procedures for this case topic (e.g. svt, anaphylaxis, neonatal_seizure, etc.) to check expected key points.
- Use `verify_drug_dosage` to verify the safety and accuracy of any drug name, dosage, or fluid resuscitation proposed by the student. Always pass the patient's weight if the medication requires weight-based calculations.
- IMPORTANT: If the student specifies a drug dosage (e.g., "10 mg/kg Adenosine" or "0.01 mg/kg Epinephrine"), you MUST run `verify_drug_dosage` to confirm it is safe before finalizing your feedback. Do not rely on your own estimated dosing thresholds.

Patient Info:
- Weight: {weight_kg} kg

Current Patient Vitals (BEFORE student intervention):
- Heart Rate: {current_hr} bpm
- Blood Pressure: {current_bp} mmHg
- SpO2: {current_spo2}%
- Respiratory Rate: {current_rr}/min
- Temperature: {current_temp} C
- Status: {current_status_description}

Rules:
- This is educational simulation only, not real patient care.
- Evaluate clinical reasoning quality.
- Check for safe clinical logic.
- Return structured JSON only.

Feedback formatting rules:
- The "feedback" field MUST use Markdown formatting.
- Use **bold** to highlight key medical terms, drug names, and critical concepts.
- Use bullet lists (- item) to structure multiple points.
- Use `inline code` for dosages, measurements, and medical values (e.g., `0.01 mg/kg`, `SpO2 > 94%`).
- If applicable, add a brief reference note at the end using a blockquote (> Reference: ...).
- Keep feedback educational, concise, and well-structured.

Case title: {case_title}

Current clinical question:
{question}

Expected key learning points:
{key_points}

Student answer:
{answer}

Return JSON exactly matching this schema (all strings in {language_name}, except vitals numbers):
{{
  "score": <integer 0-100>,
  "is_safe": <true|false>,
  "correct_points": [<string>, ...],
  "missing_points": [<string>, ...],
  "unsafe_points": [<string>, ...],
  "weak_topics": [<string>, ...],
  "feedback": "<Markdown-formatted educational feedback in {language_name}>",
  "difficulty_change": "<increase|same|decrease>",
  "vitals": {{
    "heart_rate": <integer, updated heart rate in bpm>,
    "blood_pressure": "<string, updated blood pressure like '120/80' in mmHg>",
    "spo2": <integer, updated SpO2 percentage>,
    "respiratory_rate": <integer, updated respiratory rate/min>,
    "temperature": <float, updated body temperature in C>,
    "status_description": "<string, brief update on patient symptoms, conscious status, and skin in {language_name}>"
  }}
}}
"""


def _get_fallback_weight(case_id: str, case_title: str) -> float:
    title_lower = case_title.lower()
    id_lower = case_id.lower()
    if "neonatal" in title_lower or "neonatal" in id_lower or "yenidoğan" in title_lower:
        return 3.0
    if "peds" in id_lower or "pediat" in title_lower or "child" in title_lower or "çocuk" in title_lower:
        return 25.0
    return 70.0


def _validate_evaluation(result: dict) -> bool:
    required_keys = [
        "score", "is_safe", "correct_points", "missing_points",
        "unsafe_points", "weak_topics", "feedback", "difficulty_change", "vitals"
    ]
    if not all(k in result for k in required_keys):
        return False
    
    # Check types
    if not isinstance(result["score"], (int, float)):
        return False
    if not isinstance(result["is_safe"], bool):
        return False
    if not isinstance(result["correct_points"], list):
        return False
    if not isinstance(result["missing_points"], list):
        return False
    if not isinstance(result["unsafe_points"], list):
        return False
    if not isinstance(result["weak_topics"], list):
        return False
    if not isinstance(result["feedback"], str):
        return False
    if result["difficulty_change"] not in ("increase", "same", "decrease"):
        return False
    
    # Check vitals keys
    vitals = result["vitals"]
    if not isinstance(vitals, dict):
        return False
    required_vitals = ["heart_rate", "blood_pressure", "spo2", "respiratory_rate", "temperature", "status_description"]
    if not all(vk in vitals for vk in required_vitals):
        return False
    
    return True


def _evaluate_with_gemini(
    case_title: str,
    question: str,
    key_points: list[str],
    answer: str,
    language: str,
    weight_kg: float,
    current_vitals: dict,
) -> dict:
    from google import genai
    from google.genai import types
    from app.mcp_server import lookup_guideline, verify_drug_dosage

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    lang_name = LANGUAGE_NAMES.get(language, "English")

    prompt = EXAMINER_PROMPT.format(
        language_name=lang_name,
        case_title=case_title,
        question=question,
        key_points="\n".join(f"- {p}" for p in key_points),
        answer=answer,
        weight_kg=weight_kg,
        current_hr=current_vitals.get("heart_rate", 80),
        current_bp=current_vitals.get("blood_pressure", "120/80"),
        current_spo2=current_vitals.get("spo2", 99),
        current_rr=current_vitals.get("respiratory_rate", 16),
        current_temp=current_vitals.get("temperature", 37.0),
        current_status_description=current_vitals.get("status_description", ""),
    )

    config = types.GenerateContentConfig(
        tools=[lookup_guideline, verify_drug_dosage],
        response_mime_type="application/json"
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=config,
    )
    raw = response.text.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    parsed = json.loads(raw)
    if not _validate_evaluation(parsed):
        raise ValueError("Invalid schema returned by Gemini model")
    return parsed


def _rule_based_evaluate(
    key_points: list[str],
    answer: str,
    language: str,
    current_vitals: dict,
) -> dict:
    answer_lower = answer.lower()
    correct: list[str] = []
    missing: list[str] = []

    keyword_map = {
        "ABC assessment": ["abc", "airway", "breathing", "circulation", "hava yolu", "solunum", "dolaşım", "dolasim"],
        "Vital signs": ["vital", "blood pressure", "bp", "heart rate", "spo2", "tansiyon", "nabız", "nabiz"],
        "Cardiac monitoring": ["monitor", "ecg", "ekg", "monitörizasyon", "monitorizasyon"],
        "IV access": ["iv", "intravenous", "damar yolu", "serum yolu"],
        "12-lead ECG": ["ecg", "ekg", "12 derivasyon", "elektrokardiyogram"],
        "Adenosine": ["adenosine", "adenozin"],
        "Synchronized cardioversion": ["cardioversion", "kardiyoversiyon", "senkronize"],
        "Intramuscular epinephrine 0.01 mg/kg (max 0.5 mg) \u2014 FIRST LINE": ["epinephrine", "adrenaline", "epinefrin", "adrenalin"],
        "Immediate bedside blood glucose check": ["glucose", "gl\u00fckoz", "glukoz", "kan \u015fekeri", "kan sekeri", "dextrose"],
        "Oxygen supplementation if SpO2 low": ["oxygen", "oksijen", "o2"],
    }

    for kp in key_points:
        keywords = keyword_map.get(kp, [kp.lower().split()[0]])
        if any(kw in answer_lower for kw in keywords):
            correct.append(kp)
        else:
            missing.append(kp)

    score = round((len(correct) / max(len(key_points), 1)) * 100)
    difficulty_change = "increase" if score >= 80 else ("same" if score >= 50 else "decrease")
    weak_topics = missing[:2]

    # Vitals deterioration/improvement mock in rule-based
    vitals = current_vitals.copy()
    if score >= 80:
        # improvement
        if vitals.get("heart_rate", 80) > 100:
            vitals["heart_rate"] = max(80, vitals["heart_rate"] - 30)
        vitals["status_description"] = (
            "Hasta durumu stabilize oluyor." if language == "tr"
            else "Patient condition is stabilizing."
        )
    elif score < 50:
        # deterioration
        if vitals.get("heart_rate", 80) > 100:
            vitals["heart_rate"] = min(220, vitals["heart_rate"] + 15)
        vitals["status_description"] = (
            "Standart müdahalelerin yapılmaması nedeniyle hasta durumu kötüleşiyor." if language == "tr"
            else "Patient is deteriorating due to lack of standard interventions."
        )

    if language == "tr":
        feedback_parts = []
        if correct:
            feedback_parts.append("**Doğru belirlediğiniz noktalar:**")
            for c in correct:
                feedback_parts.append(f"- **{c}** ✓")
        if missing:
            feedback_parts.append("\n**Eksik kalan noktalar:**")
            for m in missing:
                feedback_parts.append(f"- **{m}**")
        feedback_parts.append("\n" + ("Devam edin, iyi çalışıyorsunuz! 👏" if score >= 80 else "Eksik noktaları gözden geçirin ve tekrar deneyin."))
    else:
        feedback_parts = []
        if correct:
            feedback_parts.append("**Correctly identified:**")
            for c in correct:
                feedback_parts.append(f"- **{c}** ✓")
        if missing:
            feedback_parts.append("\n**Missing points:**")
            for m in missing:
                feedback_parts.append(f"- **{m}**")
        feedback_parts.append("\n" + ("Excellent work! Keep it up! 👏" if score >= 80 else "Review the missing points above and try to incorporate them in your clinical reasoning."))

    return {
        "score": score,
        "is_safe": True,
        "correct_points": correct,
        "missing_points": missing,
        "unsafe_points": [],
        "weak_topics": weak_topics,
        "feedback": "\n".join(feedback_parts),
        "difficulty_change": difficulty_change,
        "vitals": vitals,
    }


class ExaminerAgent:
    def evaluate(
        self,
        case_id: str,
        step_number: int,
        question: str,
        answer: str,
        language: str = "en",
        current_vitals: dict = None,
    ) -> dict:
        case = DEMO_CASES.get(case_id, {})
        steps = case.get("steps", [])
        current_step = next((s for s in steps if s["step"] == step_number), None)
        key_points: list[str] = current_step["key_points"] if current_step else []
        case_title = case.get(f"case_title_{language}") or case.get("case_title", "")
        
        weight_kg = case.get("weight_kg", _get_fallback_weight(case_id, case_title))
        
        # Load baseline vitals if not provided
        if not current_vitals:
            from app.agents.state_engine import PatientStateEngine
            engine = PatientStateEngine()
            current_vitals = engine.get_baseline_vitals(case_id, language=language)

        if _gemini_available():
            try:
                return _evaluate_with_gemini(
                    case_title=case_title,
                    question=question,
                    key_points=key_points,
                    answer=answer,
                    language=language,
                    weight_kg=weight_kg,
                    current_vitals=current_vitals,
                )
            except Exception:
                pass

        return _rule_based_evaluate(key_points, answer, language, current_vitals)


