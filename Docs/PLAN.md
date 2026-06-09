# PLAN.md — MedCase Agent MVP

## Project Name
**MedCase Agent — Autonomous Clinical Reasoning Tutor for Medical Students**

## Goal
Build a working MVP for the Google for Startups AI Agents Challenge.

The product is an autonomous AI medical learning agent that simulates clinical reasoning sessions for medical students. It generates patient cases, evaluates student answers, asks adaptive follow-up questions, tracks weak topics, and gives structured feedback.

This is an **educational simulation tool**, not a real medical diagnosis or treatment system.

---

## Core MVP Scope

Build a web app with:

1. A simple student login/demo user flow
2. Topic and difficulty selection
3. Dynamic clinical case simulation
4. Student answer input
5. AI evaluation of each answer
6. Adaptive next question generation
7. Weak topic tracking
8. Session summary
9. Basic dashboard showing weak topics and previous sessions

Do **not** build a full production medical platform. Focus on a clean, working demo.

---

## Recommended Tech Stack

### Backend
- Python
- FastAPI
- SQLite for MVP
- SQLAlchemy or simple sqlite3
- Google Gemini API
- Google ADK-style agent structure

### Frontend
- React / Next.js preferred
- Simple responsive UI
- Chat-style case simulation screen
- Dashboard screen

### Deployment
- Google Cloud Run preferred
- Local development must work first

---

## Safety Rules

The app must always follow these rules:

- Use only fictional or synthetic patient cases.
- Never claim to diagnose or treat real patients.
- Always describe the system as an educational simulation tool.
- Add a visible disclaimer in the UI:
  > This tool is for medical education and simulated clinical reasoning practice only. It does not provide real patient diagnosis or treatment.
- Avoid giving unsafe medical advice outside the simulated education context.
- Evaluation should be framed as student learning feedback.

---

## Main User Flow

### 1. Start Session
Student selects:

- Topic
- Difficulty
- Optional weak topic focus

Example topics:

- Pediatric Emergency
- Cardiology
- Neonatology
- Allergy and Anaphylaxis

Example difficulty levels:

- Beginner
- Intermediate
- Advanced

The backend creates a new session and generates the first clinical case prompt.

---

### 2. Case Simulation
The student sees a case opening.

Example:

> A 10-year-old girl presents to the emergency department with sudden palpitations for 30 minutes. She is conscious and anxious. What is your first approach?

Student writes an answer.

---

### 3. Evaluation
The Examiner Agent evaluates the answer and returns structured JSON:

```json
{
  "score": 85,
  "is_safe": true,
  "correct_points": [
    "ABC assessment mentioned",
    "Vital signs requested",
    "ECG requested"
  ],
  "missing_points": [
    "Hemodynamic stability should be assessed explicitly"
  ],
  "unsafe_points": [],
  "weak_topics": [
    "Hemodynamic stability assessment"
  ],
  "feedback": "Good first step. You correctly prioritized ABC, vital signs and ECG. However, in tachycardia cases, you should explicitly determine whether the patient is stable or unstable because this changes management.",
  "next_question": "The ECG shows a regular narrow-complex tachycardia at 220/min. The patient is stable. What would you do next?",
  "difficulty_change": "same"
}
```

---

### 4. Adaptive Questioning
The next question should depend on the student answer.

Rules:

- If answer is strong: increase complexity.
- If answer is incomplete: ask a guiding follow-up.
- If answer is unsafe: explain the safety issue and redirect.
- If the same weakness appears repeatedly: save it as a weak topic.

---

### 5. Session Summary
After 5–7 questions, generate a session summary.

Summary must include:

- Total score
- Strong topics
- Weak topics
- Reasoning mistakes
- Recommended next case
- Recommended review topics

---

## MVP Demo Cases

Implement at least 3 demo case templates.

### Case 1 — Pediatric SVT

Learning goals:

