import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import time
import json

from dotenv import load_dotenv
load_dotenv()

# Ensure backend folder is in path
sys.path.insert(0, ".")
from app.agents.examiner import ExaminerAgent

# Colors for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

TEST_CASES = [
    {
        "name": "Pediatric SVT - Correct Initial Approach",
        "case_id": "peds_svt_001",
        "step": 1,
        "question": "What is your first approach? What do you assess and what initial steps do you take?",
        "answer": "First, I will assess the patient's airway, breathing, and circulation (ABCs). I will hook up continuous cardiac monitoring, check vital signs (heart rate, blood pressure, oxygen saturation), establish intravenous (IV) access, and obtain a 12-lead ECG.",
        "expected_safe": True,
        "min_score": 80
    },
    {
        "name": "Pediatric SVT - Incomplete Answer",
        "case_id": "peds_svt_001",
        "step": 1,
        "question": "What is your first approach? What do you assess and what initial steps do you take?",
        "answer": "I will check the heart rate and give medicine.",
        "max_score": 50
    },
    {
        "name": "Pediatric SVT - Unsafe Medication Dosage (Critical Safety Check)",
        "case_id": "peds_svt_001",
        "step": 3,
        "question": "Vagal maneuvers failed. What medication do you use, at what dose, and how exactly do you administer it?",
        "answer": "I will give a massive dose of 10 mg/kg Adenosine quickly through a peripheral IV.",
        "expected_safe": False,
        "max_score": 40
    },
    {
        "name": "Neonatal Seizure - Correct Management",
        "case_id": "neonatal_seizure_001",
        "step": 2,
        "question": "Blood glucose is critically low (28 mg/dL). What is your immediate treatment? Which other urgent laboratory tests do you order?",
        "answer": "Since the glucose is critically low and the baby is actively seizing, I will immediately administer an IV bolus of D10W (Dextrose 10%) at 2 mL/kg. I will then start a continuous dextrose infusion. I will order urgent serum electrolytes (sodium, potassium, calcium, magnesium) and blood cultures.",
        "expected_safe": True,
        "min_score": 60
    }
]

def run_stress_test():
    print("=" * 60)
    print("      MEDCASE AGENT — AI STRESS TESTING & EVALUATION HARNESS")
    print("=" * 60)
    
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        print(f"{GREEN}✓ Gemini API Key found. Testing live Gemini model execution.{RESET}")
    else:
        print(f"{YELLOW}⚠ Gemini API Key NOT found. Falling back to local rule-based validator.{RESET}")
    
    agent = ExaminerAgent()
    success_count = 0
    
    for i, tc in enumerate(TEST_CASES, 1):
        print(f"\n[Test {i}/{len(TEST_CASES)}] {tc['name']}")
        print(f"  Question: {tc['question']}")
        print(f"  Student Answer: '{tc['answer']}'")
        
        start_time = time.time()
        try:
            result = agent.evaluate(
                case_id=tc["case_id"],
                step_number=tc["step"],
                question=tc["question"],
                answer=tc["answer"],
                language="en"
            )
            elapsed = time.time() - start_time
            
            # Print evaluation results
            print(f"  Response Time: {elapsed:.2f} seconds")
            print(f"  Score: {result.get('score')} / 100")
            print(f"  Is Safe: {result.get('is_safe')}")
            print(f"  Correct Points Identified: {result.get('correct_points')}")
            print(f"  Missing Points Identified: {result.get('missing_points')}")
            print(f"  Unsafe Points Identified: {result.get('unsafe_points')}")
            print(f"  Weak Topics Detected: {result.get('weak_topics')}")
            print(f"  Vitals Output: {result.get('vitals')}")
            
            # Validation assertions
            assertions = []
            
            # 1. Structure validation
            required_keys = ["score", "is_safe", "correct_points", "missing_points", "unsafe_points", "weak_topics", "feedback", "difficulty_change", "vitals"]
            struct_ok = all(k in result for k in required_keys)
            
            # Check vitals sub-structure
            if struct_ok and isinstance(result.get("vitals"), dict):
                vitals_keys = ["heart_rate", "blood_pressure", "spo2", "respiratory_rate", "temperature", "status_description"]
                vitals_ok = all(k in result["vitals"] for k in vitals_keys)
                struct_ok = struct_ok and vitals_ok
                
            assertions.append(("JSON Schema Structure Match (including Vitals)", struct_ok))
            
            # 2. Safety check validation
            safety_ok = True
            if "expected_safe" in tc:
                safety_ok = result.get("is_safe") == tc["expected_safe"]
            assertions.append(("Safety Flag matches expected", safety_ok))

            
            # 3. Score constraint validation
            score = result.get("score", 0)
            score_ok = True
            if "min_score" in tc and score < tc["min_score"]:
                score_ok = False
            if "max_score" in tc and score > tc["max_score"]:
                score_ok = False
            assertions.append(("Score is within bounds", score_ok))
            
            # Check results
            all_passed = True
            for desc, status in assertions:
                status_str = f"{GREEN}PASS{RESET}" if status else f"{RED}FAIL{RESET}"
                print(f"    - {desc}: {status_str}")
                if not status:
                    all_passed = False
            
            if all_passed:
                print(f"  {GREEN}➔ Test case PASSED{RESET}")
                success_count += 1
            else:
                print(f"  {RED}➔ Test case FAILED{RESET}")
                
        except Exception as e:
            print(f"  {RED}➔ Exception occurred: {e}{RESET}")
            
    print("\n" + "=" * 60)
    print(f"  STRESS TEST COMPLETED: {success_count}/{len(TEST_CASES)} PASSED")
    print("=" * 60)
    
    if success_count == len(TEST_CASES):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    run_stress_test()
