"use client";

import { useState, Suspense, useEffect } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { api, type EvaluationResponse } from "@/lib/api";
import { RichFeedback } from "./RichFeedback";
import { VoiceInput } from "../components/VoiceInput";

type Lang = "en" | "tr";

const I18N: Record<Lang, Record<string, string>> = {
  en: {
    activeCaseLabel: "Active Case",
    stepLabel: "Step",
    clinicalUpdateLabel: "Clinical Update",
    answerLabel: "Your Answer",
    answerPlaceholder: "Describe your clinical approach step by step…",
    submitBtn: "Submit Answer →",
    evaluatingBtn: "Evaluating…",
    scoreLabel: "Score",
    feedbackLabel: "Feedback",
    correctLabel: "✓ Correct",
    missingLabel: "⚠ Missing",
    unsafeLabel: "⛔ Unsafe Reasoning",
    weakTopicsLabel: "Weak Topics Detected",
    nextScenarioLabel: "What Happens Next",
    nextQuestionBtn: "Next Question →",
    summaryBtn: "View Summary →",
    emptyAnswerError: "Please write an answer before submitting.",
    patientMonitor: "Bedside Monitor",
    hrLabel: "HR",
    bpLabel: "BP",
    spo2Label: "SpO2",
    rrLabel: "RR",
    tempLabel: "TEMP",
  },
  tr: {
    activeCaseLabel: "Aktif Vaka",
    stepLabel: "Basamak",
    clinicalUpdateLabel: "Klinik Gelişme",
    answerLabel: "Cevabınız",
    answerPlaceholder: "Klinik yaklaşımınızı adım adım açıklayın…",
    submitBtn: "Gönder →",
    evaluatingBtn: "Değerlendiriliyor…",
    scoreLabel: "Puan",
    feedbackLabel: "Geri Bildirim",
    correctLabel: "✓ Doğru",
    missingLabel: "⚠ Eksik",
    unsafeLabel: "⛔ Güvensiz Yaklaşım",
    weakTopicsLabel: "Tespit Edilen Zayıf Konular",
    nextScenarioLabel: "Sonraki Gelişme",
    nextQuestionBtn: "Sonraki Soru →",
    summaryBtn: "Özeti Görüntüle →",
    emptyAnswerError: "Göndermeden önce bir cevap yazın.",
    patientMonitor: "Hasta Monitörü",
    hrLabel: "KAH",
    bpLabel: "KAN BASINCI",
    spo2Label: "SpO2",
    rrLabel: "SS",
    tempLabel: "ATEŞ",
  },
};