- ABC approach
- Vital signs
- ECG request
- Stable vs unstable tachycardia
- Vagal maneuver
- Adenosine
- Synchronized cardioversion for unstable patient

Opening prompt:

> A 10-year-old girl presents to the emergency department with sudden palpitations for 30 minutes. She is conscious, anxious, and has no chest pain. What is your first approach?

---

### Case 2 — Neonatal Seizure

Learning goals:

- Immediate stabilization
- Glucose check
- Calcium and electrolyte assessment
- Sepsis evaluation
- Hypoxic ischemic injury
- Intracranial hemorrhage
- Metabolic causes

Opening prompt:

> A 3-day-old newborn is brought to the emergency department with abnormal jerking movements and poor feeding. What is your first approach?

---

### Case 3 — Anaphylaxis

Learning goals:

- Recognition of anaphylaxis
- Airway, breathing, circulation
- Intramuscular adrenaline/epinephrine
- Oxygen
- IV fluids
- Observation
- Avoiding delay in epinephrine

Opening prompt:

> A 7-year-old child develops generalized urticaria, facial swelling, cough, and difficulty breathing after eating peanuts. What is your first approach?

---

## Backend API

### POST `/session/start`

Request:

```json
{
  "student_id": "demo_user",
  "topic": "Pediatric Emergency",
  "difficulty": "Intermediate"
}
```

Response:

```json
{
  "session_id": "session_123",
  "case_id": "peds_svt_001",
  "case_title": "Pediatric SVT",
  "question": "A 10-year-old girl presents..."
}
```

---

### POST `/session/{session_id}/answer`

Request:

```json
{
  "answer": "I would assess ABC, check vital signs, monitor the patient, and order an ECG."
}
```

Response:

```json
{
  "score": 90,
  "is_safe": true,
  "correct_points": [],
  "missing_points": [],
  "unsafe_points": [],
  "weak_topics": [],
  "feedback": "...",
  "next_question": "...",
  "difficulty_change": "same"
}
```

---

### GET `/session/{session_id}/summary`

Response:

```json
{
  "session_id": "session_123",
  "total_score": 82,
  "strong_topics": [
    "Initial emergency assessment",
    "ECG request"
  ],
  "weak_topics": [
    "Adenosine dosing",
    "Unstable SVT management"
  ],
  "recommendations": [
    "Review stable vs unstable tachycardia algorithm",
    "Practice another SVT case"
  ],
  "recommended_next_case": "Unstable tachycardia simulation"
}
```

---

### GET `/student/{student_id}/weak-topics`

Response:

```json
{
  "student_id": "demo_user",
  "weak_topics": [
    {
      "topic": "Adenosine dosing",
      "frequency": 3,
      "last_seen": "2026-05-28"
    }
  ]
}
```

---

### GET `/student/{student_id}/sessions`

> **Added in Faz 1 — MVP Tamamlama**

Returns all sessions for a student, ordered newest first.

Response:

```json
[
  {
    "session_id": "session_123",
    "topic": "Pediatric Emergency",
    "difficulty": "Intermediate",
    "case_title": "Pediatric SVT",
    "status": "active",
    "total_score": 85,
    "current_step": 3,
    "language": "en",
    "created_at": "2026-06-01T10:00:00Z",
    "updated_at": "2026-06-01T10:15:00Z"
  }
]
```

---

### GET `/student/{student_id}/dashboard`

> **Added in Faz 1 — MVP Tamamlama**

Full dashboard data: sessions list + stats + weak topics in one call.

Response:

```json
{
  "student_id": "demo_user",
  "student_name": "Demo Student",
  "average_score": 78.5,
  "total_sessions": 5,
  "completed_sessions": 3,
  "sessions": [ "...SessionListItem array..." ],
  "weak_topics": [ "...WeakTopicItem array..." ]
}
```

---

### GET `/session/{session_id}/resume`

> **Added in Faz 1 — MVP Tamamlama**

Returns current state of an active session so the frontend can resume it.

Response:

