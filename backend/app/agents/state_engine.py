"""
Patient State Engine
Manages patient baseline vitals and formats vitals state for simulations.
"""

BASELINES = {
    "peds_svt_001": {
        "heart_rate": 220,
        "blood_pressure": "100/60",
        "spo2": 98,
        "respiratory_rate": 20,
        "temperature": 37.1,
        "status_description_en": "Active SVT. Conscious, talking, but anxious. Hemodynamically stable.",
        "status_description_tr": "Aktif SVT. Bilinci açık, konuşabiliyor ancak kaygılı. Hemodinamik olarak stabil.",
    },
    "neonatal_seizure_001": {
        "heart_rate": 162,
        "blood_pressure": "65/40",
        "spo2": 94,
        "respiratory_rate": 48,
        "temperature": 36.8,
        "status_description_en": "Active generalized tonic-clonic movements, poor feeding, lethargic.",
        "status_description_tr": "Aktif jeneralize tonik-klonik hareketler, beslenme yetersizliği, letarjik.",
    },
    "anaphylaxis_001": {
        "heart_rate": 148,
        "blood_pressure": "80/50",
        "spo2": 88,
        "respiratory_rate": 36,
        "temperature": 37.0,
        "status_description_en": "Severe respiratory distress. Facial/lip swelling, generalized hives, audible stridor.",
        "status_description_tr": "Ciddi solunum sıkıntısı. Yüz/dudak şişmesi, jeneralize ürtiker, işitilebilir stridor.",
    },
    "cardio_ami_001": {
        "heart_rate": 96,
        "blood_pressure": "150/95",
        "spo2": 96,
        "respiratory_rate": 22,
        "temperature": 36.9,
        "status_description_en": "Diaphoretic, pale, anxious. Crushing substernal chest pain radiating to left arm.",
        "status_description_tr": "Terli, soluk, kaygılı. Sol kola yayılan ezici substernal göğüs ağrısı.",
    },
    "cardio_hf_001": {
        "heart_rate": 120,
        "blood_pressure": "180/100",
        "spo2": 85,
        "respiratory_rate": 32,
        "temperature": 37.0,
        "status_description_en": "Severe dyspnea, orthopneic, pink frothy sputum. Bilateral crackles in mid-lung fields.",
        "status_description_tr": "Şiddetli dispne, ortopneik, pembe köpüklü balgam. Akciğer orta alanlarında bilateral raller.",
    },
    "trauma_poly_001": {
        "heart_rate": 140,
        "blood_pressure": "85/50",
        "spo2": 94,
        "respiratory_rate": 28,
        "temperature": 36.5,
        "status_description_en": "Lethargic, crying, confused (GCS 12). Swollen, shortened left thigh, right abdominal guarding.",
        "status_description_tr": "Letarjik, ağlıyor, konfüze (GKS 12). Sol uylukta şişlik ve kısalma, sağ batında defans.",
    },
    "trauma_abd_001": {
        "heart_rate": 105,
        "blood_pressure": "110/70",
        "spo2": 99,
        "respiratory_rate": 20,
        "temperature": 37.0,
        "status_description_en": "LUQ abdominal tenderness, positive Kehr's sign (referred left shoulder pain). Stable.",
        "status_description_tr": "Sol üst kadran hassasiyeti, pozitif Kehr belirtisi (sol omuza yayılan ağrı). Stabil.",
    },
    "intox_paracetamol_001": {
        "heart_rate": 80,
        "blood_pressure": "120/80",
        "spo2": 99,
        "respiratory_rate": 16,
        "temperature": 36.7,
        "status_description_en": "Currently asymptomatic. Rumack-Matthew Nomogram indicates toxic paracetamol ingestion (~15g).",
        "status_description_tr": "Şu anda asemptomatik. Rumack-Matthew Nomogramı toksik parasetamol alımına işaret ediyor (~15g).",
    },
    "intox_oph_001": {
        "heart_rate": 48,
        "blood_pressure": "90/60",
        "spo2": 88,
        "respiratory_rate": 10,
        "temperature": 36.5,
        "status_description_en": "Bradycardia, pinpoint pupils, salivation, sweating, fasciculations. Cholinergic crisis.",
        "status_description_tr": "Bradikardi, iğne ucu pupiller, salivasyon, terleme, fasikülasyonlar. Kolinerjik kriz.",
    },
}

DEFAULT_BASELINE = {
    "heart_rate": 80,
    "blood_pressure": "120/80",
    "spo2": 99,
    "respiratory_rate": 16,
    "temperature": 37.0,
    "status_description_en": "Hemodynamically stable patient.",
    "status_description_tr": "Hemodinamik olarak stabil hasta.",
}


class PatientStateEngine:
    def get_baseline_vitals(self, case_id: str, language: str = "en") -> dict:
        """Return baseline vitals for a given case_id, fallback to default."""
        base = BASELINES.get(case_id, DEFAULT_BASELINE).copy()
        lang = language if language in ("en", "tr") else "en"
        
        # Populate status_description based on active language
        if f"status_description_{lang}" in base:
            base["status_description"] = base[f"status_description_{lang}"]
        elif "status_description_en" in base:
            base["status_description"] = base["status_description_en"]
        
        # Clean up bilingual fields
        base.pop("status_description_en", None)
        base.pop("status_description_tr", None)
        return base

    def format_vitals_text(self, vitals: dict) -> str:
        """Return a formatted string representing the vitals."""
        return (
            f"Heart Rate: {vitals.get('heart_rate', 0)} bpm | "
            f"Blood Pressure: {vitals.get('blood_pressure', 'N/A')} mmHg | "
            f"SpO2: {vitals.get('spo2', 0)}% | "
            f"Respiratory Rate: {vitals.get('respiratory_rate', 0)}/min | "
            f"Temp: {vitals.get('temperature', 0.0)} C\n"
            f"Status: {vitals.get('status_description', 'No details.')}"
        )