function SimulationContent() {
  const router = useRouter();
  const params = useSearchParams();

  const sessionId      = params.get("session")  ?? "";
  const caseTitle      = params.get("case")      ?? "Clinical Case";
  const initialQuestion = params.get("q")        ?? "";
  const rawLang        = params.get("lang")       ?? "en";
  const lang: Lang     = rawLang === "tr" ? "tr" : "en";
  const initialScenario = params.get("scenario") ?? "";
  const initialStep     = parseInt(params.get("step") ?? "1", 10) || 1;

  const tx = I18N[lang];

  const [currentScenario, setCurrentScenario] = useState(initialScenario);
  const [currentQuestion, setCurrentQuestion]  = useState(initialQuestion);
  const [answer, setAnswer]                    = useState("");
  const [evaluation, setEvaluation]            = useState<EvaluationResponse | null>(null);
  const [loading, setLoading]                  = useState(false);
  const [error, setError]                      = useState("");
  const [step, setStep]                        = useState(initialStep);
  // After evaluation, show next scenario before the Next button triggers the question transition
  const [pendingScenario, setPendingScenario]  = useState("");
  const [vitals, setVitals]                    = useState<Record<string, any> | null>(null);

  useEffect(() => {
    if (sessionId) {
      api.resumeSession(sessionId)
        .then((data) => {
          if (data.vitals) {
            setVitals(data.vitals);
          }
          if (data.scenario_update) {
            setCurrentScenario(data.scenario_update);
          }
          if (data.question) {
            setCurrentQuestion(data.question);
          }
        })
        .catch(console.error);
    }
  }, [sessionId]);

  async function handleSubmit() {
    if (!answer.trim()) { setError(tx.emptyAnswerError); return; }
    setError("");
    setLoading(true);
    try {
      const ev = await api.submitAnswer(sessionId, answer);
      setEvaluation(ev);
      setPendingScenario(ev.next_scenario_update ?? "");
      if (ev.vitals) {
        setVitals(ev.vitals);
      }
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : "Submission failed");
    } finally {
      setLoading(false);
    }
  }

  function handleNext() {
    if (!evaluation) return;
    if (evaluation.session_complete) {
      router.push(`/summary?session=${sessionId}`);
      return;
    }
    setCurrentScenario(pendingScenario);
    setCurrentQuestion(evaluation.next_question);
    setAnswer("");
    setEvaluation(null);
    setPendingScenario("");
    setStep((s) => s + 1);
  }

  const scoreColor =
    (evaluation?.score ?? 0) >= 80 ? "text-emerald-600"
    : (evaluation?.score ?? 0) >= 50 ? "text-amber-500"
    : "text-red-500";

  return (
    <div className="flex flex-col gap-6 max-w-2xl mx-auto">
      {/* Case header */}
      <div className="flex items-center justify-between">
        <div>
          <p className="text-xs text-slate-500 uppercase tracking-wider font-semibold">
            {tx.activeCaseLabel}
          </p>
          <h1 className="text-2xl font-bold text-slate-800">{caseTitle}</h1>
        </div>
        <span className="bg-blue-100 text-blue-700 text-sm font-semibold px-3 py-1 rounded-full">
          {tx.stepLabel} {step}
        </span>
      </div>

      {/* Bedside Vitals Monitor */}
      {vitals && (
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-lg flex flex-col gap-4 font-mono select-none">
          <div className="flex items-center justify-between border-b border-slate-850 pb-2">
            <span className="text-emerald-400 text-xs font-bold tracking-wider animate-pulse flex items-center gap-1.5">
              <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block animate-ping"></span>
              🏥 {tx.patientMonitor} — ACTIVE
            </span>
            <span className="text-slate-500 text-xs font-bold uppercase">
              Bedside Unit
            </span>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-5 gap-4">
            {/* HR */}
            <div className="bg-slate-950/60 rounded-xl p-3 border border-slate-800/80 flex flex-col justify-between">
              <span className="text-[10px] font-bold text-emerald-500 tracking-wide">{tx.hrLabel} (bpm)</span>
              <span className={`text-3xl font-extrabold tracking-tight mt-1 ${
                vitals.heart_rate > 150 || vitals.heart_rate < 50 ? "text-red-500 animate-pulse" : "text-emerald-400"
              }`}>
                {vitals.heart_rate}
              </span>
            </div>

            {/* BP */}
            <div className="bg-slate-950/60 rounded-xl p-3 border border-slate-800/80 flex flex-col justify-between">
              <span className="text-[10px] font-bold text-cyan-400 tracking-wide">{tx.bpLabel}</span>
              <span className="text-2xl font-extrabold tracking-tight text-cyan-400 mt-1.5">
                {vitals.blood_pressure}
              </span>
            </div>

            {/* SpO2 */}
            <div className="bg-slate-950/60 rounded-xl p-3 border border-slate-800/80 flex flex-col justify-between">
              <span className="text-[10px] font-bold text-blue-400 tracking-wide">{tx.spo2Label} (%)</span>
              <span className={`text-3xl font-extrabold tracking-tight mt-1 ${
                vitals.spo2 < 92 ? "text-red-500 animate-pulse" : "text-blue-400"
              }`}>
                {vitals.spo2}
              </span>
            </div>

            {/* RR */}
            <div className="bg-slate-950/60 rounded-xl p-3 border border-slate-800/80 flex flex-col justify-between">
              <span className="text-[10px] font-bold text-amber-400 tracking-wide">{tx.rrLabel} (/min)</span>
              <span className="text-3xl font-extrabold tracking-tight text-amber-400 mt-1">
                {vitals.respiratory_rate}
              </span>
            </div>

            {/* Temp */}
            <div className="bg-slate-950/60 rounded-xl p-3 border border-slate-800/80 flex flex-col justify-between col-span-2 sm:col-span-1">
              <span className="text-[10px] font-bold text-slate-300 tracking-wide">{tx.tempLabel} (°C)</span>
              <span className="text-3xl font-extrabold tracking-tight text-slate-100 mt-1">
                {vitals.temperature}
              </span>
            </div>
          </div>

          {/* Patient Status Description */}
          {vitals.status_description && (
            <div className="border-t border-slate-800/60 pt-3.5 mt-1">
              <span className="text-[10px] font-bold text-slate-500 tracking-wider block mb-1">
                {lang === "tr" ? "HASTA DURUMU / KLİNİK BULGULAR" : "PATIENT STATUS / CLINICAL FINDINGS"}
              </span>
              <p className="text-sm text-slate-300 leading-relaxed font-sans font-medium">
                {vitals.status_description}
              </p>
            </div>
          )}
        </div>
      )}

      {/* Clinical scenario update card */}
      {currentScenario && (
        <div className="bg-sky-50 border border-sky-200 rounded-xl p-5">
          <p className="text-xs font-semibold text-sky-600 uppercase mb-2">
            {tx.clinicalUpdateLabel}
          </p>
          <p className="text-slate-700 leading-relaxed whitespace-pre-line">{currentScenario}</p>
        </div>
      )}

      {/* Question card */}
      <div className="bg-blue-50 border border-blue-200 rounded-xl p-5">
        <p className="text-slate-700 leading-relaxed">{currentQuestion}</p>
      </div>

      {/* Answer area (hidden when evaluation shown) */}
      {!evaluation && (
        <div className="flex flex-col gap-3">
          <label className="text-sm font-semibold text-slate-700">{tx.answerLabel}</label>
          <div className="flex gap-2">
            <textarea
              className="flex-1 bg-white border border-slate-300 rounded-xl px-4 py-3 text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500 min-h-[120px] resize-none"
              placeholder={tx.answerPlaceholder}
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
            />
            <VoiceInput
              onTranscript={(text) => setAnswer(text)}
              language={lang}
              disabled={loading}
            />
          </div>
          {error && <p className="text-red-500 text-sm">{error}</p>}
          <button
            onClick={handleSubmit}
            disabled={loading}
            className="self-end bg-blue-600 hover:bg-blue-700 disabled:bg-blue-300 text-white font-semibold px-6 py-2.5 rounded-xl transition-colors"
          >
            {loading ? tx.evaluatingBtn : tx.submitBtn}
          </button>
        </div>
      )}

      {/* Feedback panel */}
      {evaluation && (
        <div className="flex flex-col gap-4">
          {/* Score */}
          <div className="bg-white border border-slate-200 rounded-xl p-5 flex items-center justify-between shadow-sm">
            <span className="font-semibold text-slate-700">{tx.scoreLabel}</span>
            <span className={`text-3xl font-bold ${scoreColor}`}>
              {evaluation.score}
              <span className="text-base font-normal text-slate-500">/100</span>
            </span>
          </div>

          {/* Feedback text — rich Markdown rendering */}
          <div className="bg-white border border-slate-200 rounded-xl p-5 shadow-sm">
            <h3 className="font-semibold text-slate-700 mb-2">{tx.feedbackLabel}</h3>
            <RichFeedback content={evaluation.feedback} />
          </div>

          {/* Correct / Missing */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {(evaluation.correct_points ?? []).length > 0 && (
              <div className="bg-emerald-50 border border-emerald-200 rounded-xl p-4">
                <p className="text-xs font-semibold text-emerald-700 uppercase mb-2">{tx.correctLabel}</p>
                <ul className="space-y-1">
                  {(evaluation.correct_points ?? []).map((p) => <li key={p} className="text-sm text-slate-700">• {p}</li>)}
                </ul>
              </div>
            )}
            {(evaluation.missing_points ?? []).length > 0 && (
              <div className="bg-amber-50 border border-amber-200 rounded-xl p-4">
                <p className="text-xs font-semibold text-amber-700 uppercase mb-2">{tx.missingLabel}</p>
                <ul className="space-y-1">
                  {(evaluation.missing_points ?? []).map((p) => <li key={p} className="text-sm text-slate-700">• {p}</li>)}
                </ul>
              </div>
            )}
          </div>

          {(evaluation.unsafe_points ?? []).length > 0 && (
            <div className="bg-red-50 border border-red-300 rounded-xl p-4">
              <p className="text-xs font-semibold text-red-700 uppercase mb-2">{tx.unsafeLabel}</p>
              <ul className="space-y-1">
                {(evaluation.unsafe_points ?? []).map((p) => <li key={p} className="text-sm text-red-700">• {p}</li>)}
              </ul>
            </div>
          )}

          {(evaluation.weak_topics ?? []).length > 0 && (
            <div className="bg-slate-100 border border-slate-200 rounded-xl p-4">
              <p className="text-xs font-semibold text-slate-600 uppercase mb-2">{tx.weakTopicsLabel}</p>
              <div className="flex flex-wrap gap-2">
                {(evaluation.weak_topics ?? []).map((t) => (
                  <span key={t} className="bg-white border border-slate-300 text-slate-700 text-xs font-medium px-2.5 py-1 rounded-full">{t}</span>
                ))}
              </div>
            </div>
          )}

          {/* Next scenario preview (shown before user clicks Next) */}
          {!evaluation.session_complete && pendingScenario && (
            <div className="bg-sky-50 border border-sky-200 rounded-xl p-5">
              <p className="text-xs font-semibold text-sky-600 uppercase mb-2">{tx.nextScenarioLabel}</p>
              <p className="text-slate-700 leading-relaxed">{pendingScenario}</p>
            </div>
          )}

          <button
            onClick={handleNext}
            className="self-end bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-2.5 rounded-xl transition-colors"
          >
            {evaluation.session_complete ? tx.summaryBtn : tx.nextQuestionBtn}
          </button>
        </div>
      )}
    </div>
  );
}

export default function SimulationPage() {
  return (
    <Suspense fallback={<div className="text-slate-400">Loading case…</div>}>
      <SimulationContent />
    </Suspense>
  );
}