```json
{
  "session_id": "session_123",
  "case_title": "Pediatric SVT",
  "status": "active",
  "current_step": 3,
  "language": "en",
  "scenario_update": "...",
  "question": "...",
  "total_score": 85
}
```

---

## Database Schema

Use SQLite for MVP.

### `students`

```sql
CREATE TABLE students (
  id TEXT PRIMARY KEY,
  name TEXT,
  level TEXT,
  created_at TEXT
);
```

### `sessions`

```sql
CREATE TABLE sessions (
  id TEXT PRIMARY KEY,
  student_id TEXT,
  topic TEXT,
  difficulty TEXT,
  case_id TEXT,
  case_title TEXT,
  current_step INTEGER,
  status TEXT,
  total_score INTEGER,
  created_at TEXT,
  updated_at TEXT
);
```

### `answers`

```sql
CREATE TABLE answers (
  id TEXT PRIMARY KEY,
  session_id TEXT,
  step_number INTEGER,
  question TEXT,
  student_answer TEXT,
  score INTEGER,
  is_safe INTEGER,
  correct_points TEXT,
  missing_points TEXT,
  unsafe_points TEXT,
  weak_topics TEXT,
  feedback TEXT,
  next_question TEXT,
  created_at TEXT
);
```

### `weak_topics`

```sql
CREATE TABLE weak_topics (
  id TEXT PRIMARY KEY,
  student_id TEXT,
  topic TEXT,
  frequency INTEGER,
  last_seen TEXT
);
```

---

## Agent Architecture

Implement the system as separate logical agents, even if they are Python classes/functions in the MVP.

### 1. Case Generator Agent

Responsibilities:

- Generate or select a fictional clinical case
- Adapt case to topic and difficulty
- Use previous weak topics if available
- Do not reveal final diagnosis too early

Input:

```json
{
  "topic": "Pediatric Emergency",
  "difficulty": "Intermediate",
  "weak_topics": ["SVT management"]
}
```

Output:

```json
{
  "case_id": "peds_svt_001",
  "case_title": "Pediatric SVT",
  "opening_question": "..."
}
```

---

### 2. Examiner Agent

Responsibilities:

- Evaluate student response
- Score clinical reasoning
- Identify correct, missing, and unsafe points
- Detect weak topics
- Produce the next adaptive question

Output must be structured JSON.

---

### 3. Feedback Agent

Responsibilities:

- Convert evaluation into clear educational feedback
- Explain reasoning step-by-step
- Avoid overly long explanations
- Keep tone supportive but direct

---

### 4. Adaptive Tutor Agent

Responsibilities:

- Decide whether to increase, keep, or decrease difficulty
- Choose the next question
- Reinforce weak areas
- End session after enough steps

---

### 5. Progress Tracker Agent

Responsibilities:

- Save scores
- Save weak topics
- Update topic frequency
- Generate session summary
- Recommend next case

---

## Prompt Templates

### Case Generator Prompt

```text
You are a clinical case generation agent for medical education.

Generate a realistic but fictional educational patient case for a medical student.

Rules:
- Do not use real patient data.
- This is for simulated medical education only.
- Adapt the case to the student's level.
- Include only the first visible part of the case.
- Do not reveal the final diagnosis immediately.
- Return structured JSON only.

Student level: {difficulty}
Topic: {topic}
Weak topics: {weak_topics}
```

---

### Examiner Prompt

```text
You are a clinical reasoning examiner for medical students.

Evaluate the student's answer in the context of the current simulated case.

Rules:
- This is educational simulation, not real patient care.
- Do not provide real patient-specific diagnosis or treatment.
- Evaluate the student's clinical reasoning.
- Check whether the student followed safe clinical logic.
- Identify correct points, missing points, unsafe points, and weak topics.
- Ask exactly one adaptive follow-up question.
- Return structured JSON only.

Case:
{case}

Current question:
{question}

Student answer:
{answer}
```

---

## JSON Evaluation Schema

