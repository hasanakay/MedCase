import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from app.mcp_server import lookup_guideline, verify_drug_dosage

print("=" * 60)
print("              MEDCASE AGENT — MCP SERVER UNIT TEST")
print("=" * 60)

# Test 1: Guidelines Lookup
print("\n[Test 1] Guidelines Lookup (svt):")
res1 = lookup_guideline("svt")
print(res1[:200] + "...\n")
assert "Pediatric SVT" in res1
print("➔ Test 1 PASSED")

# Test 2: Guidelines Lookup (Fallback match)
print("\n[Test 2] Guidelines Lookup (anaphylaxis partial):")
res2 = lookup_guideline("anaphylaxis shock")
print(res2[:200] + "...\n")
assert "Pediatric Anaphylaxis" in res2
print("➔ Test 2 PASSED")

# Test 3: Correct Pediatric Adenosine Dose
print("\n[Test 3] Correct Pediatric Adenosine Dose:")
res3 = verify_drug_dosage("adenosine", 0.1, "mg/kg", 10.0)
print(res3 + "\n")
assert "Status: Safe" in res3
print("➔ Test 3 PASSED")

# Test 4: Unsafe Pediatric Adenosine Overdose
print("\n[Test 4] Unsafe Pediatric Adenosine Overdose:")
res4 = verify_drug_dosage("adenosine", 2.0, "mg/kg", 10.0)
print(res4 + "\n")
assert "Status: UNSAFE" in res4
print("➔ Test 4 PASSED")

# Test 5: Correct Anaphylaxis Epinephrine Dose
print("\n[Test 5] Correct Anaphylaxis Epinephrine Dose:")
res5 = verify_drug_dosage("epinephrine", 0.1, "mg", 10.0)
print(res5 + "\n")
assert "Status: Safe" in res5
print("➔ Test 5 PASSED")

# Test 6: Neonatal Dextrose D10W Dose
print("\n[Test 6] Neonatal D10W Dose:")
res6 = verify_drug_dosage("dextrose", 2.0, "ml/kg", 3.0)
print(res6 + "\n")
assert "Status: Safe" in res6
print("➔ Test 6 PASSED")

print("\n" + "=" * 60)
print("              ALL MCP TOOL LOGIC TESTS PASSED!")
print("=" * 60)
