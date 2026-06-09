"""
Static demo clinical cases — bilingual (EN/TR) with progressive step structure.
Each step has a scenario_update (clinical context) and a question, both in EN and TR.
"""

DEMO_CASES = {
    "peds_svt_001": {
        "case_id": "peds_svt_001",
        "case_title_en": "Pediatric SVT",
        "case_title_tr": "Pediatrik SVT (Supraventriküler Taşikardi)",
        "case_title": "Pediatric SVT",
        "topic": "Pediatric Emergency",
        "difficulty": "Intermediate",
        "weight_kg": 30.0,
        "learning_goals": [
            "ABC approach", "Vital signs", "ECG request",
            "Stable vs unstable tachycardia", "Vagal maneuver",
            "Adenosine", "Synchronized cardioversion for unstable patient",
        ],
        "steps": [
            {
                "step": 1,
                "scenario_update_en": (
                    "A 10-year-old girl is brought to the emergency department by her parents. "
                    "She has been experiencing sudden palpitations for the last 30 minutes. "
                    "She is conscious and anxious. No chest pain or syncope. "
                    "She looks scared but is talking to you."
                ),
                "scenario_update_tr": (
                    "10 yaşında kız çocuğu ailesi tarafından acile getirildi. "
                    "30 dakikadır ani başlayan çarpıntı şikayeti var. "
                    "Bilinci açık, ajite görünüyor. Göğüs ağrısı ve bayılma yok. "
                    "Korkmuş ama sizinle konuşabiliyor."
                ),
                "question_en": (
                    "What is your first approach? "
                    "What do you assess and what initial steps do you take?"
                ),
                "question_tr": (
                    "İlk yaklaşımınız ne olur? "
                    "Ne değerlendirirsiniz ve ilk adımlarınız neler?"
                ),
                "key_points": [
                    "ABC assessment",
                    "Vital signs",
                    "Cardiac monitoring",
                    "IV access",
                    "12-lead ECG",
                ],
            },
            {
                "step": 2,
                "scenario_update_en": (
                    "Initial assessment done. Vitals: HR 220 bpm, BP 100/60 mmHg, "
                    "SpO2 98% on room air, RR 20/min, Temp 37.1 C. "
                    "Patient is alert and responsive. Monitor applied — narrow-complex "
                    "regular tachycardia visible. IV access secured."
                ),
                "scenario_update_tr": (
                    "İlk değerlendirme yapıldı. Vitaller: KH 220 atım/dk, KB 100/60 mmHg, "
                    "SpO2 %%98, SS 20/dk, Ateş 37.1 C. "
                    "Hasta bilinçli ve uyumlu. Monitör takıldı — dar QRS kompleksli "
                    "düzgün taşikardi görülüyor. IV yol açıldı."
                ),
                "question_en": (
                    "12-lead ECG is on the way. "
                    "What is your clinical diagnosis and immediate management plan?"
                ),
                "question_tr": (
                    "12 derivasyonlu EKG istendi. "
                    "Klinik tanınız ne ve acil tedavi planınız nedir?"
                ),
                "key_points": [
                    "Diagnosis: SVT (Supraventricular Tachycardia)",
                    "Hemodynamic stability assessment — patient is STABLE",
                    "Vagal maneuver as first-line (Valsalva or ice to face)",
                    "Prepare adenosine as next step if vagal maneuver fails",
                ],
            },
            {
                "step": 3,
                "scenario_update_en": (
                    "ECG confirmed: regular narrow-complex tachycardia at 220 bpm, "
                    "no visible P waves — consistent with SVT. "
                    "Vagal maneuvers attempted (Valsalva + ice pack to face) — no conversion. "
                    "Rhythm unchanged. Patient remains hemodynamically stable."
                ),
                "scenario_update_tr": (
                    "EKG onaylandı: 220 atım/dk düzgün dar QRS taşikardisi, "
                    "P dalgası görülmüyor — SVT ile uyumlu. "
                    "Vagal manevra uygulandı (Valsalva + yüze buz) — ritim dönmedi. "
                    "Hasta hemodinamik olarak stabil."
                ),
                "question_en": (
                    "Vagal maneuvers failed. "
                    "What medication do you use, at what dose, and how exactly do you administer it?"
                ),
                "question_tr": (
                    "Vagal manevra başarısız oldu. "
                    "Hangi ilacı, hangi dozda ve nasıl uygularsınız?"
                ),
                "key_points": [
                    "Adenosine",
                    "Dose: 0.1 mg/kg IV bolus (max first dose 6 mg)",
                    "Rapid IV push followed by immediate saline flush",
                    "Continuous cardiac monitoring during administration",
                    "Warn patient of brief chest discomfort/flushing",
                ],
            },
            {
                "step": 4,
                "scenario_update_en": (
                    "After your intervention, the patient suddenly deteriorates. "
                    "New vitals: HR 220 bpm, BP drops to 70/40 mmHg, "
                    "patient becomes less responsive (GCS 12), skin is pale and mottled. "
                    "ECG still shows narrow-complex tachycardia at 220 bpm."
                ),
                "scenario_update_tr": (
                    "Müdahalenizin ardından hasta aniden kötüleşti. "
                    "Yeni vitaller: KH 220 atım/dk, KB 70/40 mmHg'ye düştü, "
                    "bilinci bulanıklaşıyor (GKS 12), deri soluk ve alacalı. "
                    "EKG hâlâ 220 atım/dk dar QRS taşikardisi."
                ),
                "question_en": (
                    "The patient is now hemodynamically UNSTABLE with ongoing tachycardia. "
                    "What is your immediate action?"
                ),
                "question_tr": (
                    "Hasta artık taşikardi ile birlikte hemodinamik olarak İNSTABİL durumda. "
                    "Acil adımınız ne?"
                ),
                "key_points": [
                    "Recognize hemodynamic instability",
                    "Synchronized cardioversion (NOT unsynchronized defibrillation)",
                    "Energy dose: 0.5-1 J/kg",
                    "Sedation/analgesia before cardioversion if time allows",
                    "Call for team support / announce emergency",
                ],
            },
            {
                "step": 5,
                "scenario_update_en": (
                    "Synchronized cardioversion performed at 1 J/kg. "
                    "Patient converts to sinus rhythm. "
                    "New vitals: HR 85 bpm, BP 110/70 mmHg, SpO2 99%, patient alert and responsive. "
                    "Good color and perfusion returning."
                ),
                "scenario_update_tr": (
                    "1 J/kg senkronize kardiyoversiyon uygulandı. "
                    "Hasta sinüs ritmine döndü. "
                    "Yeni vitaller: KH 85 atım/dk, KB 110/70 mmHg, SpO2 %%99, hasta uyanık ve yanıtlı. "
                    "Renk ve perfüzyon düzelmekte."
                ),
                "question_en": (
                    "Patient has converted to sinus rhythm. "
                    "What are your post-conversion monitoring steps, required investigations, "
                    "and disposition plan?"
                ),
                "question_tr": (
                    "Hasta sinüs ritmine döndü. "
                    "Konversiyon sonrası izlem adımlarınız, isteyeceğiniz tetkikler "
                    "ve taburculuk/yatış planınız nedir?"
                ),
                "key_points": [
                    "Continuous cardiac monitoring",
                    "Repeat vital signs frequently",
                    "Post-conversion 12-lead ECG",
                    "Cardiology consultation",
                    "Admit for observation (risk of recurrence)",
                    "Discuss recurrence prevention and prophylaxis with family",
                ],
            },
        ],
    },

    "neonatal_seizure_001": {
        "case_id": "neonatal_seizure_001",
        "case_title_en": "Neonatal Seizure",
        "case_title_tr": "Yenidoğan Nöbeti",
        "case_title": "Neonatal Seizure",
        "topic": "Neonatology",
        "difficulty": "Intermediate",
        "weight_kg": 3.0,
        "learning_goals": [
            "Immediate stabilization", "Glucose check",
            "Calcium and electrolyte assessment", "Sepsis evaluation",
            "Hypoxic ischemic injury", "Intracranial hemorrhage", "Metabolic causes",
        ],
        "steps": [
            {
                "step": 1,
                "scenario_update_en": (
                    "A 3-day-old newborn is brought to the emergency department by the mother. "
                    "She reports abnormal jerking movements of arms and legs for the last 10 minutes "
                    "and poor feeding since yesterday. Normal vaginal delivery at term, "
                    "discharged home 24 hours ago. No fever reported."
                ),
                "scenario_update_tr": (
                    "3 günlük yenidoğan annesi tarafından acile getirildi. "
                    "Anne, 10 dakikadır kol ve bacaklarda anormal sarsıntılı hareketler "
                    "ve dünden beri emme güçlüğü olduğunu bildiriyor. "
                    "Normal vajinal doğum, 24 saat önce taburcu. Ateş bildirilmiyor."
                ),
                "question_en": (
                    "What is your first approach? "
                    "What do you assess and what are your immediate priorities?"
                ),
                "question_tr": (
                    "İlk yaklaşımınız ne? "
                    "Neyi değerlendirirsiniz ve acil öncelikleriniz neler?"
                ),
                "key_points": [
                    "Airway, Breathing, Circulation",
                    "Oxygen supplementation if SpO2 low",
                    "IV access",
                    "Immediate bedside blood glucose check",
                    "Cardiac monitoring and pulse oximetry",
                ],
            },
            {
                "step": 2,
                "scenario_update_en": (
                    "Vital signs: HR 162, RR 48, SpO2 94%% on room air, Temp 36.8 C. "
                    "Active generalized tonic-clonic jerking movements ongoing. "
                    "IV access secured. "
                    "Bedside glucose: 28 mg/dL — CRITICALLY LOW."
                ),
                "scenario_update_tr": (
                    "Vitaller: KH 162, SS 48, SpO2 %%94, Ateş 36.8 C. "
                    "Aktif jeneralize tonik-klonik sarsıntı hareketleri devam ediyor. "
                    "IV yol açıldı. "
                    "Bedside glükoz: 28 mg/dL — KRİTİK DÜŞÜK."
                ),
                "question_en": (
                    "Blood glucose is critically low. "
                    "What is your immediate treatment? "
                    "Which other urgent laboratory tests do you order?"
                ),
                "question_tr": (
                    "Kan şekeri kritik düşük. "
                    "Acil tedaviniz ne? "
                    "Hangi diğer acil laboratuvar tetkiklerini istiyorsunuz?"
                ),
                "key_points": [
                    "IV dextrose bolus: D10W 2 mL/kg",
                    "Followed by continuous dextrose infusion",
                    "Check serum sodium, potassium, calcium, magnesium",
                    "Serum calcium (hypocalcemia is common neonatal seizure cause)",
                    "Blood culture before antibiotics",
                ],
            },
            {
                "step": 3,
                "scenario_update_en": (
                    "Glucose corrected to 68 mg/dL after dextrose. Seizures continuing. "
                    "Lab results back: Sodium 137, Potassium 4.2, "
                    "Calcium 6.4 mg/dL (LOW — normal >8), Magnesium 1.8. "
                    "Blood culture drawn. CBC: WBC 18000 with left shift."
                ),
                "scenario_update_tr": (
                    "Glükoz 68 mg/dL'ye düzeltildi. Nöbetler devam ediyor. "
                    "Lab sonuçları geldi: Sodyum 137, Potasyum 4.2, "
                    "Kalsiyum 6.4 mg/dL (DÜŞÜK — normal >8), Magnezyum 1.8. "
                    "Kan kültürü alındı. CBC: Sol kayma ile BK 18000."
                ),
                "question_en": (
                    "Glucose corrected but seizures continue. Calcium is low. "
                    "What treatments do you give now? "
                    "CBC shows possible infection — what do you do?"
                ),
                "question_tr": (
                    "Glükoz düzeltildi ama nöbetler devam ediyor. Kalsiyum düşük. "
                    "Şimdi hangi tedavileri verirsiniz? "
                    "CBC enfeksiyon düşündürüyor — ne yaparsınız?"
                ),
                "key_points": [
                    "IV calcium gluconate 10%% 1-2 mL/kg slowly (over 5-10 min)",
                    "Cardiac monitoring during calcium infusion",
                    "Phenobarbital as first-line anticonvulsant if seizures persist",
                    "Empirical antibiotics for sepsis (ampicillin + gentamicin)",
                ],
            },
            {
                "step": 4,
                "scenario_update_en": (
                    "Calcium and phenobarbital given. Seizures now controlled. "
                    "Baby admitted to NICU. "
                    "LP performed: CSF WBC 120/mm3, protein elevated, glucose low. "
                    "HSV PCR sent. Gram stain pending."
                ),
                "scenario_update_tr": (
                    "Kalsiyum ve fenobarbital verildi. Nöbetler kontrol altında. "
                    "Bebek YYBÜ'ne yatırıldı. "
                    "LP yapıldı: BOS BK 120/mm3, protein yüksek, glükoz düşük. "
                    "HSV PCR gönderildi. Gram boyama bekleniyor."
                ),
                "question_en": (
                    "CSF results suggest meningitis. "
                    "What is your diagnosis and how do you adjust your treatment? "
                    "What additional coverage do you add?"
                ),
                "question_tr": (
                    "BOS sonuçları menenjit düşündürüyor. "
                    "Tanınız ne ve tedaviyi nasıl düzenliyorsunuz? "
                    "Hangi ek kapsamı ekliyorsunuz?"
                ),
                "key_points": [
                    "Diagnosis: Neonatal bacterial meningitis",
                    "Continue ampicillin + gentamicin (or add cefotaxime)",
                    "Add acyclovir for HSV coverage (neonatal herpes meningitis)",
                    "Repeat LP at 48-72 hours to assess treatment response",
                    "Neurology and infectious disease consultation",
                ],
            },
            {
                "step": 5,
                "scenario_update_en": (
                    "Day 3 of NICU admission. Baby clinically improving. "
                    "Blood culture: Streptococcus agalactiae (Group B Strep). "
                    "HSV PCR negative. Repeat CSF normalizing. "
                    "MRI head ordered — pending."
                ),
                "scenario_update_tr": (
                    "YYBÜ yatışının 3. günü. Bebek klinik olarak iyileşiyor. "
                    "Kan kültürü: Streptococcus agalactiae (Grup B Streptokok). "
                    "HSV PCR negatif. Tekrar BOS normalleşiyor. "
                    "Kafa MRI'ı istendi — bekleniyor."
                ),
                "question_en": (
                    "Blood culture grew Group B Strep. HSV is negative. "
                    "How do you adjust antibiotics? "
                    "What is the total treatment duration and what do you monitor long-term?"
                ),
                "question_tr": (
                    "Kan kültüründe Grup B Streptokok üredi. HSV negatif. "
                    "Antibiyotiği nasıl düzenlersiniz? "
                    "Toplam tedavi süresi ne ve uzun vadede ne izlersiniz?"
                ),
                "key_points": [
                    "Switch to high-dose IV penicillin G (definitive for GBS)",
                    "Total treatment duration: 14-21 days for GBS meningitis",
                    "Discontinue acyclovir (HSV negative)",
                    "Long-term neurodevelopmental follow-up",
                    "Hearing screen before discharge",
                    "MRI for neurological sequelae assessment",
                ],
            },
        ],
    },

    "anaphylaxis_001": {
        "case_id": "anaphylaxis_001",
        "case_title_en": "Pediatric Anaphylaxis",
        "case_title_tr": "Pediatrik Anafilaksi",
        "case_title": "Pediatric Anaphylaxis",
        "topic": "Allergy and Anaphylaxis",
        "difficulty": "Beginner",
        "weight_kg": 22.0,
        "learning_goals": [
            "Recognition of anaphylaxis", "Airway, breathing, circulation",
            "Intramuscular adrenaline/epinephrine", "Oxygen", "IV fluids",
            "Observation", "Avoiding delay in epinephrine",
        ],
        "steps": [
            {
                "step": 1,
                "scenario_update_en": (
                    "A 7-year-old child is brought to the emergency department. "
                    "Parents report she ate peanuts about 15 minutes ago. "
                    "She now has generalized hives all over her body, "
                    "her face and lips are visibly swelling, she is coughing "
                    "and tells you she cannot breathe properly."
                ),
                "scenario_update_tr": (
                    "7 yaşında kız çocuğu acile getirildi. "
                    "Yaklaşık 15 dakika önce yer fıstığı yediğini ebeveynler bildiriyor. "
                    "Tüm vücudunda jeneralize ürtikerler var, "
                    "yüz ve dudaklarında belirgin şişlik, öksürük var "
                    "ve nefes alamadığını söylüyor."
                ),
                "question_en": (
                    "What is your immediate approach? "
                    "What is the most critical life-saving intervention?"
                ),
                "question_tr": (
                    "Acil yaklaşımınız ne? "
                    "En kritik hayat kurtarıcı müdahale nedir?"
                ),
                "key_points": [
                    "Recognize anaphylaxis",
                    "Call for help immediately",
                    "Intramuscular epinephrine 0.01 mg/kg (max 0.5 mg) — FIRST LINE",
                    "Position: supine with legs elevated or upright if respiratory distress",
                    "High-flow oxygen",
                ],
            },
            {
                "step": 2,
                "scenario_update_en": (
                    "IM epinephrine given. Vitals: HR 148, BP 80/50 mmHg, "
                    "SpO2 88%% on room air, RR 36/min. "
                    "Stridor audible. Bilateral wheeze on auscultation. "
                    "Child increasingly anxious. IV access not yet established."
                ),
                "scenario_update_tr": (
                    "İM epinefrin verildi. Vitaller: KH 148, KB 80/50 mmHg, "
                    "SpO2 %%88, SS 36/dk. "
                    "Stridor duyuluyor. Oskültasyonda bilateral hışırtı mevcut. "
                    "Çocuk giderek ajite oluyor. IV yol henüz yok."
                ),
                "question_en": (
                    "Initial epinephrine given but patient still deteriorating. "
                    "SpO2 is 88%%, BP is low, stridor and wheeze persist. "
                    "What are your next steps?"
                ),
                "question_tr": (
                    "İlk epinefrin verildi ama hasta hâlâ kötüleşiyor. "
                    "SpO2 %%88, KB düşük, stridor ve hışırtı devam ediyor. "
                    "Sonraki adımlarınız ne?"
                ),
                "key_points": [
                    "High-flow oxygen via non-rebreather mask",
                    "Establish IV or IO access urgently",
                    "IV normal saline bolus 10-20 mL/kg for hypotension",
                    "Second dose IM epinephrine if no improvement in 5-15 minutes",
                    "Nebulized salbutamol for bronchospasm",
                    "Prepare for airway management (possible intubation)",
                ],
            },
            {
                "step": 3,
                "scenario_update_en": (
                    "After IV fluids and second epinephrine dose: "
                    "SpO2 improves to 96%%, BP 105/65 mmHg, stridor resolving, "
                    "wheeze reduced. Child is more alert. Urticaria still visible. "
                    "The team asks about antihistamines and steroids."
                ),
                "scenario_update_tr": (
                    "IV sıvı ve ikinci epinefrin dozundan sonra: "
                    "SpO2 %%96'ya yükseldi, KB 105/65 mmHg, stridor geriliyor, "
                    "hışırtı azaldı. Çocuk daha uyanık. Ürtiker hâlâ mevcut. "
                    "Ekip antihistaminik ve steroid sormakta."
                ),
                "question_en": (
                    "Patient is stabilizing. "
                    "What is the role of antihistamines and steroids here? "
                    "Do you give them? When and why?"
                ),
                "question_tr": (
                    "Hasta stabilize oluyor. "
                    "Antihistaminik ve steroidin buradaki rolü ne? "
                    "Verir misiniz? Ne zaman ve neden?"
                ),
                "key_points": [
                    "Antihistamines and steroids are SECOND-LINE — never replace epinephrine",
                    "Antihistamines (diphenhydramine) for skin symptoms (not for anaphylaxis reversal)",
                    "IV/oral corticosteroids to reduce risk of biphasic reaction",
                    "Do NOT delay epinephrine to give antihistamines",
                    "Biphasic anaphylaxis can occur 4-12 hours after initial reaction",
                ],
            },
            {
                "step": 4,
                "scenario_update_en": (
                    "Child is now stable. SpO2 99%%, BP 112/70 mmHg, no stridor, "
                    "urticaria fading. She is hungry and asking for water. "
                    "Parents are asking when they can go home and what to do next."
                ),
                "scenario_update_tr": (
                    "Çocuk şimdi stabil. SpO2 %%99, KB 112/70 mmHg, stridor yok, "
                    "ürtiker soluklaşıyor. Aç ve su istiyor. "
                    "Ebeveynler eve ne zaman gidebileceklerini ve ne yapacaklarını soruyor."
                ),
                "question_en": (
                    "Patient is clinically stable. "
                    "What is your minimum observation period and why? "
                    "What must you prescribe and teach the family before discharge?"
                ),
                "question_tr": (
                    "Hasta klinik olarak stabil. "
                    "Minimum gözlem süreniz ne ve neden? "
                    "Taburculuk öncesi aileye ne reçete eder ve ne öğretirsiniz?"
                ),
                "key_points": [
                    "Observe minimum 4-6 hours (biphasic anaphylaxis risk)",
                    "Prescribe auto-injectable epinephrine (EpiPen / EpiPen Jr)",
                    "Written anaphylaxis action plan",
                    "Allergen avoidance education for family and child",
                    "Allergy/immunology referral",
                    "Follow-up with primary care",
                ],
            },
        ],
    },
}