All AI evaluations must match this structure:

```json
{
  "score": 0,
  "is_safe": true,
  "correct_points": [],
  "missing_points": [],
  "unsafe_points": [],
  "weak_topics": [],
  "feedback": "",
  "next_question": "",
  "difficulty_change": "same"
}
```

Rules:

- `score` must be between 0 and 100.
- `difficulty_change` must be one of:
  - `increase`
  - `same`
  - `decrease`
- `next_question` must contain only one question.
- `feedback` must be educational and concise.
- `unsafe_points` should be empty unless the student's response contains dangerous reasoning.

---

## Frontend Pages

### Page 1 — Home / Start

Components:

- App title
- Disclaimer
- Topic selector
- Difficulty selector
- Start button

---

### Page 2 — Simulation

Components:

- Case title
- Current question
- Student answer text area
- Submit button
- Feedback panel
- Progress indicator
- Weak topics mini panel

---

### Page 3 — Summary

Components:

- Total score
- Strong topics
- Weak topics
- Recommendations
- Recommended next case
- Restart button

---

### Page 4 — Dashboard

Components:

- Previous sessions
- Average score
- Weak topic list
- Recommended next simulations

---

## UI Style

Use a clean medical education dashboard style.

Recommended design:

- White or light background
- Blue/green accent
- Card-based layout
- Clear typography
- Minimal clutter
- Strong separation between:
  - case prompt
  - student answer
  - AI feedback
  - weak topics

Important: The UI should feel like a professional educational tool, not a casual chatbot.

---

## Development Phases

## Phase 1 — Backend Foundation

Tasks:

- Create FastAPI project
- Add SQLite database
- Add models/tables
- Add seed demo student
- Add static demo cases
- Implement `/session/start`
- Implement `/session/{id}/answer`
- Implement `/session/{id}/summary`

Acceptance criteria:

- Backend runs locally.
- A session can be started.
- An answer can be submitted.
- Evaluation is returned.
- Session summary works.

---

## Phase 2 — Gemini Integration

Tasks:

- Connect Gemini API
- Implement structured evaluation response
- Add fallback rule-based evaluation if Gemini fails
- Validate JSON output
- Store evaluation in database

Acceptance criteria:

- Student answer is evaluated by Gemini.
- Output always returns valid JSON.
- App does not crash if AI output is malformed.
- Weak topics are saved.

---

## Phase 3 — Adaptive Learning

Tasks:

- Track repeated weak topics
- Use weak topics when starting new cases
- Adjust next question based on score
- End session after 5–7 steps
- Generate summary

Acceptance criteria:

- Weak topics influence future sessions.
- Low score triggers simpler follow-up.
- High score triggers more advanced follow-up.
- Session summary reflects actual performance.

---

## Phase 4 — Frontend

Tasks:

- Create home page
- Create simulation page
- Create feedback panel
- Create summary page
- Create dashboard page
- Connect API calls

Acceptance criteria:

- User can complete a full clinical simulation from UI.
- Feedback appears after each answer.
- Summary appears at the end.
- Dashboard displays weak topics.

---

## Phase 5 — Demo Polish

Tasks:

- Add 3 polished demo cases
- Add loading states
- Add error handling
- Add educational disclaimer
- Add sample login/demo mode
- Prepare architecture diagram
- Prepare demo script

Acceptance criteria:

- The app is demo-ready.
- A judge can test the app without setup confusion.
- The demo clearly shows autonomous agent behavior.

---

## Demo Script

Use this flow in the video:

1. Open dashboard.
2. Show demo student profile with weak topics.
3. Start Pediatric Emergency case.
4. Agent presents SVT case.
5. Student gives incomplete answer.
6. Agent scores answer and asks adaptive follow-up.
7. Student improves answer.
8. Agent increases difficulty.
9. End session.
10. Show weak topic tracking and recommended next case.

Key message:

> MedCase Agent does not simply answer questions. It runs an adaptive clinical reasoning loop: generate case, evaluate response, ask follow-up, track weaknesses, and personalize future learning.

---

## Devpost Submission Notes

### Project Description

MedCase Agent is an autonomous clinical reasoning tutor for medical students. It simulates realistic patient encounters, evaluates student decisions in real time, asks adaptive follow-up questions, and generates personalized learning paths based on weak topics.

The agent guides students through history taking, physical examination, differential diagnosis, investigations, diagnosis, and management. It is designed for education only and does not provide real patient diagnosis or treatment.

---

### Google Technologies to Mention

- Gemini models for clinical reasoning simulation
- Google Agent Development Kit-inspired multi-agent architecture
- Structured JSON outputs for reliable evaluation
- Tool-based workflow for student profile, progress tracking, and learning plan generation
- Google Cloud Run for deployment

---

### Judging Criteria Alignment

#### Technical Implementation
- Multi-agent workflow
- Structured outputs
- Session state
- Weak topic tracking
- Adaptive difficulty
- Cloud deployment

#### Business Case
- Helps medical students practice clinical reasoning
- Reduces fragmented learning
- Can integrate into MedApp
- Freemium and institutional licensing model

#### Innovation
- Moves beyond static question banks
- Simulates clinical encounters
- Personalizes learning through weak-topic memory
- Gives reasoning-based feedback

#### Demo and Presentation
- Live case simulation
- Real-time evaluation
- Adaptive follow-up questions
- Performance dashboard

---

## F2.4 — Performance Charts (Completed)

Dashboard sayfasına `chart.js` + `react-chartjs-2` ile 3 performans grafiği eklendi:

### Weak Topic Frequency Bar Chart
- Yatay bar chart
- Zayıf konuların tekrar sıklığını gösterir
- Frekansa göre renk kodlaması (düşük → mavi, orta → sarı, yüksek → kırmızı)

### Score Trend Line Chart
- Tamamlanmış oturumların skor trendini gösterir
- Skor ≥80 yeşil, ≥50 sarı, <50 kırmızı nokta renkleri
- Mavi gradient fill ile alan grafiği

### Topic Radar Chart
- Konu bazlı ortalama skor radar grafiği
- En az 3 farklı konu gerektirir
- Mor renk teması ile görselleştirme

Files:
- `frontend/app/dashboard/PerformanceCharts.tsx` (NEW)
- `frontend/app/dashboard/page.tsx` (MODIFIED — chart imports and integration)

---

## F2.5 — Markdown/Rich Text Feedback (Completed)

Simülasyon sayfasındaki AI feedback'leri artık Markdown formatında render ediliyor:

### Frontend
- `react-markdown` + `remark-gfm` ile Markdown parsing
- Tıbbi terimlerin `**bold**` ile vurgulanması (mavi arka planlı)
- `code` formatında dozaj/ölçüm değerleri (yeşil arka planlı)
- Listeler, blockquote referanslar ve tablolar desteği
- Custom component override'ları ile premium görünüm

### Backend
- Examiner Agent prompt'una Markdown format talimatları eklendi
- Gemini API artık Markdown-formatted feedback döndürüyor
- Rule-based fallback evaluator da Markdown formatting kullanıyor

Files:
- `frontend/app/simulation/RichFeedback.tsx` (NEW)
- `frontend/app/simulation/page.tsx` (MODIFIED — RichFeedback integration)
- `frontend/app/globals.css` (MODIFIED — rich-feedback styles)
- `backend/app/agents/examiner.py` (MODIFIED — Markdown prompt)

---

## F3.1 — OSCE Mode (Completed)

OSCE (Objective Structured Clinical Examination) simülasyonu eklendi. Zamanlı istasyonlar ile yapılandırılmış klinik sınav modu.

