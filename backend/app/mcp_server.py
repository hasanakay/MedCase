"""
MedCase Agent — Model Context Protocol (MCP) Server
Exposes clinical reference guidelines and drug dosage verification tools for Gemini.
"""
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP Server
mcp = FastMCP("MedCase Clinical Reference")

# Clinical Guidelines Database
GUIDELINES = {
    "svt": {
        "title": "Pediatric SVT (Supraventricular Tachycardia) Guidelines",
        "content": (
            "- Initial Approach: Assess airway, breathing, circulation (ABCs). Start continuous ECG and pulse oximetry monitoring. Establish IV or IO access. Obtain 12-lead ECG.\n"
            "- Hemodynamically Stable Management:\n"
            "  1. Attempt vagal maneuvers first (e.g., ice to face for infants/young children, Valsalva maneuver for older cooperative children).\n"
            "  2. If vagal maneuvers fail, administer Adenosine: First dose 0.1 mg/kg IV/IO rapid bolus (maximum first dose 6 mg) followed immediately by a rapid flush of normal saline (at least 5-10 mL). If unsuccessful, a second dose of 0.2 mg/kg IV/IO rapid bolus (maximum second dose 12 mg) can be administered.\n"
            "- Hemodynamically Unstable Management (Altered mental status, signs of shock, hypotension):\n"
            "  1. Perform synchronized cardioversion immediately. Initial energy level: 0.5 to 1 J/kg. If unsuccessful, increase the energy level to 2 J/kg.\n"
            "  2. Administer sedation prior to synchronized cardioversion if the patient is conscious and time allows, but do not delay treatment."
        )
    },
    "neonatal_seizure": {
        "title": "Neonatal Seizure Management Guidelines",
        "content": (
            "- Initial Approach: Stabilize airway, breathing, and circulation. Maintain normal temperature. Secure IV access.\n"
            "- Bedside Glucose Check: Draw immediate bedside blood glucose. Normal newborn glucose target: >40-45 mg/dL. If glucose is <40 mg/dL, treat immediately with D10W (Dextrose 10%) 2 mL/kg IV bolus, followed by continuous IV infusion of D10W at a glucose infusion rate (GIR) of 6-8 mg/kg/min.\n"
            "- Check Electrolytes: Draw serum sodium, potassium, calcium, magnesium. If hypocalcemia is confirmed (calcium <8 mg/dL or ionized calcium <1 mmol/L), administer IV Calcium Gluconate 10% 1-2 mL/kg (100-200 mg/kg) slowly over 5-10 minutes under continuous cardiac monitoring (watch for bradycardia or arrhythmias).\n"
            "- Anticonvulsant Therapy: If seizures continue after correcting glucose/calcium, administer Phenobarbital 20 mg/kg IV slowly as first line. If seizures persist, additional boluses of Phenobarbital (5-10 mg/kg) can be given up to a total of 40 mg/kg.\n"
            "- Sepsis/Meningitis Evaluation: Perform lumbar puncture (LP) if stable. Start empiric antibiotics immediately: Ampicillin (100 mg/kg) + Gentamicin (4-5 mg/kg) or Cefotaxime. If herpes simplex virus (HSV) meningitis is suspected, add Acyclovir 20 mg/kg IV every 8 hours."
        )
    },
    "anaphylaxis": {
        "title": "Pediatric Anaphylaxis Guidelines",
        "content": (
            "- First-Line Therapy: Epinephrine (adrenaline) IM in the mid-outer thigh (anterolateral aspect) immediately. NEVER delay epinephrine for secondary treatments.\n"
            "- Epinephrine Dosage: 0.01 mg/kg of 1:1000 (1 mg/mL) solution IM. Maximum single dose: 0.3 mg for children, 0.5 mg for adults. Can repeat every 5 to 15 minutes if symptoms persist.\n"
            "- Positioning: Place patient in supine position with legs elevated (unless in severe respiratory distress, where they should be allowed to sit up. AVOID sudden standing or sitting up).\n"
            "- Supportive Care: High-flow oxygen via non-rebreather mask. IV normal saline bolus (10-20 mL/kg) for hypotension or signs of shock.\n"
            "- Second-Line Therapies (Give ONLY after epinephrine): Antihistamines (H1 blocker diphenhydramine 1-2 mg/kg IV/IM; H2 blocker ranitidine/famotidine), Corticosteroids (methylprednisolone 1-2 mg/kg IV to prevent biphasic reactions).\n"
            "- Observation Period: Observe all patients in a medical facility for at least 4 to 6 hours due to risk of a biphasic reaction (recurrent symptoms without re-exposure).\n"
            "- Discharge Planning: Prescribe epinephrine auto-injector (e.g. EpiPen), provide a written Anaphylaxis Action Plan, and educate on allergen avoidance."
        )
    },
    "ami": {
        "title": "Acute Myocardial Infarction (AMI/STEMI) Guidelines",
        "content": (
            "- Immediate Assessment: 12-lead ECG within 10 minutes of arrival. Apply continuous cardiac monitor, secure IV access, obtain vital signs.\n"
            "- Immediate Medications: Aspirin 162-325 mg chewed immediately (non-enteric coated). If chest pain persists, administer sublingual nitroglycerin (0.4 mg) every 5 minutes (up to 3 doses) unless contraindicated.\n"
            "- Contraindications for Nitroglycerin: Systolic BP <90 mmHg, bradycardia (<50 bpm), tachycardia, or suspected Right Ventricular (RV) infarction.\n"
            "- Right Ventricular (RV) Infarction: Suspected in inferior STEMI (ST elevation in II, III, aVF) with ST elevation in right-sided lead V4R. In RV infarction, AVOID preload-reducing drugs (nitrates, morphine, diuretics). Treat hypotension with IV fluid boluses (normal saline).\n"
            "- Reperfusion Strategy: Primary PCI is preferred if it can be performed within 90 minutes of first medical contact (door-to-balloon time <90 mins) or within 120 minutes if transferred. If PCI is not available within 120 minutes, administer fibrinolytic therapy within 30 minutes of arrival (door-to-needle time <30 mins)."
        )
    },
    "heart_failure": {
        "title": "Acute Decompensated Heart Failure (ADHF) and Pulmonary Edema Guidelines",
        "content": (
            "- Initial Management:\n"
            "  1. Position the patient upright (reduces venous return/preload).\n"
            "  2. Administer oxygen therapy. Start Non-Invasive Ventilation (CPAP or BiPAP) if the patient has respiratory distress or SpO2 <90%.\n"
            "  3. Establish IV access, start cardiac monitoring, and obtain a 12-lead ECG.\n"
            "- Diuretic Therapy: Loop diuretics are first-line. Administer IV Furosemide (Lasix) at a dose equal to or greater than the patient's daily oral dose (e.g. 20-80 mg IV bolus).\n"
            "- Vasodilator Therapy: If systolic BP is elevated (>110 mmHg), administer IV Nitroglycerin infusion to reduce preload and afterload. Titrate to improve dyspnea while keeping systolic BP >90 mmHg.\n"
            "- Monitoring: Place an indwelling urinary catheter to monitor strict hourly urine output. Track daily weights. Restrict sodium and fluid intake."
        )
    },
    "trauma": {
        "title": "ATLS Primary Survey and Pediatric Polytrauma Guidelines",
        "content": (
            "- ATLS Primary Survey:\n"
            "  1. A - Airway with C-spine protection: Check patency, suction secretions, apply jaw thrust, maintain rigid collar.\n"
            "  2. B - Breathing: Check respiratory rate, chest expansion, auscultate breath sounds, rule out tension pneumothorax or hemothorax.\n"
            "  3. C - Circulation with hemorrhage control: Check pulses, capillary refill, skin temperature, blood pressure. Establish two large-bore IVs. Apply direct pressure to bleeding.\n"
            "  4. D - Disability: Assess Glasgow Coma Scale (GCS) score, check pupil size and response.\n"
            "  5. E - Exposure / Environment: Fully undress patient, inspect all areas, keep warm with blankets and warmed IV fluids (avoid hypothermia).\n"
            "- Hemorrhagic Shock Resuscitation: In children, give an initial crystalloid bolus of 20 mL/kg (Normal Saline or Lactated Ringer's). Reassess vitals. If patient remains unstable, repeat crystalloid bolus or begin blood transfusion (10-15 mL/kg packed RBCs).\n"
            "- Splinting: Femur fractures should be splinted urgently (e.g., traction splint) to control pain and reduce internal bleeding.\n"
            "- Post-Splenectomy Care: If patient undergoes splenectomy, they are at high risk for overwhelming post-splenectomy infection (OPSI). Essential measures include: pneumococcal, meningococcal, and Haemophilus influenzae type b (Hib) vaccinations; lifelong daily antibiotic prophylaxis (oral penicillin/amoxicillin); and immediate medical care for any fever."
        )
    },
    "paracetamol_poisoning": {
        "title": "Paracetamol (Acetaminophen) Poisoning and Overdose Guidelines",
        "content": (
            "- Toxic Dose: Single ingestion of >150 mg/kg in children, or >7.5 g total in adults is considered potentially hepatotoxic.\n"
            "- Gastrointestinal Decontamination: Administer Activated Charcoal (1 g/kg) if the patient presents within 1 to 2 hours of ingestion and has a patent airway.\n"
            "- Assessment: Draw a serum paracetamol level at a minimum of 4 hours post-ingestion. Plot the level on the Rumack-Matthew Nomogram to determine if treatment is indicated. Do NOT wait for symptoms to start treatment, as paracetamol toxicity is initially asymptomatic.\n"
            "- Antidote (N-Acetylcysteine / NAC): If paracetamol level is on or above the treatment line of the nomogram, start IV NAC immediately.\n"
            "- IV NAC 3-Bag Regimen:\n"
            "  1. Bag 1: 150 mg/kg in 200 mL D5W over 60 minutes.\n"
            "  2. Bag 2: 50 mg/kg in 500 mL D5W over 4 hours.\n"
            "  3. Bag 3: 100 mg/kg in 1000 mL D5W over 16 hours.\n"
            "- Discontinuing NAC: Do NOT stop NAC at the end of the protocol if the paracetamol level is still detectable, AST/ALT are elevated or rising, or INR is elevated. Continue NAC infusion at 6.25 mg/kg/hour until paracetamol is undetectable, LFTs are improving, and INR is normal."
        )
    }
}


