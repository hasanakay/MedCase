// Central API client — all backend calls go through here

const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000";

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`API error ${res.status}: ${body}`);
  }
  return res.json() as Promise<T>;
}

// ── Types ────────────────────────────────────────────────────────────────────

export interface SessionStartRequest {
  student_id: string;
  topic: string;
  difficulty: string;
  language?: string;
  weak_topic_focus?: string;
}

export interface SessionStartResponse {
  session_id: string;
  case_id: string;
  case_title: string;
  scenario_update: string;
  question: string;
  vitals?: Record<string, any>;
}

export interface EvaluationResponse {
  score: number;
  is_safe: boolean;
  correct_points: string[];
  missing_points: string[];
  unsafe_points: string[];
  weak_topics: string[];
  feedback: string;
  next_scenario_update: string;
  next_question: string;
  difficulty_change: "increase" | "same" | "decrease";
  session_complete: boolean;
  vitals?: Record<string, any>;
}

export interface SessionSummary {
  session_id: string;
  total_score: number;
  strong_topics: string[];
  weak_topics: string[];
  recommendations: string[];
  recommended_next_case: string;
}

export interface WeakTopicItem {
  topic: string;
  frequency: number;
  last_seen: string;
}

export interface TopicsResponse {
  topics: string[];
  difficulties: string[];
}

export interface SessionListItem {
  session_id: string;
  topic: string;
  difficulty: string;
  case_title: string;
  status: string;
  total_score: number;
  current_step: number;
  language: string;
  created_at: string;
  updated_at: string;
}

export interface DashboardResponse {
  student_id: string;
  student_name: string;
  average_score: number;
  total_sessions: number;
  completed_sessions: number;
  sessions: SessionListItem[];
  weak_topics: WeakTopicItem[];
}

export interface ResumeSessionResponse {
  session_id: string;
  case_title: string;
  status: string;
  current_step: number;
  language: string;
  scenario_update: string;
  question: string;
  total_score: number;
  vitals?: Record<string, any>;
}

// ── API calls ─────────────────────────────────────────────────────────────────

export const api = {
  getTopics: () => request<TopicsResponse>("/topics"),

  startSession: (body: SessionStartRequest) =>
    request<SessionStartResponse>("/session/start", {
      method: "POST",
      body: JSON.stringify(body),
    }),

  submitAnswer: (sessionId: string, answer: string) =>
    request<EvaluationResponse>(`/session/${sessionId}/answer`, {
      method: "POST",
      body: JSON.stringify({ answer }),
    }),

  getSummary: (sessionId: string) =>
    request<SessionSummary>(`/session/${sessionId}/summary`),

  getWeakTopics: (studentId: string) =>
    request<{ student_id: string; weak_topics: WeakTopicItem[] }>(
      `/student/${studentId}/weak-topics`
    ),

  getDashboard: (studentId: string) =>
    request<DashboardResponse>(`/student/${studentId}/dashboard`),

  getSessions: (studentId: string) =>
    request<SessionListItem[]>(`/student/${studentId}/sessions`),

  resumeSession: (sessionId: string) =>
    request<ResumeSessionResponse>(`/session/${sessionId}/resume`),

  // ── OSCE API calls ────────────────────────────────────────────────────────

  getOSCESets: (language: string = "en") =>
    request<OSCESetSummary[]>(`/osce/sets?language=${language}`),

  startOSCE: (body: OSCEStartRequest) =>
    request<OSCEStartResponse>("/osce/start", {
      method: "POST",
      body: JSON.stringify(body),
    }),

  getOSCEStation: (sessionId: string, stationNumber: number) =>
    request<OSCEStationResponse>(`/osce/${sessionId}/station/${stationNumber}`),

  submitOSCEAnswer: (sessionId: string, stationNumber: number, answer: string, timeSpent: number) =>
    request<OSCEStationResult>(`/osce/${sessionId}/station/${stationNumber}/answer`, {
      method: "POST",
      body: JSON.stringify({ answer, time_spent_seconds: timeSpent }),
    }),

  getOSCESummary: (sessionId: string) =>
    request<OSCESummaryResponse>(`/osce/${sessionId}/summary`),
};

// ── OSCE Types ──────────────────────────────────────────────────────────────

export interface OSCESetSummary {
  set_id: string;
  title: string;
  description: string;
  difficulty: string;
  total_stations: number;
}

export interface OSCEStartRequest {
  student_id: string;
  osce_set_id: string;
  language?: string;
}

export interface OSCEStartResponse {
  session_id: string;
  osce_set_id: string;
  osce_set_title: string;
  total_stations: number;
  first_station: OSCEStationResponse;
}

export interface OSCEStationResponse {
  station_id: string;
  station_number: number;
  title: string;
  time_limit_seconds: number;
  station_type: string;
  patient_scenario: string;
  task: string;
}

export interface OSCEAnswerRequest {
  answer: string;
  time_spent_seconds: number;
}

export interface ChecklistResult {
  item: string;
  category: string;
  met: boolean;
}

export interface OSCEStationResult {
  station_number: number;
  station_title: string;
  score: number;
  checklist_results: ChecklistResult[];
  feedback: string;
}

export interface OSCESummaryResponse {
  session_id: string;
  osce_set_title: string;
  total_score: number;
  station_results: OSCEStationResult[];
  strong_areas: string[];
  weak_areas: string[];
  recommendations: string[];
}