### OSCE Setleri
3 adet OSCE seti, her biri 4 istasyon:
1. **Pediatric Emergency OSCE** — SVT, Anaphylaxis, Discharge Counseling (Intermediate)
2. **Internal Medicine OSCE** — Chest Pain, STEMI, Heart Failure, Drug Overdose (Advanced)
3. **Trauma & Emergency Surgery OSCE** — Polytrauma, Hemorrhagic Shock, FAST, Post-op (Advanced)

### İstasyon Tipleri
- `history` — Öykü alma
- `physical_exam` — Fizik muayene
- `diagnosis` — Tanı koyma
- `management` — Tedavi yönetimi
- `communication` — Hasta/aile iletişimi

### Özellikler
- 8 dakika/istasyon zamanlayıcı (dairesel progress bar)
- Süre dolunca otomatik gönderim
- Checklist bazlı OSCE puanlama (AI + keyword matching blend)
- İstasyon bazlı sonuç görünümü
- Toplam OSCE özeti (güçlü/zayıf alanlar, öneriler)

### Files
- `backend/app/data/osce_stations.py` (NEW — OSCE veri tanımları)
- `backend/app/routers/osce.py` (NEW — OSCE endpointleri)
- `backend/app/schemas.py` (MODIFIED — OSCE schemas)
- `backend/app/models.py` (MODIFIED — session_type alanı)
- `backend/app/main.py` (MODIFIED — OSCE router + migration)
- `frontend/app/osce/page.tsx` (NEW — OSCE başlangıç sayfası)
- `frontend/app/osce/exam/page.tsx` (NEW — OSCE sınav sayfası)
- `frontend/app/osce/exam/StationTimer.tsx` (NEW — zamanlayıcı bileşeni)
- `frontend/app/layout.tsx` (MODIFIED — OSCE nav link)
- `frontend/lib/api.ts` (MODIFIED — OSCE API çağrıları)

---

## F3.3 — Voice Exam Simulation (Completed)

Web Speech API ile sesli sınav simülasyonu. Öğrenci cevabını konuşarak verebilir.

### Özellikler
- Web Speech API (SpeechRecognition) entegrasyonu
- Toggle modunda mikrofon butonu (basınca kayıt başlar/bırakınca durur)
- Gerçek zamanlı konuşma transkript'i
- EN/TR dil desteği (`en-US`, `tr-TR`)
- Tarayıcı uyumluluk kontrolü (desteklemiyorsa buton gizlenir)
- Pulse animasyonu ile kayıt durumu göstergesi
- Hem OSCE hem normal simülasyon sayfasında kullanılabilir

### Desteklenen Tarayıcılar
- ✅ Chrome, Edge, Safari
- ❌ Firefox (Web Speech API desteklenmez — graceful degradation)

### Files
- `frontend/app/components/VoiceInput.tsx` (NEW — sesli giriş bileşeni)
- `frontend/app/simulation/page.tsx` (MODIFIED — VoiceInput entegrasyonu)
- `frontend/app/osce/exam/page.tsx` (VoiceInput entegre)

---

## F4.1 — UI Readability Improvements (Completed)

Tüm frontend sayfalarında okunabilirlik iyileştirmesi yapıldı. Soluk renkler, küçük fontlar ve düşük kontrast sorunları giderildi.