# Merge extra cases into DEMO_CASES
from app.data.extra_cases import EXTRA_CASES
DEMO_CASES.update(EXTRA_CASES)


TOPIC_TO_CASE_MAP = {
    "Pediatric Emergency": ["peds_svt_001"],
    "Neonatology": ["neonatal_seizure_001"],
    "Allergy and Anaphylaxis": ["anaphylaxis_001"],
    "Cardiology": ["cardio_ami_001", "cardio_hf_001"],
    "Trauma / Emergency Surgery": ["trauma_poly_001", "trauma_abd_001"],
    "Intoxication / Poisoning": ["intox_paracetamol_001", "intox_oph_001"],
    "Respiratory Failure": ["resp_asthma_001"],
}


def get_case_for_topic(topic: str, difficulty: str, weak_topics: list[str] | None = None) -> dict:
    """Return the best matching demo case for a given topic.

    Selection logic:
    1. Filter cases by topic mapping.
    2. Prefer cases whose difficulty matches the requested difficulty.
    3. If weak_topics provided, prefer cases whose learning_goals overlap.
    4. If multiple candidates remain, pick randomly for variety.
    """
    import random

    case_ids = TOPIC_TO_CASE_MAP.get(topic, list(DEMO_CASES.keys()))
    candidates = [DEMO_CASES[cid] for cid in case_ids if cid in DEMO_CASES]

    if not candidates:
        candidates = list(DEMO_CASES.values())

    # Prefer matching difficulty
    diff_matched = [c for c in candidates if c.get("difficulty", "").lower() == difficulty.lower()]
    if diff_matched:
        candidates = diff_matched

    # Prefer cases whose learning goals overlap with weak topics
    if weak_topics:
        weak_lower = {wt.lower() for wt in weak_topics}

        def overlap_score(case: dict) -> int:
            goals = {g.lower() for g in case.get("learning_goals", [])}
            return len(goals & weak_lower)

        candidates.sort(key=overlap_score, reverse=True)
        best_overlap = overlap_score(candidates[0])
        if best_overlap > 0:
            candidates = [c for c in candidates if overlap_score(c) == best_overlap]

    return random.choice(candidates)


def get_step_content(case_data: dict, step_number: int, language: str = "en") -> tuple[str, str]:
    """Return (scenario_update, question) for a step in the given language."""
    steps = case_data.get("steps", [])
    step = next((s for s in steps if s["step"] == step_number), None)
    if not step:
        return "", ""
    lang = language if language in ("en", "tr") else "en"
    scenario = step.get(f"scenario_update_{lang}") or step.get("scenario_update_en", "")
    question = step.get(f"question_{lang}") or step.get("question_en", "")
    return scenario, question


def get_case_title(case_data: dict, language: str = "en") -> str:
    """Return case title in the given language."""
    lang = language if language in ("en", "tr") else "en"
    return case_data.get(f"case_title_{lang}") or case_data.get("case_title", "")
