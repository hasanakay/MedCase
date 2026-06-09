import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from app.data.demo_cases import DEMO_CASES, get_case_title

print(f"Total cases: {len(DEMO_CASES)}")
for cid, c in DEMO_CASES.items():
    title = get_case_title(c, "tr")
    topic = c["topic"]
    diff = c["difficulty"]
    steps = len(c["steps"])
    print(f"  {cid}: {title} ({topic} / {diff}) - {steps} steps")
