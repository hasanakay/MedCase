"""
Extra clinical cases — bilingual (EN/TR) with progressive step structure.
Added for F2.3: Cardiology, Trauma, Intoxication, Respiratory Failure topics.
"""

EXTRA_CASES = {

    # ═══════════════════════════════════════════════════════════════════════════
    # CASE 4 — Acute Myocardial Infarction (AMI)
    # ═══════════════════════════════════════════════════════════════════════════
    "cardio_ami_001": {
        "case_id": "cardio_ami_001",
        "case_title_en": "Acute Myocardial Infarction",
        "case_title_tr": "Akut Miyokard İnfarktüsü",
        "case_title": "Acute Myocardial Infarction",
        "topic": "Cardiology",
        "difficulty": "Advanced",
        "learning_goals": [
            "STEMI recognition", "Chest pain assessment", "12-lead ECG interpretation",
            "Aspirin and antiplatelet therapy", "Reperfusion strategy",
            "Cardiac biomarkers", "Complication recognition",
        ],
        "steps": [
            {
                "step": 1,
                "scenario_update_en": (
                    "A 58-year-old male presents to the emergency department with crushing "
                    "substernal chest pain radiating to the left arm for the past 45 minutes. "
                    "He is diaphoretic, pale, and anxious. He has a history of hypertension "
                    "and smoking (30 pack-years). He took sublingual nitroglycerin at home "
                    "with no relief."
                ),
                "scenario_update_tr": (
                    "58 yaşında erkek hasta, 45 dakikadır sol kola yayılan şiddetli "
                    "substernal göğüs ağrısı ile acile başvurdu. Terleme, solukluk ve "
                    "anksiyete mevcut. Hipertansiyon ve sigara öyküsü (30 paket-yıl) var. "
                    "Evde dilaltı nitrogliserin almış ancak rahatlama olmamış."
                ),
                "question_en": (
                    "What is your immediate approach? "
                    "What assessments and interventions do you prioritize?"
                ),
                "question_tr": (
                    "Acil yaklaşımınız nedir? "
                    "Hangi değerlendirme ve müdahalelere öncelik verirsiniz?"
                ),
                "key_points": [
                    "ABC assessment",
                    "Vital signs",
                    "12-lead ECG within 10 minutes",
                    "IV access",
                    "Cardiac monitoring",
                    "Aspirin 300 mg chewable immediately",
                ],
            },
            {
                "step": 2,
                "scenario_update_en": (
                    "Vitals: HR 96, BP 150/95 mmHg, SpO2 96%, RR 22. "
                    "12-lead ECG shows: ST elevation in leads II, III, aVF (>2mm). "
                    "Reciprocal ST depression in I, aVL. "
                    "Aspirin given. IV access secured. Morphine considered for pain."
                ),
                "scenario_update_tr": (
                    "Vitaller: KH 96, KB 150/95 mmHg, SpO2 %96, SS 22. "
                    "12 derivasyonlu EKG: II, III, aVF'de ST elevasyonu (>2mm). "
                    "I, aVL'de resiprokal ST depresyonu. "
                    "Aspirin verildi. IV yol açıldı. Ağrı için morfin düşünülüyor."
                ),
                "question_en": (
                    "What is your ECG interpretation and diagnosis? "
                    "What is your immediate management plan?"
                ),
                "question_tr": (
                    "EKG yorumunuz ve tanınız nedir? "
                    "Acil tedavi planınız nedir?"
                ),
                "key_points": [
                    "Diagnosis: Inferior STEMI",
                    "Activate cardiac catheterization lab for primary PCI",
                    "Dual antiplatelet: add P2Y12 inhibitor (clopidogrel/ticagrelor)",
                    "Anticoagulation (heparin)",
                    "Morphine for pain relief if needed",
                    "Check right-sided ECG (V4R) to rule out RV infarction",
                ],
            },
            {
                "step": 3,
                "scenario_update_en": (
                    "Cath lab activated. Door-to-balloon target: <90 minutes. "
                    "Right-sided ECG shows ST elevation in V4R — right ventricular "
                    "involvement confirmed. Patient suddenly becomes hypotensive: "
                    "BP 80/50 mmHg, HR 110. Skin is cold and clammy."
                ),
                "scenario_update_tr": (
                    "Kateterizasyon laboratuvarı aktive edildi. Kapı-balon hedefi: <90 dakika. "
                    "Sağ taraflı EKG V4R'de ST elevasyonu gösteriyor — sağ ventrikül "
                    "tutulumu doğrulandı. Hasta aniden hipotansif oluyor: "
                    "KB 80/50 mmHg, KH 110. Deri soğuk ve nemli."
                ),
                "question_en": (
                    "The patient is now hypotensive with confirmed RV infarction. "
                    "How do you manage this complication? What should you avoid?"
                ),
                "question_tr": (
                    "Hasta sağ ventrikül infarktüsü ile birlikte hipotansif. "
                    "Bu komplikasyonu nasıl yönetirsiniz? Nelerden kaçınmalısınız?"
                ),
                "key_points": [
                    "IV fluid bolus (normal saline) for RV infarction",
                    "AVOID nitrates (worsen hypotension in RV infarction)",
                    "AVOID morphine excess (vasodilatory effect)",
                    "Consider inotropic support (dobutamine) if fluids fail",
                    "Urgent PCI remains priority",
                ],
            },
            {
                "step": 4,
                "scenario_update_en": (
                    "IV fluids improved BP to 100/65 mmHg. Patient taken to cath lab. "
                    "PCI performed: right coronary artery 100% occlusion, stent placed. "
                    "Post-PCI: TIMI 3 flow restored. Patient in CCU. "
                    "Troponin I: 15 ng/mL (markedly elevated). CK-MB: 120 U/L."
                ),
                "scenario_update_tr": (
                    "IV sıvılarla KB 100/65 mmHg'ye yükseldi. Hasta kateter laboratuvarına alındı. "
                    "PKG yapıldı: sağ koroner arter %100 tıkalı, stent yerleştirildi. "
                    "PKG sonrası: TIMI 3 akım sağlandı. Hasta KKÜ'de. "
                    "Troponin I: 15 ng/mL (belirgin yüksek). CK-MB: 120 U/L."
                ),
                "question_en": (
                    "PCI was successful. What are your post-PCI orders? "
                    "What medications and monitoring do you continue? "
                    "What complications do you watch for?"
                ),
                "question_tr": (
                    "PKG başarılı oldu. PKG sonrası tedavi planınız nedir? "
                    "Hangi ilaçlar ve izlem devam eder? "
                    "Hangi komplikasyonları takip edersiniz?"
                ),
                "key_points": [
                    "Dual antiplatelet therapy (DAPT) — continue for 12 months",
                    "Beta-blocker (metoprolol) when hemodynamically stable",
                    "ACE inhibitor / ARB within 24 hours",
                    "High-dose statin (atorvastatin 80 mg)",
                    "Continuous cardiac monitoring for arrhythmias",
                    "Echocardiography to assess LV function",
                    "Risk factor modification counseling",
                ],
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # CASE 5 — Acute Heart Failure / Pulmonary Edema
    # ═══════════════════════════════════════════════════════════════════════════
    "cardio_hf_001": {
        "case_id": "cardio_hf_001",
        "case_title_en": "Acute Heart Failure",
        "case_title_tr": "Akut Kalp Yetmezliği",
        "case_title": "Acute Heart Failure",
        "topic": "Cardiology",
        "difficulty": "Intermediate",
        "learning_goals": [
            "Recognize acute decompensated heart failure",
            "Pulmonary edema management", "Diuretic therapy",
            "Non-invasive ventilation", "Underlying cause identification",
        ],
        "steps": [
            {
                "step": 1,
                "scenario_update_en": (
                    "A 72-year-old female with known congestive heart failure presents "
                    "with acute worsening dyspnea over the past 6 hours. She cannot lie flat "
                    "(orthopnea), is using accessory muscles, and has pink frothy sputum. "
                    "She ran out of her furosemide 3 days ago."
                ),
                "scenario_update_tr": (
                    "72 yaşında bilinen konjestif kalp yetmezliği olan kadın hasta, "
                    "son 6 saatte kötüleşen nefes darlığı ile başvurdu. Düz yatamıyor "
                    "(ortopne), yardımcı solunum kaslarını kullanıyor ve pembe köpüklü "
                    "balgam var. 3 gündür furosemid ilacını almamış."
                ),
                "question_en": (
                    "What is your immediate assessment and first-line management?"
                ),
                "question_tr": (
                    "Acil değerlendirmeniz ve ilk basamak tedaviniz nedir?"
                ),
                "key_points": [
                    "ABC assessment",
                    "Sit patient upright (reduces preload)",
                    "High-flow oxygen / non-invasive ventilation (CPAP/BiPAP)",
                    "IV furosemide (loop diuretic) as first-line",
                    "IV access and cardiac monitoring",
                    "12-lead ECG",
                ],
            },
            {
                "step": 2,
                "scenario_update_en": (
                    "Patient seated upright. CPAP applied at 10 cmH2O. "
                    "Vitals: HR 120, BP 180/100 mmHg, SpO2 85% on CPAP, RR 32. "
                    "Bilateral crackles to mid-lung fields. JVP elevated. "
                    "Peripheral edema 3+. ECG: sinus tachycardia, LVH pattern."
                ),
                "scenario_update_tr": (
                    "Hasta oturur pozisyona alındı. CPAP 10 cmH2O ile uygulandı. "
                    "Vitaller: KH 120, KB 180/100 mmHg, SpO2 %85 CPAP ile, SS 32. "
                    "Bilateral krepitanlar orta akciğer alanlarına kadar. JVB yükselmiş. "
                    "Periferik ödem 3+. EKG: sinüs taşikardisi, SVH paterni."
                ),
                "question_en": (
                    "SpO2 is still low. BP is very high. "
                    "What additional treatments do you initiate?"
                ),
                "question_tr": (
                    "SpO2 hâlâ düşük. KB çok yüksek. "
                    "Hangi ek tedavileri başlatırsınız?"
                ),
                "key_points": [
                    "IV furosemide bolus (40-80 mg)",
                    "IV nitroglycerin infusion for afterload reduction (BP high)",
                    "Titrate CPAP/BiPAP settings",
                    "Strict fluid restriction",
                    "Insert urinary catheter to monitor output",
                    "Order BNP/NT-proBNP, troponin, renal panel, chest X-ray",
                ],
            },
            {
                "step": 3,
                "scenario_update_en": (
                    "After furosemide and nitroglycerin: BP 140/85, SpO2 92%, "
                    "urine output 200 mL in first hour. Chest X-ray confirms "
                    "bilateral pulmonary edema with cardiomegaly. "
                    "BNP: 2400 pg/mL (markedly elevated). Troponin mildly elevated. "
                    "Creatinine: 1.8 mg/dL (baseline 1.2)."
                ),
                "scenario_update_tr": (
                    "Furosemid ve nitrogliserin sonrası: KB 140/85, SpO2 %92, "
                    "ilk saatte idrar çıkışı 200 mL. Akciğer grafisi bilateral "
                    "pulmoner ödem ve kardiyomegaliyi doğruluyor. "
                    "BNP: 2400 pg/mL (belirgin yüksek). Troponin hafif yüksek. "
                    "Kreatinin: 1.8 mg/dL (bazal 1.2)."
                ),
                "question_en": (
                    "Patient is improving but not resolved. "
                    "What is the underlying cause? What additional workup and treatment?"
                ),
                "question_tr": (
                    "Hasta düzeliyor ama tamamen çözülmedi. "
                    "Altta yatan neden nedir? Ek tetkik ve tedaviniz?"
                ),
                "key_points": [
                    "Echocardiography to assess EF and valvular function",
                    "Identify precipitating factor (medication non-compliance)",
                    "Continue diuresis with monitoring of renal function",
                    "Consider ACE inhibitor once BP stabilized",
                    "Cardiology consultation",
                    "Daily weight monitoring",
                ],
            },
            {
                "step": 4,
                "scenario_update_en": (
                    "Day 2: Patient much improved. Off CPAP, on nasal cannula 2L. "
                    "SpO2 96%. Echo: EF 30%, moderate mitral regurgitation, "
                    "dilated LV. Weight down 3 kg from admission. "
                    "Creatinine improving (1.5). Patient asking about going home."
                ),
                "scenario_update_tr": (
                    "2. gün: Hasta belirgin düzelme gösteriyor. CPAP çıkarıldı, "
                    "nazal kanül 2L ile SpO2 %96. Eko: EF %30, orta derece mitral "
                    "yetmezlik, dilate sol ventrikül. Kilo yatıştan 3 kg düşmüş. "
                    "Kreatinin düzeliyor (1.5). Hasta eve gitmek istiyor."
                ),
                "question_en": (
                    "What is your discharge plan? "
                    "What medications do you prescribe and what education do you provide?"
                ),
                "question_tr": (
                    "Taburculuk planınız nedir? "
                    "Hangi ilaçları reçete eder ve hangi eğitimi verirsiniz?"
                ),
                "key_points": [
                    "Optimize oral diuretic (furosemide with dose adjustment)",
                    "ACE inhibitor or ARB",
                    "Beta-blocker (carvedilol or bisoprolol — start low, titrate)",
                    "Daily weight monitoring education",
                    "Sodium and fluid restriction education",
                    "Medication adherence counseling",
                    "Follow-up with cardiology in 1-2 weeks",
                ],
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # CASE 6 — Pediatric Polytrauma
    # ═══════════════════════════════════════════════════════════════════════════
    "trauma_poly_001": {
        "case_id": "trauma_poly_001",
        "case_title_en": "Pediatric Polytrauma",
        "case_title_tr": "Pediatrik Politravma",
        "case_title": "Pediatric Polytrauma",
        "topic": "Trauma / Emergency Surgery",
        "difficulty": "Intermediate",
        "learning_goals": [
            "ATLS primary survey", "Airway management", "Hemorrhagic shock",
            "FAST exam", "C-spine precautions", "Damage control resuscitation",
        ],
        "steps": [
            {
                "step": 1,
                "scenario_update_en": (
                    "An 8-year-old boy is brought by ambulance after being hit by a car "
                    "while crossing the street. He was thrown approximately 5 meters. "
                    "GCS at scene: 12 (E3V4M5). C-spine collar applied by EMS. "
                    "He is crying but confused. Visible abrasion on the right side of his abdomen "
                    "and deformity of his left thigh."
                ),
                "scenario_update_tr": (
                    "8 yaşında erkek çocuk, yoldan geçerken araba çarpması sonrası "
                    "ambulansla getirildi. Yaklaşık 5 metre fırlatılmış. "
                    "Olay yerinde GKS: 12 (G3S4M5). ATT tarafından servikal boyunluk takıldı. "
                    "Ağlıyor ama konfüze. Sağ karın bölgesinde abrazyon "
                    "ve sol uylukta deformite görülüyor."
                ),
                "question_en": (
                    "The patient arrives in the trauma bay. "
                    "What is your systematic primary survey approach?"
                ),
                "question_tr": (
                    "Hasta travma odasına getirildi. "
                    "Sistematik birincil değerlendirme yaklaşımınız nedir?"
                ),
                "key_points": [
                    "ATLS Primary Survey: A-B-C-D-E",
                    "Airway with C-spine protection",
                    "Breathing: bilateral chest auscultation, look for pneumothorax",
                    "Circulation: hemorrhage control, two large-bore IVs",
                    "Disability: GCS reassessment, pupil check",
                    "Exposure: full undress with temperature control",
                ],
            },
            {
                "step": 2,
                "scenario_update_en": (
                    "Primary survey: Airway patent with collar in place. "
                    "Breathing: bilateral air entry, no pneumothorax. RR 28. "
                    "Circulation: HR 140 (tachycardic), BP 85/50, weak peripheral pulses, "
                    "capillary refill 4 seconds. Skin pale and cool. "
                    "Left thigh is swollen and shortened — suspected femur fracture. "
                    "Abdomen tender on right side with guarding."
                ),
                "scenario_update_tr": (
                    "Birincil değerlendirme: Hava yolu açık, boyunluk yerinde. "
                    "Solunum: bilateral hava girişi var, pnömotoraks yok. SS 28. "
                    "Dolaşım: KH 140 (taşikardik), KB 85/50, periferik nabızlar zayıf, "
                    "kapiller dolum 4 saniye. Deri soluk ve soğuk. "
                    "Sol uyluk şişkin ve kısalmış — femur kırığı şüphesi. "
                    "Karın sağ tarafta hassas ve defansı var."
                ),
                "question_en": (
                    "The child is showing signs of hemorrhagic shock. "
                    "What is your fluid resuscitation strategy and what imaging do you order?"
                ),
                "question_tr": (
                    "Çocukta hemorajik şok bulguları var. "
                    "Sıvı resüsitasyon stratejiniz ve isteyeceğiniz görüntüleme nedir?"
                ),
                "key_points": [
                    "Classify hemorrhagic shock (Class III based on vitals)",
                    "Isotonic crystalloid bolus 20 mL/kg (reassess after each bolus)",
                    "Crossmatch blood — prepare for transfusion",
                    "FAST (Focused Assessment with Sonography in Trauma)",
                    "Femur fracture splinting (traction splint) to reduce bleeding",
                    "Pelvic X-ray and chest X-ray",
                ],
            },
            {
                "step": 3,
                "scenario_update_en": (
                    "20 mL/kg NS bolus given. HR 130, BP 90/55. Slight improvement. "
                    "FAST exam: free fluid in Morrison's pouch and pelvis — POSITIVE. "
                    "Chest X-ray: no pneumothorax or hemothorax. "
                    "Femur splinted. Second bolus running. Hemoglobin: 8.2 g/dL."
                ),
                "scenario_update_tr": (
                    "20 mL/kg SF bolus verildi. KH 130, KB 90/55. Hafif düzelme. "
                    "FAST: Morrison poşunda ve pelviste serbest sıvı — POZİTİF. "
                    "Akciğer grafisi: pnömotoraks veya hemotoraks yok. "
                    "Femur atele alındı. İkinci bolus veriliyor. Hemoglobin: 8.2 g/dL."
                ),
                "question_en": (
                    "FAST is positive for intra-abdominal free fluid. "
                    "Patient is not fully responding to fluids. What are your next steps?"
                ),
                "question_tr": (
                    "FAST karın içi serbest sıvı için pozitif. "
                    "Hasta sıvılara tam yanıt vermiyor. Sonraki adımlarınız nedir?"
                ),
                "key_points": [
                    "Activate massive transfusion protocol",
                    "Packed RBCs transfusion (10-15 mL/kg)",
                    "Urgent surgical consultation",
                    "CT abdomen if patient is hemodynamically stable enough",
                    "If unstable — direct to OR for exploratory laparotomy",
                    "Avoid hypothermia (warm fluids, blankets)",
                    "Tranexamic acid (TXA) consideration",
                ],
            },
            {
                "step": 4,
                "scenario_update_en": (
                    "Blood transfusion started. Surgeon consulted. "
                    "CT abdomen (patient briefly stabilized): Grade III splenic laceration "
                    "with active extravasation. No other solid organ injury. "
                    "Patient taken to OR for splenectomy. Femur fracture managed with "
                    "external fixation. Post-op stable in PICU."
                ),
                "scenario_update_tr": (
                    "Kan transfüzyonu başlatıldı. Cerrah konsülte edildi. "
                    "Batın BT (hasta kısa süreliğine stabilize oldu): Grade III dalak "
                    "laserasyonu, aktif ekstravazasyon. Diğer solid organ hasarı yok. "
                    "Hasta splenektomi için ameliyathaneye alındı. Femur kırığı "
                    "eksternal fiksatörle tedavi edildi. Post-op ÇÇYBÜ'de stabil."
                ),
                "question_en": (
                    "Post-operative management: What monitoring, medications, "
                    "and long-term considerations does this child need after splenectomy?"
                ),
                "question_tr": (
                    "Post-operatif yönetim: Splenektomi sonrası bu çocuğun hangi izlem, "
                    "ilaç ve uzun vadeli takip ihtiyaçları vardır?"
                ),
                "key_points": [
                    "Post-splenectomy vaccination (pneumococcal, meningococcal, H. influenzae)",
                    "Lifelong penicillin prophylaxis (or amoxicillin)",
                    "Education about overwhelming post-splenectomy infection (OPSI)",
                    "DVT prophylaxis",
                    "Orthopedic follow-up for femur fracture",
                    "Psychological support for trauma",
                ],
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # CASE 7 — Blunt Abdominal Trauma
    # ═══════════════════════════════════════════════════════════════════════════
    "trauma_abd_001": {
        "case_id": "trauma_abd_001",
        "case_title_en": "Blunt Abdominal Trauma",
        "case_title_tr": "Künt Batın Travması",
        "case_title": "Blunt Abdominal Trauma",
        "topic": "Trauma / Emergency Surgery",
        "difficulty": "Advanced",
        "learning_goals": [
            "Blunt abdominal trauma assessment", "FAST exam", "CT grading",
            "Non-operative management", "Surgical decision making",
            "Hollow viscus injury recognition",
        ],
        "steps": [
            {
                "step": 1,
                "scenario_update_en": (
                    "A 14-year-old boy fell from a bicycle at high speed and hit his "
                    "abdomen on the handlebar. He presents with severe abdominal pain, "
                    "especially in the left upper quadrant. He vomited once. "
                    "No loss of consciousness. No other visible injuries."
                ),
                "scenario_update_tr": (
                    "14 yaşında erkek çocuk, bisikletten yüksek hızda düşerek karnını "
                    "gidon koluna çarpmış. Şiddetli karın ağrısı, özellikle sol üst "
                    "kadranda mevcut. Bir kez kusmuş. Bilinç kaybı yok. "
                    "Diğer görünür yaralanma yok."
                ),
                "question_en": (
                    "What is your initial assessment and management approach?"
                ),
                "question_tr": (
                    "İlk değerlendirme ve tedavi yaklaşımınız nedir?"
                ),
                "key_points": [
                    "ATLS Primary Survey (A-B-C-D-E)",
                    "Focused abdominal examination",
                    "Two large-bore IV lines",
                    "Blood type and crossmatch",
                    "FAST exam at bedside",
                    "Serial vital signs monitoring",
                ],
            },
            {
                "step": 2,
                "scenario_update_en": (
                    "Vitals: HR 105, BP 110/70, SpO2 99%, RR 20. "
                    "Abdomen: LUQ tenderness with voluntary guarding. "
                    "Kehr's sign positive (left shoulder pain on palpation of LUQ). "
                    "FAST: small amount of free fluid in the splenorenal recess. "
                    "Hemoglobin: 11.2 g/dL."
                ),
                "scenario_update_tr": (
                    "Vitaller: KH 105, KB 110/70, SpO2 %99, SS 20. "
                    "Karın: Sol üst kadranda hassasiyet, istemli defans. "
                    "Kehr belirtisi pozitif (sol üst kadran palpasyonunda sol omuz ağrısı). "
                    "FAST: spleno-renal alanda az miktarda serbest sıvı. "
                    "Hemoglobin: 11.2 g/dL."
                ),
                "question_en": (
                    "FAST is positive with Kehr's sign. The patient is hemodynamically stable. "
                    "What organ is likely injured? What is your next diagnostic step?"
                ),
                "question_tr": (
                    "FAST pozitif ve Kehr belirtisi var. Hasta hemodinamik olarak stabil. "
                    "Hangi organ yaralanmış olabilir? Sonraki tanısal adımınız nedir?"
                ),
                "key_points": [
                    "Suspected splenic injury (Kehr's sign = diaphragmatic irritation)",
                    "CT abdomen with IV contrast (gold standard for stable patients)",
                    "Serial hemoglobin monitoring",
                    "Keep patient NPO",
                    "Surgical consultation",
                ],
            },
            {
                "step": 3,
                "scenario_update_en": (
                    "CT abdomen: Grade II splenic laceration with small perisplenic "
                    "hematoma. No active contrast extravasation. No other organ injury. "
                    "Free fluid limited to left upper quadrant. "
                    "Patient remains hemodynamically stable. HR 95, BP 115/75."
                ),
                "scenario_update_tr": (
                    "Batın BT: Grade II dalak laserasyonu, küçük perisplenik hematom. "
                    "Aktif kontrast ekstravazasyonu yok. Diğer organ hasarı yok. "
                    "Serbest sıvı sol üst kadranla sınırlı. "
                    "Hasta hemodinamik olarak stabil. KH 95, KB 115/75."
                ),
                "question_en": (
                    "Grade II splenic laceration in a stable patient. "
                    "What is your management approach? Operative or non-operative?"
                ),
                "question_tr": (
                    "Stabil hastada Grade II dalak laserasyonu. "
                    "Tedavi yaklaşımınız nedir? Ameliyat mı konservatif tedavi mi?"
                ),
                "key_points": [
                    "Non-operative management (NOM) for Grade I-III stable patients",
                    "Bed rest and close monitoring in PICU",
                    "Serial hemoglobin every 6 hours",
                    "Serial abdominal examinations",
                    "Strict NPO initially",
                    "Criteria for surgery: hemodynamic instability despite resuscitation",
                ],
            },
            {
                "step": 4,
                "scenario_update_en": (
                    "Day 3 of NOM: Patient improving. Hemoglobin stable at 10.8 g/dL. "
                    "Tolerating clear liquids. Mild tenderness remains. "
                    "Parents asking about activity restrictions and follow-up."
                ),
                "scenario_update_tr": (
                    "Konservatif tedavinin 3. günü: Hasta düzeliyor. Hemoglobin 10.8 g/dL ile stabil. "
                    "Berrak sıvıları tolere ediyor. Hafif hassasiyet devam ediyor. "
                    "Ebeveynler aktivite kısıtlamaları ve takip hakkında soruyor."
                ),
                "question_en": (
                    "What are your discharge criteria and activity restriction guidelines "
                    "for a child with a Grade II splenic injury managed non-operatively?"
                ),
                "question_tr": (
                    "Konservatif tedavi edilen Grade II dalak yaralanmalı çocuk için "
                    "taburculuk kriterleri ve aktivite kısıtlama rehberiniz nedir?"
                ),
                "key_points": [
                    "No contact sports for 2-3 months (based on grade)",
                    "Follow-up imaging (ultrasound) at 4-6 weeks",
                    "Return precautions: worsening pain, dizziness, pallor",
                    "Gradual return to activity",
                    "No splenectomy = no need for vaccination changes",
                ],
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # CASE 8 — Paracetamol (Acetaminophen) Intoxication
    # ═══════════════════════════════════════════════════════════════════════════
    "intox_paracetamol_001": {
        "case_id": "intox_paracetamol_001",
        "case_title_en": "Paracetamol Overdose",
        "case_title_tr": "Parasetamol İntoksikasyonu",
        "case_title": "Paracetamol Overdose",
        "topic": "Intoxication / Poisoning",
        "difficulty": "Intermediate",
        "learning_goals": [
            "Toxic dose calculation", "Rumack-Matthew nomogram",
            "N-Acetylcysteine protocol", "Liver function monitoring",
            "Psychiatric evaluation", "Activated charcoal timing",
        ],
        "steps": [
            {
                "step": 1,
                "scenario_update_en": (
                    "A 16-year-old girl is brought to the ED by her mother. "
                    "She admits to ingesting approximately 30 tablets of 500 mg paracetamol "
                    "(~15 grams total) about 2 hours ago after an argument with her boyfriend. "
                    "She is currently asymptomatic — no nausea, no abdominal pain. "
                    "She regrets the action and is tearful."
                ),
                "scenario_update_tr": (
                    "16 yaşında kız, annesi tarafından acile getirildi. "
                    "Erkek arkadaşıyla tartıştıktan sonra yaklaşık 2 saat önce "
                    "30 adet 500 mg parasetamol tableti (~15 gram toplam) aldığını kabul ediyor. "
                    "Şu anda asemptomatik — bulantı yok, karın ağrısı yok. "
                    "Yaptığından pişman ve ağlıyor."
                ),
                "question_en": (
                    "How do you assess the severity of this ingestion? "
                    "What are your immediate management priorities?"
                ),
                "question_tr": (
                    "Bu alımın ciddiyetini nasıl değerlendirirsiniz? "
                    "Acil tedavi öncelikleriniz nelerdir?"
                ),
                "key_points": [
                    "Calculate toxic dose: 15g / patient weight — likely >150 mg/kg (toxic)",
                    "Activated charcoal if within 1-2 hours of ingestion",
                    "Draw serum paracetamol level (4-hour level for nomogram)",
                    "Baseline liver function tests (AST, ALT, INR)",
                    "Renal function and electrolytes",
                    "Do NOT wait for symptoms — paracetamol toxicity is initially asymptomatic",
                ],
            },
            {
                "step": 2,
                "scenario_update_en": (
                    "Activated charcoal given (within 2-hour window). "
                    "4-hour paracetamol level: 210 mcg/mL. "
                    "When plotted on Rumack-Matthew nomogram — level is ABOVE the treatment line. "
                    "Baseline labs: AST 32, ALT 28, INR 1.0, Creatinine 0.8. "
                    "Patient still asymptomatic."
                ),
                "scenario_update_tr": (
                    "Aktif kömür verildi (2 saatlik pencere içinde). "
                    "4. saat parasetamol düzeyi: 210 mcg/mL. "
                    "Rumack-Matthew nomogramında — düzey tedavi çizgisinin ÜZERİNDE. "
                    "Bazal laboratuvar: AST 32, ALT 28, INR 1.0, Kreatinin 0.8. "
                    "Hasta hâlâ asemptomatik."
                ),
                "question_en": (
                    "The paracetamol level is above the treatment line. "
                    "What is the specific antidote? How do you administer it?"
                ),
                "question_tr": (
                    "Parasetamol düzeyi tedavi çizgisinin üzerinde. "
                    "Spesifik antidot nedir? Nasıl uygularsınız?"
                ),
                "key_points": [
                    "N-Acetylcysteine (NAC) — the specific antidote",
                    "IV NAC protocol: 150 mg/kg over 1hr, then 50 mg/kg over 4hr, then 100 mg/kg over 16hr",
                    "Start NAC immediately — do not wait for symptoms",
                    "NAC is most effective within 8 hours of ingestion",
                    "Monitor for anaphylactoid reactions to NAC (rash, bronchospasm)",
                ],
            },
            {
                "step": 3,
                "scenario_update_en": (
                    "NAC infusion started. At 24 hours: "
                    "AST 85, ALT 92 (rising), INR 1.1, paracetamol level 15 mcg/mL. "
                    "Patient has developed mild nausea and RUQ tenderness. "
                    "No jaundice. Urine output normal."
                ),
                "scenario_update_tr": (
                    "NAC infüzyonu başlatıldı. 24. saatte: "
                    "AST 85, ALT 92 (yükseliyor), INR 1.1, parasetamol düzeyi 15 mcg/mL. "
                    "Hastada hafif bulantı ve sağ üst kadran hassasiyeti gelişti. "
                    "Sarılık yok. İdrar çıkışı normal."
                ),
                "question_en": (
                    "Liver enzymes are rising. "
                    "Do you continue or stop NAC? What do you monitor now?"
                ),
                "question_tr": (
                    "Karaciğer enzimleri yükseliyor. "
                    "NAC'ı devam mı ettirirsiniz yoksa keser misiniz? Şimdi ne izlersiniz?"
                ),
                "key_points": [
                    "Continue NAC — do not stop while transaminases are rising",
                    "Serial LFTs every 12 hours (AST, ALT, INR, bilirubin)",
                    "Monitor renal function",
                    "Check coagulation (INR is best marker of liver synthetic function)",
                    "King's College Criteria for liver transplant referral",
                    "Hepatology/toxicology consultation",
                ],
            },
            {
                "step": 4,
                "scenario_update_en": (
                    "Day 3: AST peaked at 450, now trending down to 180. ALT 220 → 150. "
                    "INR 1.2 → 1.0. Paracetamol undetectable. Patient feeling better. "
                    "Eating well. No signs of liver failure. Psychiatric evaluation pending."
                ),
                "scenario_update_tr": (
                    "3. gün: AST 450'de zirve yaptı, şimdi 180'e düşüyor. ALT 220 → 150. "
                    "INR 1.2 → 1.0. Parasetamol saptanmıyor. Hasta kendini daha iyi hissediyor. "
                    "İyi yiyor. Karaciğer yetmezliği bulgusu yok. Psikiyatri değerlendirmesi bekliyor."
                ),
                "question_en": (
                    "Liver function is recovering. When can you stop NAC? "
                    "What are the essential steps before discharge?"
                ),
                "question_tr": (
                    "Karaciğer fonksiyonları düzeliyor. NAC'ı ne zaman durdurabilirsiniz? "
                    "Taburculuk öncesi zorunlu adımlar nelerdir?"
                ),
                "key_points": [
                    "Stop NAC when: paracetamol undetectable, AST/ALT declining, INR normal",
                    "Mandatory psychiatric evaluation before discharge",
                    "Safety assessment and suicide risk evaluation",
                    "Restrict access to medications at home",
                    "Follow-up LFTs in 1 week",
                    "Mental health follow-up arranged",
                ],
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # CASE 9 — Organophosphate Poisoning
    # ═══════════════════════════════════════════════════════════════════════════
    "intox_oph_001": {
        "case_id": "intox_oph_001",
        "case_title_en": "Organophosphate Poisoning",
        "case_title_tr": "Organofosfat Zehirlenmesi",
        "case_title": "Organophosphate Poisoning",
        "topic": "Intoxication / Poisoning",
        "difficulty": "Advanced",
        "learning_goals": [
            "Cholinergic toxidrome recognition", "SLUDGE/DUMBELS mnemonic",
            "Atropine titration", "Pralidoxime (2-PAM)", "Decontamination",
            "Respiratory failure management",
        ],
        "steps": [
            {
                "step": 1,
                "scenario_update_en": (
                    "A 45-year-old farmer is brought to the ED after being found "
                    "collapsed in his field next to open pesticide containers. "
                    "He is confused, drooling excessively, and has urinated on himself. "
                    "Strong garlic-like odor noted. Bilateral miotic (pinpoint) pupils. "
                    "His clothes are wet with an unknown liquid."
                ),
                "scenario_update_tr": (
                    "45 yaşında çiftçi, tarlasında açık böcek ilacı kaplarının yanında "
                    "baygın hâlde bulunarak acile getirildi. Konfüze, aşırı salya akıyor "
                    "ve üzerine idrar kaçırmış. Belirgin sarımsak benzeri koku mevcut. "
                    "Bilateral miyotik (iğne ucu) pupiller. Kıyafetleri bilinmeyen "
                    "bir sıvıyla ıslanmış."
                ),
                "question_en": (
                    "What toxidrome do you suspect? "
                    "What are your immediate priorities before starting treatment?"
                ),
                "question_tr": (
                    "Hangi toksidromu düşünüyorsunuz? "
                    "Tedaviye başlamadan önce acil öncelikleriniz nelerdir?"
                ),
                "key_points": [
                    "Cholinergic toxidrome (organophosphate poisoning)",
                    "DECONTAMINATION FIRST: remove clothing, wash skin with soap and water",
                    "Staff PPE (gloves, gown) — avoid secondary contamination",
                    "ABC assessment with focus on airway (excessive secretions)",
                    "Suction airway secretions",
                    "Atropine ready at bedside",
                ],
            },
            {
                "step": 2,
                "scenario_update_en": (
                    "Decontamination performed. PPE worn by staff. "
                    "Vitals: HR 48 (bradycardic), BP 90/60, SpO2 88%, RR 10. "
                    "SLUDGE signs: Salivation +++, Lacrimation, Urination, Diarrhea, "
                    "GI cramps, Emesis. Fasciculations visible in extremities. "
                    "Bronchospasm with audible wheezing. Pupils pinpoint bilaterally."
                ),
                "scenario_update_tr": (
                    "Dekontaminasyon yapıldı. Personel KKE giydi. "
                    "Vitaller: KH 48 (bradikardik), KB 90/60, SpO2 %88, SS 10. "
                    "SLUDGE bulguları: Aşırı salya, lakrimasyon, idrar kaçırma, ishal, "
                    "karın krampları, kusma. Ekstremitelerde fasikülasyonlar görülüyor. "
                    "Bronkospazm ve duyulabilir hışırtı mevcut. Pupiller bilateral iğne ucu."
                ),
                "question_en": (
                    "Classic cholinergic crisis confirmed. "
                    "What is your specific antidote treatment protocol?"
                ),
                "question_tr": (
                    "Klasik kolinerjik kriz doğrulandı. "
                    "Spesifik antidot tedavi protokolünüz nedir?"
                ),
                "key_points": [
                    "IV Atropine 2-4 mg bolus (adult), repeat every 5-10 min",
                    "Titrate atropine to: drying of secretions (NOT pupil size)",
                    "Pralidoxime (2-PAM) 1-2 g IV over 15-30 min",
                    "Give 2-PAM within 24-48 hours (before 'aging' occurs)",
                    "Intubation if respiratory failure (GCS low, SpO2 not improving)",
                    "Do NOT use succinylcholine for intubation (prolonged paralysis)",
                ],
            },
            {
                "step": 3,
                "scenario_update_en": (
                    "After atropine 6 mg total and pralidoxime: secretions drying. "
                    "HR improved to 78, BP 105/70. Patient intubated (GCS dropped to 8). "
                    "Ventilated. SpO2 95% on ventilator. Fasciculations reduced. "
                    "Cholinesterase level sent — pending."
                ),
                "scenario_update_tr": (
                    "Toplam 6 mg atropin ve pralidoksim sonrası: sekresyonlar kuruyor. "
                    "KH 78'e yükseldi, KB 105/70. Hasta entübe edildi (GKS 8'e düştü). "
                    "Ventilasyonda. Ventilatörde SpO2 %95. Fasikülasyonlar azaldı. "
                    "Kolinesteraz düzeyi gönderildi — bekleniyor."
                ),
                "question_en": (
                    "Patient is intubated and stabilizing. "
                    "How do you continue atropine? What complications do you anticipate?"
                ),
                "question_tr": (
                    "Hasta entübe ve stabilize oluyor. "
                    "Atropini nasıl devam ettirirsiniz? Hangi komplikasyonları beklersiniz?"
                ),
                "key_points": [
                    "Atropine infusion (continuous drip) — titrate to secretion control",
                    "Continue pralidoxime infusion for 24-48 hours",
                    "Monitor for intermediate syndrome (muscle weakness at 24-96 hours)",
                    "Watch for recurrence of cholinergic symptoms",
                    "Monitor QTc (risk of arrhythmias)",
                    "ICU admission required",
                ],
            },
            {
                "step": 4,
                "scenario_update_en": (
                    "Day 3: Atropine weaned off. Patient extubated successfully. "
                    "Cholinesterase level: very low (confirms OP poisoning). "
                    "No intermediate syndrome. Patient alert and oriented. "
                    "Psychiatric evaluation done — intentional ingestion confirmed."
                ),
                "scenario_update_tr": (
                    "3. gün: Atropin azaltılarak kesildi. Hasta başarıyla ekstübe edildi. "
                    "Kolinesteraz düzeyi: çok düşük (OP zehirlenmesini doğruluyor). "
                    "İntermediyer sendrom yok. Hasta uyanık ve oryante. "
                    "Psikiyatri değerlendirmesi yapıldı — kasıtlı alım doğrulandı."
                ),
                "question_en": (
                    "What is your discharge plan? What precautions and follow-up are needed?"
                ),
                "question_tr": (
                    "Taburculuk planınız nedir? Hangi önlemler ve takip gereklidir?"
                ),
                "key_points": [
                    "Monitor cholinesterase levels until normalizing",
                    "Watch for delayed polyneuropathy (OPIDN — weeks later)",
                    "Psychiatric follow-up (intentional poisoning)",
                    "Occupational safety education if accidental exposure",
                    "Report to poison control / public health",
                    "Remove access to pesticides at home",
                ],
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # CASE 10 — Acute Severe Asthma / Status Asthmaticus
    # ═══════════════════════════════════════════════════════════════════════════
    "resp_asthma_001": {
        "case_id": "resp_asthma_001",
        "case_title_en": "Acute Severe Asthma",
        "case_title_tr": "Akut Ağır Astım",
        "case_title": "Acute Severe Asthma",
        "topic": "Respiratory Failure",
        "difficulty": "Intermediate",
        "learning_goals": [
            "Asthma severity classification", "Bronchodilator therapy",
            "Systemic corticosteroids", "Non-invasive ventilation",
            "Magnesium sulfate", "Intubation decision",
        ],
        "steps": [
            {
                "step": 1,
                "scenario_update_en": (
                    "A 6-year-old boy with known asthma is brought to the ED by his parents. "
                    "He has been wheezing and coughing for 2 days, worsening since last night. "
                    "He can speak only in short phrases. He is sitting upright, using accessory "
                    "muscles (intercostal and subcostal retractions visible). "
                    "He used his salbutamol inhaler 4 times today with minimal relief."
                ),
                "scenario_update_tr": (
                    "6 yaşında bilinen astım hastası erkek çocuk, ebeveynleri tarafından "
                    "acile getirildi. 2 gündür hışırtı ve öksürük var, dün geceden beri "
                    "kötüleşmiş. Sadece kısa cümleler kurabiliyor. Dik oturuyor, yardımcı "
                    "solunum kaslarını kullanıyor (interkostal ve subkostal çekilmeler görülüyor). "
                    "Bugün salbutamol inhaler'ını 4 kez kullanmış, az rahatlama olmuş."
                ),
                "question_en": (
                    "How do you classify the severity of this asthma exacerbation? "
                    "What is your immediate management?"
                ),
                "question_tr": (
                    "Bu astım alevlenmesinin şiddetini nasıl sınıflandırırsınız? "
                    "Acil tedaviniz nedir?"
                ),
                "key_points": [
                    "Classify as SEVERE acute asthma (speaks in phrases, accessory muscle use)",
                    "Continuous pulse oximetry and cardiac monitoring",
                    "Nebulized salbutamol (continuous or every 20 min × 3)",
                    "Nebulized ipratropium bromide (add to salbutamol)",
                    "Systemic corticosteroids: IV methylprednisolone or oral prednisolone",
                    "High-flow oxygen to maintain SpO2 >94%",
                ],
            },
            {
                "step": 2,
                "scenario_update_en": (
                    "After 3 nebulized salbutamol doses + ipratropium + IV methylprednisolone: "
                    "SpO2 91% on 6L O2, HR 150, RR 40. Still in distress. "
                    "Bilateral expiratory wheeze, air entry reduced bilaterally. "
                    "Speaking in single words only. Peak flow not obtainable. "
                    "ABG: pH 7.35, pCO2 42, pO2 65."
                ),
                "scenario_update_tr": (
                    "3 nebulize salbutamol + ipratropiyum + IV metilprednizolon sonrası: "
                    "SpO2 %91 6L O2 ile, KH 150, SS 40. Hâlâ sıkıntılı. "
                    "Bilateral ekspiratuar hışırtı, bilateral hava girişi azalmış. "
                    "Sadece tek kelimeler söyleyebiliyor. Pik akım ölçülemiyor. "
                    "AKG: pH 7.35, pCO2 42, pO2 65."
                ),
                "question_en": (
                    "Patient is not responding to first-line treatment. "
                    "The ABG shows a normal-high pCO2 in an asthmatic — what does this mean? "
                    "What are your next escalation steps?"
                ),
                "question_tr": (
                    "Hasta birinci basamak tedaviye yanıt vermiyor. "
                    "AKG'de astımlı hastada normal-yüksek pCO2 — bu ne anlama geliyor? "
                    "Sonraki eskalasyon adımlarınız nelerdir?"
                ),
                "key_points": [
                    "Normal/rising pCO2 in acute asthma = respiratory fatigue = DANGER SIGN",
                    "IV magnesium sulfate 40 mg/kg (max 2g) over 20 min",
                    "Consider IV salbutamol infusion",
                    "PICU/ICU consultation",
                    "Prepare for possible intubation",
                    "Chest X-ray to rule out pneumothorax or pneumonia",
                ],
            },
            {
                "step": 3,
                "scenario_update_en": (
                    "IV magnesium given. IV salbutamol infusion started. "
                    "After 30 minutes: SpO2 93%, HR 135, RR 32. Some improvement. "
                    "Air entry slightly better. Patient less distressed. "
                    "Repeat ABG: pH 7.38, pCO2 38, pO2 72. "
                    "Chest X-ray: hyperinflation, no pneumothorax."
                ),
                "scenario_update_tr": (
                    "IV magnezyum verildi. IV salbutamol infüzyonu başlatıldı. "
                    "30 dakika sonra: SpO2 %93, KH 135, SS 32. Bir miktar düzelme. "
                    "Hava girişi biraz daha iyi. Hasta daha az sıkıntılı. "
                    "Tekrar AKG: pH 7.38, pCO2 38, pO2 72. "
                    "Akciğer grafisi: hiperinflasyon, pnömotoraks yok."
                ),
                "question_en": (
                    "Patient is slowly improving. "
                    "What are the criteria for intubation if the patient deteriorates again? "
                    "What ongoing monitoring do you need?"
                ),
                "question_tr": (
                    "Hasta yavaş yavaş düzeliyor. "
                    "Hasta tekrar kötüleşirse entübasyon kriterleri nelerdir? "
                    "Hangi sürekli izlemi yapmanız gerekir?"
                ),
                "key_points": [
                    "Intubation criteria: exhaustion, rising pCO2, decreasing consciousness",
                    "Use ketamine for induction (bronchodilator properties)",
                    "Avoid histamine-releasing agents (morphine, atracurium)",
                    "Continuous SpO2, heart rate, respiratory rate monitoring",
                    "Serial ABGs every 1-2 hours",
                    "Reassess response to treatment frequently",
                ],
            },
            {
                "step": 4,
                "scenario_update_en": (
                    "6 hours later: Patient markedly improved. SpO2 97% on 2L O2. "
                    "HR 110, RR 24. Speaking in full sentences. Wheeze mild. "
                    "IV salbutamol weaned off, back to nebulizers every 4 hours. "
                    "Transferred out of resuscitation to observation area."
                ),
                "scenario_update_tr": (
                    "6 saat sonra: Hasta belirgin düzelme gösteriyor. SpO2 %97 2L O2 ile. "
                    "KH 110, SS 24. Tam cümleler kurabiliyor. Hafif hışırtı var. "
                    "IV salbutamol azaltılarak kesildi, 4 saatte bir nebulize tedaviye geçildi. "
                    "Resüsitasyon odasından gözlem alanına transfer edildi."
                ),
                "question_en": (
                    "The patient is recovering. What is your discharge plan? "
                    "How do you modify the patient's asthma action plan?"
                ),
                "question_tr": (
                    "Hasta düzeliyor. Taburculuk planınız nedir? "
                    "Hastanın astım eylem planını nasıl düzenlersiniz?"
                ),
                "key_points": [
                    "Continue oral prednisolone for 3-5 days",
                    "Step up controller therapy (inhaled corticosteroid dose increase)",
                    "Ensure correct inhaler technique (spacer device for children)",
                    "Written asthma action plan for family",
                    "Identify and avoid triggers",
                    "Follow-up with pediatric pulmonology in 1-2 weeks",
                    "Review need for long-acting beta-agonist (LABA) add-on",
                ],
            },
        ],
    },
}
