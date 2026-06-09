"""
OSCE Station Data — Bilingual (EN/TR)
Objective Structured Clinical Examination station definitions.
Each OSCE set contains 4 timed stations with standardized patient scenarios.
"""

OSCE_SETS = {
    "osce_pediatric_emergency": {
        "set_id": "osce_pediatric_emergency",
        "title_en": "Pediatric Emergency OSCE",
        "title_tr": "Pediatrik Acil OSCE",
        "description_en": "Four-station OSCE covering pediatric emergency scenarios including SVT, anaphylaxis, seizures, and respiratory distress.",
        "description_tr": "SVT, anafilaksi, nöbet ve solunum sıkıntısı dahil pediatrik acil senaryolarını kapsayan dört istasyonlu OSCE.",
        "difficulty": "Intermediate",
        "stations": [
            {
                "station_id": "osce_ped_s1",
                "station_number": 1,
                "title_en": "Station 1 — History Taking: Palpitations",
                "title_tr": "İstasyon 1 — Öykü Alma: Çarpıntı",
                "time_limit_seconds": 480,
                "station_type": "history",
                "patient_scenario_en": (
                    "You are a physician in the pediatric emergency department. "
                    "A mother brings her 10-year-old daughter who has been experiencing "
                    "sudden onset palpitations for the last 30 minutes. The child is "
                    "conscious and anxious but has no chest pain or syncope.\n\n"
                    "The standardized patient (mother) will answer your questions."
                ),
                "patient_scenario_tr": (
                    "Pediatrik acil serviste görev yapan bir hekimsiniz. "
                    "Bir anne, 30 dakikadır ani başlayan çarpıntı şikayeti olan "
                    "10 yaşındaki kızını getiriyor. Çocuk bilinçli ve ajite "
                    "ama göğüs ağrısı veya bayılma yok.\n\n"
                    "Standart hasta (anne) sorularınızı cevaplayacaktır."
                ),
                "task_en": (
                    "Take a focused history from the mother. Cover:\n"
                    "- Onset, duration, and characteristics of palpitations\n"
                    "- Associated symptoms (chest pain, syncope, dyspnea)\n"
                    "- Past medical history and medications\n"
                    "- Family history of cardiac disease\n"
                    "- Initial assessment plan"
                ),
                "task_tr": (
                    "Anneden odaklanmış bir öykü alın. Şunları kapsayın:\n"
                    "- Çarpıntının başlangıcı, süresi ve özellikleri\n"
                    "- Eşlik eden semptomlar (göğüs ağrısı, bayılma, nefes darlığı)\n"
                    "- Geçmiş tıbbi öykü ve ilaçlar\n"
                    "- Ailede kalp hastalığı öyküsü\n"
                    "- İlk değerlendirme planı"
                ),
                "key_points": [
                    "Onset and duration of palpitations",
                    "Associated symptoms screening",
                    "Previous episodes or known cardiac history",
                    "Family history of sudden cardiac death or arrhythmias",
                    "Current medications and allergies",
                    "Initial ABC assessment plan",
                ],
                "checklist": [
                    {"item": "Asked about onset and duration", "category": "History"},
                    {"item": "Asked about associated chest pain", "category": "History"},
                    {"item": "Asked about syncope or near-syncope", "category": "History"},
                    {"item": "Asked about breathing difficulty", "category": "History"},
                    {"item": "Asked about previous similar episodes", "category": "History"},
                    {"item": "Asked about past medical history", "category": "History"},
                    {"item": "Asked about medications", "category": "History"},
                    {"item": "Asked about family cardiac history", "category": "History"},
                    {"item": "Mentioned ABC assessment", "category": "Management"},
                    {"item": "Mentioned vital signs and ECG", "category": "Management"},
                ],
            },
            {
                "station_id": "osce_ped_s2",
                "station_number": 2,
                "title_en": "Station 2 — Diagnosis & Management: SVT",
                "title_tr": "İstasyon 2 — Tanı ve Tedavi: SVT",
                "time_limit_seconds": 480,
                "station_type": "management",
                "patient_scenario_en": (
                    "Continuing from the previous patient. ECG shows regular "
                    "narrow-complex tachycardia at 220 bpm with no visible P waves. "
                    "Vitals: HR 220, BP 100/60, SpO2 98%. The child is hemodynamically "
                    "stable. IV access is secured.\n\n"
                    "Describe your diagnosis and step-by-step management plan."
                ),
                "patient_scenario_tr": (
                    "Önceki hastadan devam. EKG'de 220 atım/dk hızla düzgün dar QRS "
                    "taşikardisi, P dalgası görülmüyor. Vitaller: KH 220, KB 100/60, "
                    "SpO2 %98. Çocuk hemodinamik olarak stabil. IV yol açık.\n\n"
                    "Tanınızı ve adım adım tedavi planınızı açıklayın."
                ),
                "task_en": (
                    "1. State your diagnosis\n"
                    "2. Describe first-line treatment\n"
                    "3. Describe second-line treatment if first-line fails\n"
                    "4. State what you would do if the patient becomes unstable"
                ),
                "task_tr": (
                    "1. Tanınızı belirtin\n"
                    "2. İlk basamak tedaviyi açıklayın\n"
                    "3. İlk basamak başarısız olursa ikinci basamak tedaviyi açıklayın\n"
                    "4. Hasta instabil olursa ne yapacağınızı belirtin"
                ),
                "key_points": [
                    "Diagnosis: SVT (Supraventricular Tachycardia)",
                    "Hemodynamic stability assessment",
                    "Vagal maneuvers as first-line",
                    "Adenosine 0.1 mg/kg rapid IV push if vagal fails",
                    "Synchronized cardioversion for unstable patient",
                    "Continuous monitoring",
                ],
                "checklist": [
                    {"item": "Correctly diagnosed SVT", "category": "Diagnosis"},
                    {"item": "Assessed hemodynamic stability", "category": "Assessment"},
                    {"item": "Mentioned vagal maneuvers as first-line", "category": "Management"},
                    {"item": "Described specific vagal techniques", "category": "Management"},
                    {"item": "Mentioned adenosine with correct dose", "category": "Management"},
                    {"item": "Described rapid push with flush technique", "category": "Management"},
                    {"item": "Mentioned synchronized cardioversion for unstable", "category": "Management"},
                    {"item": "Mentioned correct energy dose for cardioversion", "category": "Management"},
                    {"item": "Mentioned continuous cardiac monitoring", "category": "Monitoring"},
                    {"item": "Mentioned sedation before cardioversion", "category": "Management"},
                ],
            },
            {
                "station_id": "osce_ped_s3",
                "station_number": 3,
                "title_en": "Station 3 — Emergency Management: Anaphylaxis",
                "title_tr": "İstasyon 3 — Acil Müdahale: Anafilaksi",
                "time_limit_seconds": 480,
                "station_type": "management",
                "patient_scenario_en": (
                    "A 7-year-old child is brought to the ED with generalized urticaria, "
                    "facial swelling, stridor, and difficulty breathing 15 minutes after "
                    "eating peanuts. She is anxious and using accessory muscles.\n\n"
                    "Vitals: HR 148, BP 80/50, SpO2 88%, RR 36.\n\n"
                    "Describe your immediate management."
                ),
                "patient_scenario_tr": (
                    "7 yaşında çocuk, yer fıstığı yedikten 15 dakika sonra jeneralize "
                    "ürtiker, yüz şişliği, stridor ve nefes güçlüğü ile acile getirildi. "
                    "Anksiyöz ve yardımcı solunum kaslarını kullanıyor.\n\n"
                    "Vitaller: KH 148, KB 80/50, SpO2 %88, SS 36.\n\n"
                    "Acil tedavinizi açıklayın."
                ),
                "task_en": (
                    "1. State your diagnosis\n"
                    "2. Describe the most critical first intervention\n"
                    "3. List your additional management steps in order of priority\n"
                    "4. Describe your monitoring and observation plan"
                ),
                "task_tr": (
                    "1. Tanınızı belirtin\n"
                    "2. En kritik ilk müdahaleyi açıklayın\n"
                    "3. Ek tedavi adımlarını öncelik sırasına göre listeleyin\n"
                    "4. İzlem ve gözlem planınızı açıklayın"
                ),
                "key_points": [
                    "Recognize anaphylaxis",
                    "IM epinephrine 0.01 mg/kg as FIRST priority",
                    "High-flow oxygen",
                    "IV access and fluid bolus",
                    "Second dose epinephrine if needed",
                    "Observation for biphasic reaction",
                ],
                "checklist": [
                    {"item": "Correctly diagnosed anaphylaxis", "category": "Diagnosis"},
                    {"item": "IM epinephrine as first priority", "category": "Management"},
                    {"item": "Correct epinephrine dose", "category": "Management"},
                    {"item": "High-flow oxygen applied", "category": "Management"},
                    {"item": "IV/IO access established", "category": "Management"},
                    {"item": "IV fluid bolus for hypotension", "category": "Management"},
                    {"item": "Mentioned second epinephrine dose", "category": "Management"},
                    {"item": "Mentioned airway preparation", "category": "Management"},
                    {"item": "Mentioned antihistamines as second-line", "category": "Management"},
                    {"item": "Observation period for biphasic reaction", "category": "Monitoring"},
                ],
            },
            {
                "station_id": "osce_ped_s4",
                "station_number": 4,
                "title_en": "Station 4 — Communication: Discharge Counseling",
                "title_tr": "İstasyon 4 — İletişim: Taburculuk Danışmanlığı",
                "time_limit_seconds": 480,
                "station_type": "communication",
                "patient_scenario_en": (
                    "The anaphylaxis patient from Station 3 has been stabilized and "
                    "observed for 6 hours. She is ready for discharge. The parents are "
                    "anxious and asking questions.\n\n"
                    "Counsel the parents about discharge planning, including "
                    "medication prescriptions and safety education."
                ),
                "patient_scenario_tr": (
                    "İstasyon 3'teki anafilaksi hastası stabilize edildi ve 6 saat "
                    "gözlemlendi. Taburculuğa hazır. Ebeveynler endişeli ve soru soruyor.\n\n"
                    "Ebeveynlere taburculuk planı, ilaç reçeteleri ve güvenlik "
                    "eğitimi hakkında danışmanlık yapın."
                ),
                "task_en": (
                    "1. Explain what happened to the child\n"
                    "2. Prescribe and demonstrate epinephrine auto-injector use\n"
                    "3. Create an anaphylaxis action plan\n"
                    "4. Discuss allergen avoidance and follow-up"
                ),
                "task_tr": (
                    "1. Çocuğa ne olduğunu açıklayın\n"
                    "2. Epinefrin oto-enjektörü reçete edin ve kullanımını gösterin\n"
                    "3. Anafilaksi eylem planı oluşturun\n"
                    "4. Alerjen kaçınma ve takip planını tartışın"
                ),
                "key_points": [
                    "Clear explanation of anaphylaxis",
                    "EpiPen prescription and demonstration",
                    "Written anaphylaxis action plan",
                    "Allergen avoidance education",
                    "Allergy referral",
                    "School notification advice",
                ],
                "checklist": [
                    {"item": "Explained anaphylaxis in simple terms", "category": "Communication"},
                    {"item": "Prescribed epinephrine auto-injector", "category": "Management"},
                    {"item": "Demonstrated or explained auto-injector use", "category": "Communication"},
                    {"item": "Provided written action plan", "category": "Management"},
                    {"item": "Discussed allergen avoidance", "category": "Education"},
                    {"item": "Mentioned school/daycare notification", "category": "Education"},
                    {"item": "Referred to allergy specialist", "category": "Management"},
                    {"item": "Discussed when to return to ED", "category": "Education"},
                    {"item": "Used empathetic and clear communication", "category": "Communication"},
                    {"item": "Asked if parents have questions", "category": "Communication"},
                ],
            },
        ],
    },

    "osce_internal_medicine": {
        "set_id": "osce_internal_medicine",
        "title_en": "Internal Medicine OSCE",
        "title_tr": "İç Hastalıkları OSCE",
        "description_en": "Four-station OSCE covering chest pain evaluation, heart failure management, drug overdose, and patient communication.",
        "description_tr": "Göğüs ağrısı değerlendirmesi, kalp yetmezliği yönetimi, ilaç doz aşımı ve hasta iletişimini kapsayan dört istasyonlu OSCE.",
        "difficulty": "Advanced",
        "stations": [
            {
                "station_id": "osce_im_s1",
                "station_number": 1,
                "title_en": "Station 1 — Chest Pain Assessment",
                "title_tr": "İstasyon 1 — Göğüs Ağrısı Değerlendirmesi",
                "time_limit_seconds": 480,
                "station_type": "history",
                "patient_scenario_en": (
                    "A 58-year-old male presents with crushing substernal chest pain "
                    "radiating to the left arm for 45 minutes. He is diaphoretic and "
                    "pale. History of hypertension and 30 pack-year smoking.\n\n"
                    "Take a focused history and describe your initial assessment plan."
                ),
                "patient_scenario_tr": (
                    "58 yaşında erkek hasta, 45 dakikadır sol kola yayılan ezici "
                    "substernal göğüs ağrısı ile başvurdu. Terleme ve solukluk mevcut. "
                    "Hipertansiyon ve 30 paket-yıl sigara öyküsü var.\n\n"
                    "Odaklanmış öykü alın ve ilk değerlendirme planınızı açıklayın."
                ),
                "task_en": (
                    "1. Take a focused cardiac history (SOCRATES)\n"
                    "2. Identify risk factors\n"
                    "3. Describe your immediate investigations\n"
                    "4. State your initial management"
                ),
                "task_tr": (
                    "1. Odaklanmış kardiyak öykü alın (SOCRATES)\n"
                    "2. Risk faktörlerini belirleyin\n"
                    "3. Acil tetkiklerinizi açıklayın\n"
                    "4. İlk tedavinizi belirtin"
                ),
                "key_points": [
                    "SOCRATES pain assessment",
                    "Cardiac risk factors",
                    "12-lead ECG within 10 minutes",
                    "Aspirin 300 mg immediately",
                    "Troponin and cardiac biomarkers",
                    "IV access and monitoring",
                ],
                "checklist": [
                    {"item": "Used structured pain assessment (SOCRATES)", "category": "History"},
                    {"item": "Asked about radiation pattern", "category": "History"},
                    {"item": "Identified cardiac risk factors", "category": "Assessment"},
                    {"item": "Ordered 12-lead ECG urgently", "category": "Investigation"},
                    {"item": "Gave aspirin 300 mg", "category": "Management"},
                    {"item": "Ordered troponin", "category": "Investigation"},
                    {"item": "Established IV access", "category": "Management"},
                    {"item": "Applied cardiac monitoring", "category": "Monitoring"},
                    {"item": "Considered differential diagnoses", "category": "Assessment"},
                    {"item": "Mentioned oxygen if SpO2 low", "category": "Management"},
                ],
            },
            {
                "station_id": "osce_im_s2",
                "station_number": 2,
                "title_en": "Station 2 — ECG Interpretation & STEMI Management",
                "title_tr": "İstasyon 2 — EKG Yorumlama ve STEMI Tedavisi",
                "time_limit_seconds": 480,
                "station_type": "diagnosis",
                "patient_scenario_en": (
                    "The ECG from Station 1 shows: ST elevation in leads II, III, aVF "
                    "(>2mm), reciprocal ST depression in I and aVL. "
                    "Troponin I is elevated.\n\n"
                    "Interpret the ECG and describe your definitive management."
                ),
                "patient_scenario_tr": (
                    "İstasyon 1'den EKG: II, III, aVF'de ST elevasyonu (>2mm), "
                    "I ve aVL'de resiprokal ST depresyonu. Troponin I yüksek.\n\n"
                    "EKG'yi yorumlayın ve kesin tedavinizi açıklayın."
                ),
                "task_en": (
                    "1. Interpret the ECG findings\n"
                    "2. State your diagnosis\n"
                    "3. Describe reperfusion strategy\n"
                    "4. List all medications needed"
                ),
                "task_tr": (
                    "1. EKG bulgularını yorumlayın\n"
                    "2. Tanınızı belirtin\n"
                    "3. Reperfüzyon stratejisini açıklayın\n"
                    "4. Gereken tüm ilaçları listeleyin"
                ),
                "key_points": [
                    "Inferior STEMI diagnosis",
                    "Activate cath lab for primary PCI",
                    "Dual antiplatelet therapy",
                    "Anticoagulation",
                    "Check right-sided ECG (V4R)",
                    "Door-to-balloon target <90 minutes",
                ],
                "checklist": [
                    {"item": "Identified ST elevation territory", "category": "Interpretation"},
                    {"item": "Diagnosed inferior STEMI", "category": "Diagnosis"},
                    {"item": "Activated cath lab / mentioned PCI", "category": "Management"},
                    {"item": "Mentioned door-to-balloon time", "category": "Management"},
                    {"item": "Added P2Y12 inhibitor", "category": "Management"},
                    {"item": "Mentioned heparin anticoagulation", "category": "Management"},
                    {"item": "Checked right-sided ECG (V4R)", "category": "Investigation"},
                    {"item": "Mentioned morphine for pain if needed", "category": "Management"},
                    {"item": "Considered RV infarction", "category": "Assessment"},
                    {"item": "Mentioned avoiding nitrates in RV infarction", "category": "Safety"},
                ],
            },
            {
                "station_id": "osce_im_s3",
                "station_number": 3,
                "title_en": "Station 3 — Acute Heart Failure Management",
                "title_tr": "İstasyon 3 — Akut Kalp Yetmezliği Tedavisi",
                "time_limit_seconds": 480,
                "station_type": "management",
                "patient_scenario_en": (
                    "A 72-year-old female with known CHF presents with acute dyspnea, "
                    "orthopnea, and pink frothy sputum. She stopped her furosemide 3 days ago.\n\n"
                    "Vitals: HR 120, BP 180/100, SpO2 85%, RR 32. "
                    "Bilateral crackles on auscultation. JVP elevated.\n\n"
                    "Describe your management."
                ),
                "patient_scenario_tr": (
                    "72 yaşında bilinen KKY'li kadın hasta, akut nefes darlığı, "
                    "ortopne ve pembe köpüklü balgam ile başvurdu. 3 gündür furosemid almamış.\n\n"
                    "Vitaller: KH 120, KB 180/100, SpO2 %85, SS 32. "
                    "Bilateral krepitanlar. JVB yükselmiş.\n\n"
                    "Tedavinizi açıklayın."
                ),
                "task_en": (
                    "1. Describe your immediate management steps\n"
                    "2. List medications with doses\n"
                    "3. Describe respiratory support\n"
                    "4. State investigations needed"
                ),
                "task_tr": (
                    "1. Acil tedavi adımlarınızı açıklayın\n"
                    "2. İlaçları dozlarıyla birlikte listeleyin\n"
                    "3. Solunum desteğini açıklayın\n"
                    "4. Gereken tetkikleri belirtin"
                ),
                "key_points": [
                    "Sit upright to reduce preload",
                    "Non-invasive ventilation (CPAP/BiPAP)",
                    "IV furosemide",
                    "IV nitroglycerin for afterload reduction",
                    "Monitor urine output",
                    "BNP, troponin, renal panel, chest X-ray",
                ],
                "checklist": [
                    {"item": "Positioned patient upright", "category": "Management"},
                    {"item": "Applied CPAP or BiPAP", "category": "Management"},
                    {"item": "Gave IV furosemide with dose", "category": "Management"},
                    {"item": "Started IV nitroglycerin", "category": "Management"},
                    {"item": "Ordered chest X-ray", "category": "Investigation"},
                    {"item": "Ordered BNP/NT-proBNP", "category": "Investigation"},
                    {"item": "Ordered troponin", "category": "Investigation"},
                    {"item": "Mentioned urinary catheter/output monitoring", "category": "Monitoring"},
                    {"item": "Identified precipitating factor", "category": "Assessment"},
                    {"item": "Mentioned echocardiography", "category": "Investigation"},
                ],
            },
            {
                "station_id": "osce_im_s4",
                "station_number": 4,
                "title_en": "Station 4 — Drug Overdose Management",
                "title_tr": "İstasyon 4 — İlaç Doz Aşımı Tedavisi",
                "time_limit_seconds": 480,
                "station_type": "management",
                "patient_scenario_en": (
                    "A 16-year-old girl ingested ~30 tablets of paracetamol 500mg "
                    "(~15g total) 2 hours ago. Currently asymptomatic. "
                    "4-hour paracetamol level: 210 mcg/mL — above treatment line.\n\n"
                    "Describe your complete management plan."
                ),
                "patient_scenario_tr": (
                    "16 yaşında kız, 2 saat önce ~30 adet 500mg parasetamol tableti "
                    "(~15g toplam) almış. Şu anda asemptomatik. "
                    "4. saat parasetamol düzeyi: 210 mcg/mL — tedavi çizgisinin üzerinde.\n\n"
                    "Tam tedavi planınızı açıklayın."
                ),
                "task_en": (
                    "1. Assess toxicity severity\n"
                    "2. Describe specific antidote and protocol\n"
                    "3. List monitoring requirements\n"
                    "4. Describe discharge planning"
                ),
                "task_tr": (
                    "1. Toksisite ciddiyetini değerlendirin\n"
                    "2. Spesifik antidot ve protokolü açıklayın\n"
                    "3. İzlem gereksinimlerini listeleyin\n"
                    "4. Taburculuk planını açıklayın"
                ),
                "key_points": [
                    "Toxic dose calculation (>150 mg/kg)",
                    "N-Acetylcysteine (NAC) protocol",
                    "Rumack-Matthew nomogram",
                    "Liver function monitoring",
                    "Psychiatric evaluation mandatory",
                    "Safety assessment before discharge",
                ],
                "checklist": [
                    {"item": "Calculated toxic dose correctly", "category": "Assessment"},
                    {"item": "Referenced Rumack-Matthew nomogram", "category": "Assessment"},
                    {"item": "Started NAC (N-Acetylcysteine)", "category": "Management"},
                    {"item": "Described NAC dosing protocol", "category": "Management"},
                    {"item": "Mentioned activated charcoal timing", "category": "Management"},
                    {"item": "Ordered baseline LFTs", "category": "Investigation"},
                    {"item": "Planned serial LFT monitoring", "category": "Monitoring"},
                    {"item": "Mentioned criteria to stop NAC", "category": "Management"},
                    {"item": "Mandatory psychiatric evaluation", "category": "Safety"},
                    {"item": "Safety assessment before discharge", "category": "Safety"},
                ],
            },
        ],
    },

    "osce_trauma": {
        "set_id": "osce_trauma",
        "title_en": "Trauma & Emergency Surgery OSCE",
        "title_tr": "Travma ve Acil Cerrahi OSCE",
        "description_en": "Four-station OSCE covering polytrauma assessment, hemorrhagic shock management, abdominal injury, and trauma team communication.",
        "description_tr": "Politravma değerlendirmesi, hemorajik şok yönetimi, batın yaralanması ve travma ekip iletişimini kapsayan dört istasyonlu OSCE.",
        "difficulty": "Advanced",
        "stations": [
            {
                "station_id": "osce_tr_s1",
                "station_number": 1,
                "title_en": "Station 1 — Primary Survey: Polytrauma",
                "title_tr": "İstasyon 1 — Birincil Değerlendirme: Politravma",
                "time_limit_seconds": 480,
                "station_type": "physical_exam",
                "patient_scenario_en": (
                    "An 8-year-old boy arrives by ambulance after being hit by a car. "
                    "Thrown approximately 5 meters. GCS: 12. C-spine collar in place. "
                    "Right abdominal abrasion and left thigh deformity visible.\n\n"
                    "Perform your primary survey (ABCDE approach)."
                ),
                "patient_scenario_tr": (
                    "8 yaşında erkek çocuk, araba çarpması sonrası ambulansla getirildi. "
                    "Yaklaşık 5 metre fırlatılmış. GKS: 12. Servikal boyunluk takılı. "
                    "Sağ karın abrazyonu ve sol uyluk deformitesi görülüyor.\n\n"
                    "Birincil değerlendirmenizi yapın (ABCDE yaklaşımı)."
                ),
                "task_en": (
                    "1. Describe your systematic ABCDE primary survey\n"
                    "2. State what you assess at each step\n"
                    "3. Identify immediate life threats\n"
                    "4. Describe your initial resuscitation"
                ),
                "task_tr": (
                    "1. Sistematik ABCDE birincil değerlendirmenizi açıklayın\n"
                    "2. Her adımda ne değerlendirdiğinizi belirtin\n"
                    "3. Acil yaşam tehditlerini tanımlayın\n"
                    "4. İlk resüsitasyonunuzu açıklayın"
                ),
                "key_points": [
                    "ATLS Primary Survey: A-B-C-D-E",
                    "Airway with C-spine protection",
                    "Bilateral chest assessment",
                    "Hemorrhage control and IV access",
                    "GCS reassessment and pupil check",
                    "Full exposure with temperature control",
                ],
                "checklist": [
                    {"item": "Airway assessment with C-spine protection", "category": "Airway"},
                    {"item": "Breathing: auscultation, inspection", "category": "Breathing"},
                    {"item": "Circulation: pulse, BP, capillary refill", "category": "Circulation"},
                    {"item": "Two large-bore IV lines", "category": "Circulation"},
                    {"item": "Disability: GCS, pupils", "category": "Disability"},
                    {"item": "Exposure: fully undressed", "category": "Exposure"},
                    {"item": "Temperature control mentioned", "category": "Exposure"},
                    {"item": "Identified hemorrhagic shock risk", "category": "Assessment"},
                    {"item": "Blood type and crossmatch ordered", "category": "Investigation"},
                    {"item": "Systematic approach followed", "category": "Process"},
                ],
            },
            {
                "station_id": "osce_tr_s2",
                "station_number": 2,
                "title_en": "Station 2 — Hemorrhagic Shock Management",
                "title_tr": "İstasyon 2 — Hemorajik Şok Yönetimi",
                "time_limit_seconds": 480,
                "station_type": "management",
                "patient_scenario_en": (
                    "Primary survey completed. HR 140, BP 85/50, capillary refill 4 sec. "
                    "Skin pale and cool. Left femur fracture suspected. "
                    "Abdomen tender with guarding.\n\n"
                    "The child is in hemorrhagic shock. Manage this patient."
                ),
                "patient_scenario_tr": (
                    "Birincil değerlendirme tamamlandı. KH 140, KB 85/50, kapiller dolum 4 sn. "
                    "Deri soluk ve soğuk. Sol femur kırığı şüphesi. "
                    "Karın hassas, defans mevcut.\n\n"
                    "Çocuk hemorajik şokta. Bu hastayı yönetin."
                ),
                "task_en": (
                    "1. Classify the shock\n"
                    "2. Describe fluid resuscitation strategy\n"
                    "3. Order appropriate imaging\n"
                    "4. Describe criteria for surgical intervention"
                ),
                "task_tr": (
                    "1. Şoku sınıflandırın\n"
                    "2. Sıvı resüsitasyon stratejisini açıklayın\n"
                    "3. Uygun görüntülemeyi isteyin\n"
                    "4. Cerrahi müdahale kriterlerini açıklayın"
                ),
                "key_points": [
                    "Class III hemorrhagic shock",
                    "Crystalloid bolus 20 mL/kg",
                    "Blood transfusion preparation",
                    "FAST exam",
                    "Femur splinting",
                    "Surgical consultation",
                ],
                "checklist": [
                    {"item": "Classified shock severity", "category": "Assessment"},
                    {"item": "Crystalloid bolus 20 mL/kg", "category": "Management"},
                    {"item": "Reassess after each bolus", "category": "Monitoring"},
                    {"item": "Ordered blood crossmatch/transfusion", "category": "Management"},
                    {"item": "FAST exam ordered", "category": "Investigation"},
                    {"item": "Femur fracture splinted", "category": "Management"},
                    {"item": "Surgical consultation requested", "category": "Management"},
                    {"item": "Chest and pelvic X-ray", "category": "Investigation"},
                    {"item": "Mentioned TXA consideration", "category": "Management"},
                    {"item": "Warm fluids to prevent hypothermia", "category": "Management"},
                ],
            },
            {
                "station_id": "osce_tr_s3",
                "station_number": 3,
                "title_en": "Station 3 — FAST Positive: Decision Making",
                "title_tr": "İstasyon 3 — FAST Pozitif: Karar Verme",
                "time_limit_seconds": 480,
                "station_type": "diagnosis",
                "patient_scenario_en": (
                    "After initial resuscitation: HR 130, BP 90/55. Slight improvement. "
                    "FAST: positive — free fluid in Morrison's pouch and pelvis. "
                    "Hemoglobin 8.2 g/dL. Second bolus running.\n\n"
                    "Decide: operative vs. non-operative management?"
                ),
                "patient_scenario_tr": (
                    "İlk resüsitasyon sonrası: KH 130, KB 90/55. Hafif düzelme. "
                    "FAST: pozitif — Morrison poşu ve pelviste serbest sıvı. "
                    "Hemoglobin 8.2 g/dL. İkinci bolus veriliyor.\n\n"
                    "Karar verin: ameliyat mı konservatif tedavi mi?"
                ),
                "task_en": (
                    "1. Interpret FAST results\n"
                    "2. Decide on operative vs non-operative approach\n"
                    "3. Justify your decision\n"
                    "4. Describe your next steps"
                ),
                "task_tr": (
                    "1. FAST sonuçlarını yorumlayın\n"
                    "2. Ameliyat mı konservatif yaklaşım mı karar verin\n"
                    "3. Kararınızı gerekçelendirin\n"
                    "4. Sonraki adımlarınızı açıklayın"
                ),
                "key_points": [
                    "FAST positive interpretation",
                    "Massive transfusion protocol",
                    "CT if hemodynamically stable enough",
                    "Direct to OR if unstable",
                    "Avoid hypothermia",
                    "Damage control resuscitation",
                ],
                "checklist": [
                    {"item": "Interpreted FAST correctly", "category": "Assessment"},
                    {"item": "Activated massive transfusion", "category": "Management"},
                    {"item": "Packed RBC transfusion ordered", "category": "Management"},
                    {"item": "Assessed stability for CT vs OR", "category": "Decision"},
                    {"item": "Clear decision with justification", "category": "Decision"},
                    {"item": "Mentioned damage control principles", "category": "Management"},
                    {"item": "Hypothermia prevention", "category": "Management"},
                    {"item": "Mentioned coagulopathy risk", "category": "Assessment"},
                    {"item": "Surgical team communication", "category": "Communication"},
                    {"item": "Family notification mentioned", "category": "Communication"},
                ],
            },
            {
                "station_id": "osce_tr_s4",
                "station_number": 4,
                "title_en": "Station 4 — Post-operative Care & Communication",
                "title_tr": "İstasyon 4 — Post-operatif Bakım ve İletişim",
                "time_limit_seconds": 480,
                "station_type": "communication",
                "patient_scenario_en": (
                    "Splenectomy performed. Patient stable in PICU. "
                    "Femur fracture externally fixated. Parents are anxious.\n\n"
                    "Explain the situation to the parents and describe post-operative care."
                ),
                "patient_scenario_tr": (
                    "Splenektomi yapıldı. Hasta ÇÇYBÜ'de stabil. "
                    "Femur kırığı eksternal fiksatörle tedavi edildi. Ebeveynler endişeli.\n\n"
                    "Durumu ebeveynlere açıklayın ve post-operatif bakımı tanımlayın."
                ),
                "task_en": (
                    "1. Explain what happened and the surgeries performed\n"
                    "2. Describe post-splenectomy care and vaccinations\n"
                    "3. Discuss long-term follow-up\n"
                    "4. Address parents' concerns"
                ),
                "task_tr": (
                    "1. Ne olduğunu ve yapılan ameliyatları açıklayın\n"
                    "2. Splenektomi sonrası bakım ve aşıları tanımlayın\n"
                    "3. Uzun vadeli takibi tartışın\n"
                    "4. Ebeveynlerin endişelerini ele alın"
                ),
                "key_points": [
                    "Clear explanation of surgeries",
                    "Post-splenectomy vaccinations",
                    "Lifelong penicillin prophylaxis",
                    "OPSI risk education",
                    "Orthopedic follow-up",
                    "Psychological support",
                ],
                "checklist": [
                    {"item": "Explained situation clearly", "category": "Communication"},
                    {"item": "Described splenectomy necessity", "category": "Communication"},
                    {"item": "Mentioned post-splenectomy vaccines", "category": "Management"},
                    {"item": "Mentioned lifelong antibiotic prophylaxis", "category": "Management"},
                    {"item": "Explained OPSI risk", "category": "Education"},
                    {"item": "Discussed orthopedic follow-up", "category": "Management"},
                    {"item": "Mentioned psychological support", "category": "Management"},
                    {"item": "Used empathetic communication", "category": "Communication"},
                    {"item": "Addressed questions and concerns", "category": "Communication"},
                    {"item": "Provided written discharge information", "category": "Education"},
                ],
            },
        ],
    },
}


