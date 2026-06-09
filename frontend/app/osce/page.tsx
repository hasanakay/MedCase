"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { api, type OSCESetSummary } from "@/lib/api";

const STUDENT_ID = "demo_user";

const STATION_TYPE_ICONS: Record<string, string> = {
  history: "📋",
  physical_exam: "🩺",
  diagnosis: "🔬",
  management: "💊",
  communication: "🗣️",
};

export default function OSCEStartPage() {
  const router = useRouter();
  const [sets, setSets] = useState<OSCESetSummary[]>([]);
  const [selectedSet, setSelectedSet] = useState("");
  const [language, setLanguage] = useState<"en" | "tr">("en");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    api
      .getOSCESets(language)
      .then(setSets)
      .catch(() => setError("Failed to load OSCE sets"));
  }, [language]);

  async function handleStart() {
    if (!selectedSet) {
      setError(
        language === "tr" ? "Lütfen bir OSCE seti seçin." : "Please select an OSCE set."
      );
      return;
    }
    setError("");
    setLoading(true);
    try {
      const res = await api.startOSCE({
        student_id: STUDENT_ID,
        osce_set_id: selectedSet,
        language,
      });
      router.push(
        `/osce/exam?session=${res.session_id}` +
          `&set=${encodeURIComponent(res.osce_set_id)}` +
          `&title=${encodeURIComponent(res.osce_set_title)}` +
          `&total=${res.total_stations}` +
          `&lang=${language}`
      );
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : "Failed to start OSCE");
    } finally {
      setLoading(false);
    }
  }

  const t = {
    title: language === "tr" ? "OSCE Sınavı" : "OSCE Examination",
    subtitle:
      language === "tr"
        ? "Zamanlı istasyonlar ile yapılandırılmış klinik sınav simülasyonu"
        : "Structured clinical exam simulation with timed stations",
    selectLabel: language === "tr" ? "OSCE Seti Seçin" : "Select OSCE Set",
    selectPlaceholder: language === "tr" ? "— Set seçin —" : "— Choose a set —",
    langLabel: language === "tr" ? "Dil" : "Language",
    startBtn: language === "tr" ? "OSCE Sınavını Başlat →" : "Start OSCE Exam →",
    loadingBtn: language === "tr" ? "Başlatılıyor…" : "Starting…",
    whatIsOSCE:
      language === "tr"
        ? "OSCE (Objective Structured Clinical Examination), tıp eğitiminde kullanılan yapılandırılmış klinik yetkinlik sınavıdır. Her istasyonda belirli bir süre içinde klinik görevleri tamamlamanız gerekir."
        : "OSCE (Objective Structured Clinical Examination) is a structured clinical competency exam used in medical education. At each station, you must complete clinical tasks within a set time limit.",
  };

  const selectedSetData = sets.find((s) => s.set_id === selectedSet);

  return (
    <div className="flex flex-col items-center gap-10 py-12">
      {/* Hero */}
      <div className="text-center max-w-2xl">
        <div className="inline-flex items-center gap-2 bg-purple-100 text-purple-700 text-sm font-semibold px-4 py-1.5 rounded-full mb-4">
          🏥 OSCE Mode
        </div>
        <h1 className="text-4xl font-bold text-slate-800 mb-3">{t.title}</h1>
        <p className="text-slate-600 text-lg leading-relaxed">{t.subtitle}</p>
      </div>

      {/* Info card */}
      <div className="bg-purple-50 border border-purple-200 rounded-2xl p-6 max-w-md w-full">
        <h3 className="font-semibold text-purple-800 mb-2 flex items-center gap-2">
          <span>ℹ️</span> {language === "tr" ? "OSCE Nedir?" : "What is OSCE?"}
        </h3>
        <p className="text-sm text-slate-700 leading-relaxed">{t.whatIsOSCE}</p>
        <div className="flex flex-wrap gap-2 mt-4">
          {Object.entries(STATION_TYPE_ICONS).map(([type, icon]) => (
            <span
              key={type}
              className="inline-flex items-center gap-1 text-xs bg-white border border-purple-200 px-2.5 py-1 rounded-full text-slate-700 font-medium"
            >
              {icon} {type.replace("_", " ")}
            </span>
          ))}
        </div>
      </div>

      {/* Start card */}
      <div className="bg-white rounded-2xl shadow-sm border border-slate-200 w-full max-w-md p-8 flex flex-col gap-6">
        <h2 className="text-xl font-semibold text-slate-700">
          {language === "tr" ? "OSCE Oturumu Başlat" : "Start OSCE Session"}
        </h2>

        {/* Language toggle */}
        <div className="flex flex-col gap-1.5">
          <label className="text-sm font-semibold text-slate-700">{t.langLabel}</label>
          <div className="flex gap-3">
            {(["en", "tr"] as const).map((l) => (
              <button
                key={l}
                onClick={() => setLanguage(l)}
                className={`flex-1 py-2 rounded-lg text-sm font-medium border transition-colors ${
                  language === l
                    ? "bg-purple-600 border-purple-600 text-white"
                    : "bg-white border-slate-300 text-slate-600 hover:border-purple-400"
                }`}
              >
                {l === "en" ? "🇬🇧 English" : "🇹🇷 Türkçe"}
              </button>
            ))}
          </div>
        </div>

        {/* OSCE Set selector */}
        <div className="flex flex-col gap-1.5">
          <label className="text-sm font-semibold text-slate-700">{t.selectLabel}</label>
          <select
            className="bg-white border border-slate-300 rounded-lg px-3 py-2 text-slate-800 focus:outline-none focus:ring-2 focus:ring-purple-500"
            value={selectedSet}
            onChange={(e) => setSelectedSet(e.target.value)}
          >
            <option value="">{t.selectPlaceholder}</option>
            {sets.map((s) => (
              <option key={s.set_id} value={s.set_id}>
                {s.title} ({s.total_stations} stations • {s.difficulty})
              </option>
            ))}
          </select>
        </div>

        {/* Selected set details */}
        {selectedSetData && (
          <div className="bg-slate-50 border border-slate-200 rounded-xl p-4">
            <p className="text-sm text-slate-700">{selectedSetData.description}</p>
            <div className="flex gap-3 mt-3">
              <span className="text-xs bg-purple-100 text-purple-700 px-2 py-0.5 rounded-full font-medium">
                {selectedSetData.total_stations} Stations
              </span>
              <span className="text-xs bg-amber-100 text-amber-700 px-2 py-0.5 rounded-full font-medium">
                {selectedSetData.difficulty}
              </span>
              <span className="text-xs bg-blue-100 text-blue-700 px-2 py-0.5 rounded-full font-medium">
                ⏱ 8 min/station
              </span>
            </div>
          </div>
        )}

        {error && <p className="text-red-500 text-sm">{error}</p>}

        <button
          onClick={handleStart}
          disabled={loading}
          className="w-full bg-purple-600 hover:bg-purple-700 disabled:bg-purple-300 text-white font-semibold py-3 rounded-xl transition-colors text-base"
        >
          {loading ? t.loadingBtn : t.startBtn}
        </button>
      </div>
    </div>
  );
}