@mcp.tool()
def lookup_guideline(topic: str) -> str:
    """
    Retrieve clinical emergency procedures and guidelines for a specific topic.
    Allowed topics: 'svt', 'neonatal_seizure', 'anaphylaxis', 'ami', 'heart_failure', 'trauma', 'paracetamol_poisoning'.
    """
    normalized = topic.lower().strip()
    if normalized in GUIDELINES:
        return f"=== {GUIDELINES[normalized]['title']} ===\n{GUIDELINES[normalized]['content']}"
    
    # Try finding by substring match
    for k, v in GUIDELINES.items():
        if k in normalized or normalized in k:
            return f"=== {v['title']} ===\n{v['content']}"
            
    return (
        f"Guideline for '{topic}' not found. Available guidelines topics are: "
        f"{', '.join(GUIDELINES.keys())}"
    )


@mcp.tool()
def verify_drug_dosage(
    drug_name: str,
    dose_amount: float,
    unit: str,
    weight_kg: float = 0.0
) -> str:
    """
    Verify the safety and standard dosage of emergency medications.
    Inputs:
      drug_name: The name of the medication (e.g., 'adenosine', 'epinephrine', 'dextrose', 'calcium gluconate', 'phenobarbital', 'furosemide', 'aspirin', 'paracetamol').
      dose_amount: The absolute amount or per-kg amount proposed.
      unit: The dosing unit (e.g., 'mg', 'mg/kg', 'mL', 'mL/kg', 'g').
      weight_kg: Patient weight in kilograms (crucial for pediatric calculations).
    """
    name = drug_name.lower().strip()
    
    if "adenosine" in name or "adenozin" in name:
        if weight_kg <= 0:
            return "Error: Patient weight is required for pediatric Adenosine dosage calculation."
        expected_dose_1 = 0.1 * weight_kg
        expected_dose_2 = 0.2 * weight_kg
        max_1 = 6.0
        max_2 = 12.0
        
        # Calculate actual absolute dose if dose_amount was specified in mg/kg
        actual_mg = dose_amount * weight_kg if "mg/kg" in unit else dose_amount
        
        status = "Safe"
        details = ""
        
        if actual_mg > max_2 * 1.5:
            status = "UNSAFE (Overdose)"
            details = f"The proposed dose of {actual_mg:.2f} mg is extremely high. Maximum first dose is 6 mg, and maximum second dose is 12 mg."
        elif abs(actual_mg - expected_dose_1) <= (expected_dose_1 * 0.2) or actual_mg <= max_1:
            details = f"Proposed dose of {actual_mg:.2f} mg matches the standard first-line SVT dose (0.1 mg/kg, expected: {expected_dose_1:.2f} mg, max 6 mg)."
        elif abs(actual_mg - expected_dose_2) <= (expected_dose_2 * 0.2) or actual_mg <= max_2:
            details = f"Proposed dose of {actual_mg:.2f} mg matches the standard second SVT dose (0.2 mg/kg, expected: {expected_dose_2:.2f} mg, max 12 mg)."
        else:
            status = "Incorrect Dosing"
            details = f"Standard pediatric SVT adenosine doses are 0.1 mg/kg (first dose, expected: {expected_dose_1:.2f} mg) or 0.2 mg/kg (second dose, expected: {expected_dose_2:.2f} mg)."
            
        return f"Medication: Adenosine. Status: {status}. Weight: {weight_kg} kg. Details: {details}"

    elif "epinephrine" in name or "adrenaline" in name or "epinefrin" in name or "adrenalin" in name:
        # Check standard anaphylaxis dose (0.01 mg/kg IM)
        if weight_kg <= 0:
            return "Error: Patient weight is required for pediatric Epinephrine dose verification."
        
        expected_mg = 0.01 * weight_kg
        max_limit = 0.3 if weight_kg < 50 else 0.5
        
        actual_mg = dose_amount * weight_kg if "mg/kg" in unit else dose_amount
        
        status = "Safe"
        details = ""
        
        if actual_mg > max_limit * 1.5:
            status = "UNSAFE (Overdose)"
            details = f"The proposed dose of {actual_mg:.2f} mg exceeds the safe emergency IM limit (expected 0.01 mg/kg, max {max_limit} mg for this patient)."
        elif abs(actual_mg - min(expected_mg, max_limit)) <= (expected_mg * 0.25):
            details = f"Proposed dose of {actual_mg:.2f} mg is correct for anaphylaxis (0.01 mg/kg, max {max_limit} mg)."
        else:
            status = "Incorrect Dosing"
            details = f"Standard epinephrine dose for anaphylaxis is 0.01 mg/kg IM (expected: {min(expected_mg, max_limit):.2f} mg, max {max_limit} mg)."
            
        return f"Medication: Epinephrine. Status: {status}. Weight: {weight_kg} kg. Details: {details}"

    elif "dextrose" in name or "glucose" in name or "glukoz" in name:
        if weight_kg <= 0:
            return "Error: Patient weight is required for Dextrose dose verification."
        actual_ml_kg = dose_amount if "ml/kg" in unit.lower() else (dose_amount / weight_kg if weight_kg > 0 else 0)
        
        status = "Safe"
        details = ""
        if 1.8 <= actual_ml_kg <= 2.2:
            details = f"Proposed dose of {dose_amount} mL is correct (2 mL/kg of D10W for acute hypoglycemia, expected: {2 * weight_kg:.2f} mL)."
        else:
            status = "Incorrect Dosing"
            details = f"Standard neonatal dose is 2 mL/kg of D10W (Dextrose 10%). For this baby, that is {2 * weight_kg:.2f} mL."
            
        return f"Medication: D10W. Status: {status}. Details: {details}"

    elif "calcium" in name or "kalsiyum" in name:
        if weight_kg <= 0:
            return "Error: Patient weight is required for Calcium Gluconate dose verification."
        actual_ml_kg = dose_amount if "ml/kg" in unit.lower() else (dose_amount / weight_kg)
        
        status = "Safe"
        details = ""
        if 1.0 <= actual_ml_kg <= 2.0:
            details = f"Proposed dose of {dose_amount} mL is correct (1-2 mL/kg of Calcium Gluconate 10% for hypocalcemia)."
        else:
            status = "Incorrect Dosing"
            details = f"Standard neonatal Calcium Gluconate 10% dose is 1-2 mL/kg IV slowly (expected range: {1 * weight_kg:.2f} - {2 * weight_kg:.2f} mL)."
            
        return f"Medication: Calcium Gluconate 10%. Status: {status}. Details: {details}"

    elif "phenobarbital" in name or "fenobarbital" in name:
        if weight_kg <= 0:
            return "Error: Patient weight is required for Phenobarbital loading dose verification."
        actual_mg_kg = dose_amount if "mg/kg" in unit.lower() else (dose_amount / weight_kg)
        
        status = "Safe"
        details = ""
        if 18 <= actual_mg_kg <= 22:
            details = f"Proposed dose of {dose_amount} mg is correct (20 mg/kg IV loading dose for seizures, expected: {20 * weight_kg:.2f} mg)."
        else:
            status = "Incorrect Dosing"
            details = f"Standard neonatal phenobarbital loading dose is 20 mg/kg IV slowly (expected: {20 * weight_kg:.2f} mg)."
            
        return f"Medication: Phenobarbital. Status: {status}. Details: {details}"

    elif "aspirin" in name or "asetilsalisilik" in name:
        status = "Safe"
        details = ""
        if 160 <= dose_amount <= 325:
            details = f"Proposed dose of {dose_amount} mg is correct for suspected AMI (chewable Aspirin 162-325 mg)."
        else:
            status = "Incorrect Dosing"
            details = "Standard chewable Aspirin dose for acute MI is 162 mg to 325 mg immediately."
            
        return f"Medication: Aspirin. Status: {status}. Details: {details}"

    elif "paracetamol" in name or "acetaminophen" in name or "minoset" in name or "vermidon" in name:
        status = "Information"
        details = ""
        actual_mg_kg = dose_amount if "mg/kg" in unit.lower() else (dose_amount / weight_kg if weight_kg > 0 else dose_amount)
        if actual_mg_kg >= 150 or dose_amount >= 7500:
            details = f"Dose of {dose_amount} {unit} is hepatotoxic (Toxic threshold: >150 mg/kg or 7.5 g absolute). Rumack-Matthew nomogram plotting is required."
        else:
            details = f"Dose of {dose_amount} {unit} is below standard acute toxic thresholds."
            
        return f"Medication: Paracetamol. Status: {status}. Details: {details}"

    return f"Verification not available for medication '{drug_name}'."


if __name__ == "__main__":
    # Start the FastMCP server via stdio
    mcp.run()
