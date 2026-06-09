"use client";

import { Suspense, useCallback, useEffect, useRef, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import {
  api,
  type OSCEStationResponse,
  type OSCEStationResult,
  type OSCESummaryResponse,
} from "@/lib/api";
import { StationTimer } from "./StationTimer";
import { VoiceInput } from "../../components/VoiceInput";
import { RichFeedback } from "../../simulation/RichFeedback";

/* ── Inner component with search params ─────────────────────────── */
function OSCEExamInner() {
  const router = useRouter();
  const params = useSearchParams();

  const sessionId = params.get("session") ?? "";
  const osceSetId = params.get("set") ?? "";
  const osceTitle = decodeURIComponent(params.get("title") ?? "OSCE");
  const totalStations = parseInt(params.get("total") ?? "4", 10);
  const lang = (params.get("lang") as "en" | "tr") || "en";

  const [currentStation, setCurrentStation] = useState<OSCEStationResponse | null>(null);
  const [stationNumber, setStationNumber] = useState(1);
  const [answer, setAnswer] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [stationResult, setStationResult] = useState<OSCEStationResult | null>(null);
  const [summary, setSummary] = useState<OSCESummaryResponse | null>(null);
  const [error, setError] = useState("");
  const timerStartRef = useRef<number>(Date.now());
  const voiceTranscriptRef = useRef<string>("");

  /* Load station */
  const loadStation = useCallback(
    async (num: number) => {
      try {
        const station = await api.getOSCEStation(sessionId, num);
        setCurrentStation(station);
        setStationNumber(num);
        setAnswer("");
        setStationResult(null);
        setError("");
        timerStartRef.current = Date.now();
        voiceTranscriptRef.current = "";
      } catch {
        setError("Failed to load station");
      }
    },
    [sessionId]
  );

  /* Initial load */
  useEffect(() => {
    if (sessionId) loadStation(1);
  }, [sessionId, loadStation]);

  /* Submit answer */
  const handleSubmit = useCallback(
    async (forceAnswer?: string) => {
      if (submitting) return;
      setSubmitting(true);
      setError("");

      const finalAnswer = forceAnswer ?? answer;
      const timeSpent = Math.round((Date.now() - timerStartRef.current) / 1000);

      try {
        const result = await api.submitOSCEAnswer(
          sessionId,
          stationNumber,
          finalAnswer || (lang === "tr" ? "Cevap verilmedi." : "No answer provided."),
          timeSpent
        );
        setStationResult(result);
      } catch {
        setError("Failed to submit answer");
      } finally {
        setSubmitting(false);
      }
    },
    [sessionId, stationNumber, answer, submitting, lang]
  );

  /* Time up handler */
  const handleTimeUp = useCallback(() => {
    handleSubmit(answer || (lang === "tr" ? "Süre doldu — cevap verilmedi." : "Time expired — no answer provided."));
  }, [handleSubmit, answer, lang]);

  /* Move to next station */
  const handleNext = useCallback(async () => {
    if (stationNumber >= totalStations) {
      // Show summary
      try {
        const s = await api.getOSCESummary(sessionId);
        setSummary(s);
      } catch {
        setError("Failed to load summary");
      }
    } else {
      loadStation(stationNumber + 1);
    }
  }, [stationNumber, totalStations, sessionId, loadStation]);

  /* Voice transcript handler */
  const handleVoiceTranscript = useCallback((text: string) => {
    voiceTranscriptRef.current = text;
    setAnswer(text);
  }, []);

  const t = {
    station: lang === "tr" ? "İstasyon" : "Station",
    of: lang === "tr" ? "/" : "of",
    patientScenario: lang === "tr" ? "Hasta Senaryosu" : "Patient Scenario",
    yourTask: lang === "tr" ? "Göreviniz" : "Your Task",
    answerPlaceholder:
      lang === "tr"
        ? "Cevabınızı buraya yazın veya mikrofon butonunu kullanarak söyleyin..."
        : "Type your answer here or use the microphone button to speak...",
    submit: lang === "tr" ? "Cevabı Gönder" : "Submit Answer",
    submitting: lang === "tr" ? "Değerlendiriliyor…" : "Evaluating…",
    nextStation: lang === "tr" ? "Sonraki İstasyon →" : "Next Station →",
    finish: lang === "tr" ? "Sınavı Bitir" : "Finish Exam",
    result: lang === "tr" ? "İstasyon Sonucu" : "Station Result",
    checklist: lang === "tr" ? "Kontrol Listesi" : "Checklist",
    feedback: lang === "tr" ? "Geri Bildirim" : "Feedback",
    summaryTitle: lang === "tr" ? "OSCE Özeti" : "OSCE Summary",
    dashboard: lang === "tr" ? "Dashboard'a Git" : "Go to Dashboard",
    strong: lang === "tr" ? "Güçlü Alanlar" : "Strong Areas",
    weak: lang === "tr" ? "Geliştirilecek Alanlar" : "Areas to Improve",
    recommendations: lang === "tr" ? "Öneriler" : "Recommendations",
  };

  const STATION_TYPE_ICONS: Record<string, string> = {
    history: "📋",
    physical_exam: "🩺",
    diagnosis: "🔬",
    management: "💊",
    communication: "🗣️",
  };

  /* ── Summary view ──────────────────────────────────────────────── */
  if (summary) {
    const scoreColor =
      summary.total_score >= 80
        ? "text-emerald-600"
        : summary.total_score >= 60
        ? "text-amber-600"
        : "text-red-600";

    return (
      <div className="max-w-3xl mx-auto py-8 flex flex-col gap-6">
        {/* Header */}
        <div className="text-center">
          <div className="inline-flex items-center gap-2 bg-purple-100 text-purple-700 text-sm font-semibold px-4 py-1.5 rounded-full mb-3">
            🎓 {t.summaryTitle}
          </div>
          <h1 className="text-3xl font-bold text-slate-800 mb-1">
            {summary.osce_set_title}
          </h1>
          <p className={`text-5xl font-extrabold mt-4 ${scoreColor}`}>
            {summary.total_score}%
          </p>
        </div>

        {/* Station cards */}
        <div className="flex flex-col gap-3">
          {(summary.station_results ?? []).map((sr) => (
            <div
              key={sr.station_number}
              className="bg-white border border-slate-200 rounded-xl p-5 shadow-sm"
            >
              <div className="flex items-center justify-between mb-3">
                <span className="font-semibold text-slate-700">
                  {sr.station_title}
                </span>
                <span
                  className={`text-lg font-bold ${
                    sr.score >= 70 ? "text-emerald-600" : "text-red-500"
                  }`}
                >
                  {sr.score}%
                </span>
              </div>
              {/* Checklist mini */}
              <div className="flex flex-wrap gap-1.5">
                {(sr.checklist_results ?? []).map((c, i) => (
                  <span
                    key={i}
                    className={`text-xs px-2 py-0.5 rounded-full ${
                      c.met
                        ? "bg-emerald-100 text-emerald-700"
                        : "bg-red-50 text-red-600"
                    }`}
                  >
                    {c.met ? "✓" : "✗"} {c.item}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>

        {/* Strong / Weak */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {(summary.strong_areas ?? []).length > 0 && (
            <div className="bg-emerald-50 border border-emerald-200 rounded-xl p-4">
              <h3 className="font-semibold text-emerald-700 mb-2">
                💪 {t.strong}
              </h3>
              <ul className="text-sm text-emerald-800 space-y-1">
                {(summary.strong_areas ?? []).map((a, i) => (
                  <li key={i}>✓ {a}</li>
                ))}
              </ul>
            </div>
          )}
          {(summary.weak_areas ?? []).length > 0 && (
            <div className="bg-amber-50 border border-amber-200 rounded-xl p-4">
              <h3 className="font-semibold text-amber-700 mb-2">
                📚 {t.weak}
              </h3>
              <ul className="text-sm text-amber-800 space-y-1">
                {(summary.weak_areas ?? []).map((a, i) => (
                  <li key={i}>→ {a}</li>
                ))}
              </ul>
            </div>
          )}
        </div>

        {/* Recommendations */}
        {(summary.recommendations ?? []).length > 0 && (
          <div className="bg-blue-50 border border-blue-200 rounded-xl p-4">
            <h3 className="font-semibold text-blue-700 mb-2">
              💡 {t.recommendations}
            </h3>
            <ul className="text-sm text-blue-800 space-y-1">
              {(summary.recommendations ?? []).map((r, i) => (
                <li key={i}>• {r}</li>
              ))}
            </ul>
          </div>
        )}

        <button
          onClick={() => router.push("/dashboard")}
          className="mx-auto bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 px-8 rounded-xl transition-colors"
        >
          {t.dashboard}
        </button>
      </div>
    );
  }

  /* ── Station view ──────────────────────────────────────────────── */
  return (
    <div className="max-w-3xl mx-auto py-6 flex flex-col gap-5">
      {/* Top bar: progress + timer */}
      <div className="flex items-center justify-between bg-white border border-slate-200 rounded-2xl shadow-sm px-6 py-4">
        <div>
          <h2 className="text-lg font-bold text-slate-800">{osceTitle}</h2>
          <p className="text-sm text-slate-600 font-medium">
            {t.station} {stationNumber} {t.of} {totalStations}
          </p>
          {/* Progress dots */}
          <div className="flex gap-2 mt-2">
            {Array.from({ length: totalStations }, (_, i) => (
              <div
                key={i}
                className={`w-3 h-3 rounded-full transition-colors ${
                  i + 1 < stationNumber
                    ? "bg-emerald-400"
                    : i + 1 === stationNumber
                    ? stationResult
                      ? "bg-emerald-400"
                      : "bg-purple-500 ring-2 ring-purple-200"
                    : "bg-slate-200"
                }`}
              />
            ))}
          </div>
        </div>

        {currentStation && !stationResult && (
          <StationTimer
            key={stationNumber}
            totalSeconds={currentStation.time_limit_seconds}
            onTimeUp={handleTimeUp}
            paused={!!stationResult}
          />
        )}
      </div>

      {/* Station content */}
      {currentStation && !stationResult && (
        <>
          {/* Station type badge */}
          <div className="flex items-center gap-2">
            <span className="text-2xl">
              {STATION_TYPE_ICONS[currentStation.station_type] || "📄"}
            </span>
            <span className="bg-purple-100 text-purple-700 text-sm font-semibold px-3 py-1 rounded-full">
              {currentStation.title}
            </span>
          </div>

          {/* Patient scenario */}
          <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm">
            <h3 className="text-sm font-semibold text-slate-600 uppercase tracking-wide mb-3">
              {t.patientScenario}
            </h3>
            <p className="text-slate-700 leading-relaxed whitespace-pre-line">
              {currentStation.patient_scenario}
            </p>
          </div>

          {/* Task */}
          <div className="bg-purple-50 border border-purple-200 rounded-xl p-6">
            <h3 className="text-sm font-semibold text-purple-700 uppercase tracking-wide mb-3">
              {t.yourTask}
            </h3>
            <p className="text-slate-700 leading-relaxed whitespace-pre-line">
              {currentStation.task}
            </p>
          </div>

          {/* Answer area */}
          <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm">
            <div className="flex items-center gap-2 mb-3">
              <textarea
                className="flex-1 bg-white border border-slate-300 rounded-lg p-4 text-slate-700 min-h-[140px] resize-y focus:outline-none focus:ring-2 focus:ring-purple-500"
                placeholder={t.answerPlaceholder}
                value={answer}
                onChange={(e) => setAnswer(e.target.value)}
                disabled={submitting}
              />
              <div className="flex flex-col items-center gap-2">
                <VoiceInput
                  onTranscript={handleVoiceTranscript}
                  language={lang}
                  disabled={submitting}
                />
              </div>
            </div>

            {error && <p className="text-red-500 text-sm mb-3">{error}</p>}

            <button
              onClick={() => handleSubmit()}
              disabled={submitting || !answer.trim()}
              className="w-full bg-purple-600 hover:bg-purple-700 disabled:bg-purple-300 text-white font-semibold py-3 rounded-xl transition-colors"
            >
              {submitting ? t.submitting : t.submit}
            </button>
          </div>
        </>
      )}

      {/* Station result */}
      {stationResult && (
        <div className="flex flex-col gap-4">
          {/* Score header */}
          <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm text-center">
            <h3 className="text-sm font-semibold text-slate-600 uppercase tracking-wide mb-2">
              {t.result}
            </h3>
            <span
              className={`text-4xl font-extrabold ${
                stationResult.score >= 70 ? "text-emerald-600" : "text-red-500"
              }`}
            >
              {stationResult.score}%
            </span>
          </div>

          {/* Checklist */}
          <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm">
            <h3 className="font-semibold text-slate-700 mb-3">{t.checklist}</h3>
            <div className="grid gap-2">
              {(stationResult.checklist_results ?? []).map((c, i) => (
                <div
                  key={i}
                  className={`flex items-center gap-2 text-sm p-2 rounded-lg ${
                    c.met
                      ? "bg-emerald-50 text-emerald-800"
                      : "bg-red-50 text-red-700"
                  }`}
                >
                  <span className="text-base">
                    {c.met ? "✅" : "❌"}
                  </span>
                  <span className="flex-1">{c.item}</span>
                  <span className="text-xs bg-white/80 px-2 py-0.5 rounded-full text-slate-600 font-medium">
                    {c.category}
                  </span>
                </div>
              ))}
            </div>
          </div>

          {/* Feedback */}
          <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm">
            <h3 className="font-semibold text-slate-700 mb-3">{t.feedback}</h3>
            <RichFeedback content={stationResult.feedback} />
          </div>

          {/* Next button */}
          <button
            onClick={handleNext}
            className="w-full bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 rounded-xl transition-colors text-base"
          >
            {stationNumber >= totalStations ? t.finish : t.nextStation}
          </button>
        </div>
      )}
    </div>
  );
}

/* ── Page wrapper with Suspense ──────────────────────────────────── */
export default function OSCEExamPage() {
  return (
    <Suspense
      fallback={
        <div className="flex justify-center py-20 text-slate-400 text-lg">
          Loading OSCE...
        </div>
      }
    >
      <OSCEExamInner />
    </Suspense>
  );
}