def get_osce_set(set_id: str) -> dict | None:
    """Return an OSCE set by its ID."""
    return OSCE_SETS.get(set_id)


def get_osce_station(set_id: str, station_number: int) -> dict | None:
    """Return a specific station from an OSCE set."""
    osce_set = OSCE_SETS.get(set_id)
    if not osce_set:
        return None
    return next(
        (s for s in osce_set["stations"] if s["station_number"] == station_number),
        None,
    )


def get_station_content(station: dict, language: str = "en") -> dict:
    """Return station content localized to the given language."""
    lang = language if language in ("en", "tr") else "en"
    return {
        "station_id": station["station_id"],
        "station_number": station["station_number"],
        "title": station.get(f"title_{lang}") or station.get("title_en", ""),
        "time_limit_seconds": station.get("time_limit_seconds", 480),
        "station_type": station["station_type"],
        "patient_scenario": station.get(f"patient_scenario_{lang}") or station.get("patient_scenario_en", ""),
        "task": station.get(f"task_{lang}") or station.get("task_en", ""),
    }


def list_osce_sets(language: str = "en") -> list[dict]:
    """Return a summary list of all available OSCE sets."""
    lang = language if language in ("en", "tr") else "en"
    result = []
    for s in OSCE_SETS.values():
        result.append({
            "set_id": s["set_id"],
            "title": s.get(f"title_{lang}") or s.get("title_en", ""),
            "description": s.get(f"description_{lang}") or s.get("description_en", ""),
            "difficulty": s["difficulty"],
            "total_stations": len(s["stations"]),
        })
    return result