### Düzeltilen Sorunlar
- **Soluk metin renkleri**: `text-slate-400` → `text-slate-500/600` (label'lar, açıklamalar, tarihler)
- **Küçük disclaimer barı**: `text-xs` → `text-sm`, `py-1.5` → `py-2`, `font-medium` + `tracking-wide` eklendi
- **Form label'ları**: `font-medium text-slate-600` → `font-semibold text-slate-700` (tüm sayfalarda)
- **Tablo başlıkları**: `text-slate-400` → `text-slate-500` (dashboard session history)
- **Tarih sütunu**: `text-xs text-slate-400` → `text-sm text-slate-500`
- **Alt açıklamalar**: `text-slate-400` → `text-slate-500` (chart açıklamaları, section alt başlıkları)
- **Navigasyon**: Nav link'ler `font-medium` → `font-semibold`, renkler koyulaştırıldı
- **RichFeedback**: Paragraf, liste, blockquote ve tablo hücre metinleri koyulaştırıldı
- **Weak topic badge'ler**: `font-medium` eklendi, metin `text-slate-700` yapıldı
- **OSCE timer label**: `font-medium text-slate-400` → `font-semibold text-slate-500`

### Etkilenen Dosyalar
- `frontend/app/layout.tsx` (MODIFIED — disclaimer bar, nav links)
- `frontend/app/page.tsx` (MODIFIED — subtitle, labels, feature cards)
- `frontend/app/simulation/page.tsx` (MODIFIED — case label, answer label, score, weak topics)
- `frontend/app/simulation/RichFeedback.tsx` (MODIFIED — paragraphs, lists, blockquotes, tables)
- `frontend/app/dashboard/page.tsx` (MODIFIED — stat labels, table, weak topics, dates)
- `frontend/app/dashboard/PerformanceCharts.tsx` (MODIFIED — chart descriptions)
- `frontend/app/summary/page.tsx` (MODIFIED — score label, denominator)
- `frontend/app/osce/page.tsx` (MODIFIED — subtitle, labels, info text)
- `frontend/app/osce/exam/page.tsx` (MODIFIED — station info, scenario labels, checklist)
- `frontend/app/osce/exam/StationTimer.tsx` (MODIFIED — timer label)

---

## F4.2 — Dark Mode Background & Form Control Contrast Fixes (Completed)

Kullanıcının tarayıcı/sistem koyu mod (dark mode) tercihine sahip olması durumunda arka planın kararması ve bazı metinlerin (başlıklar, açıklamalar) okunamaz hale gelmesi sorunu giderildi. Uygulama tıbbi eğitim tasarımı gereği açık renkli (light mode) bir temaya sahip olduğu için light mode sabitlendi.

### Düzeltilen Sorunlar
- **Koyu Arka Plan Sorunu**: `globals.css` dosyasındaki `@media (prefers-color-scheme: dark)` medya sorgusu silindi ve `:root` etiketine `color-scheme: light` eklenerek uygulamanın her koşulda açık renk modunda çalışması sağlandı.
- **Form Elemanlarının Arka Planları**: `select` ve `textarea` gibi form girdilerinin tarayıcı tarafından otomatik olarak koyu renk yapılmasını önlemek amacıyla bu elemanlara açıkça `bg-white` sınıfları eklendi.

### Etkilenen Dosyalar
- `frontend/app/globals.css` (MODIFIED — prefers-color-scheme dark rules removed, color-scheme light forced)
- `frontend/app/page.tsx` (MODIFIED — added bg-white to topic select dropdown)
- `frontend/app/simulation/page.tsx` (MODIFIED — added bg-white to answer textarea)
- `frontend/app/osce/page.tsx` (MODIFIED — added bg-white to OSCE set select dropdown)
- `frontend/app/osce/exam/page.tsx` (MODIFIED — added bg-white to answer textarea)

---

## Out of Scope for MVP

Do not implement these in the first version:

- Real patient data
- Real hospital integration
- Real diagnosis for patients
- Complex authentication
- Payment system
- Full mobile app
- Full curriculum coverage
- Voice input
- PDF upload
- Faculty admin panel

These can be mentioned as future work.

---

## Future Improvements

After MVP:

- MedApp integration
- PDF lecture note upload
- Faculty dashboard
- OSCE mode
- Exam preparation mode
- Voice-based oral exam simulation
- Multi-language support
- More specialty case packs
- Spaced repetition scheduling
- Google Calendar study plan integration

---

## Final MVP Success Definition

The MVP is successful if a user can:

1. Start a clinical case simulation
2. Answer multiple adaptive questions
3. Receive structured feedback after each answer
4. See weak topics detected automatically
5. Complete the session
6. View personalized recommendations

If these six things work, the project is strong enough for the hackathon demo.
