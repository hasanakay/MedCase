"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { api, type TopicsResponse } from "@/lib/api";

const STUDENT_ID = "demo_user";

export default function HomePage() {
  const router = useRouter();
  const [data, setData] = useState<TopicsResponse | null>(null);
  const [topic, setTopic] = useState("");
  const [difficulty, setDifficulty] = useState("Intermediate");
  const [language, setLanguage] = useState<"en" | "tr">("en");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    api.getTopics().then(setData).catch(console.error);
  }, []);

  async function handleStart() {
    if (!topic) { setError(language === "tr" ? "Lütfen bir konu seçin." : "Please select a topic."); return; }
    setError("");
    setLoading(true);
    try {
      const session = await api.startSession({
        student_id: STUDENT_ID,
        topic,
        difficulty,
        language,
      });
      router.push(
        `/simulation?session=${session.session_id}` +
        `&case=${encodeURIComponent(session.case_title)}` +
        `&q=${encodeURIComponent(session.question)}` +
        `&lang=${language}` +
        `&scenario=${encodeURIComponent(session.scenario_update)}`
      );
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : (language === "tr" ? "Oturum başlatılamadı." : "Failed to start session"));
    } finally {
      setLoading(false);
    }
  }

  const t = {
    title:      language === "tr" ? "Klinik Akıl Yürütme Simülatörü"   : "Clinical Reasoning Simulator",
    subtitle:   language === "tr"
      ? "Uyarlanabilir klinik vakalar üzerinde çalışın, yapay zeka destekli geri bildirim alın ve zayıf konularınızı takip edin."
      : "Practice adaptive clinical cases, receive AI-powered feedback, and track your weak topics across sessions.",
    startTitle: language === "tr" ? "Oturum Başlat"                     : "Start a Session",
    topicLabel: language === "tr" ? "Konu"                              : "Topic",
    topicPlaceholder: language === "tr" ? "— Konu seçin —"              : "— Select a topic —",
    diffLabel:  language === "tr" ? "Zorluk"                            : "Difficulty",
    startBtn:   language === "tr" ? "Vaka Simülasyonunu Başlat →"       : "Start Case Simulation →",
    loadingBtn: language === "tr" ? "Başlatılıyor…"                     : "Starting…",
    langLabel:  language === "tr" ? "Dil"                               : "Language",
  };

  const features = language === "tr"
    ? [
        { icon: "🩺", title: "Uyarlanabilir Vakalar",         desc: "Sorular performansınıza göre gerçek zamanlı olarak ayarlanır." },
        { icon: "📊", title: "Zayıf Konu Takibi",             desc: "Yapay zeka örüntüleri algılar ve boşluklarınıza öncelik verir." },
        { icon: "✅", title: "Yapılandırılmış Geri Bildirim", desc: "Neyi doğru yaptığınızı ve neleri gözden geçirmeniz gerektiğini tam olarak öğrenin." },
      ]
    : [
        { icon: "🩺", title: "Adaptive Cases",      desc: "Questions adjust to your performance in real time." },
        { icon: "📊", title: "Weak Topic Tracking", desc: "AI detects patterns and prioritises your gaps." },
        { icon: "✅", title: "Structured Feedback", desc: "Know exactly what you got right and what to review." },
      ];

  return (
    <div className="flex flex-col items-center gap-10 py-12">
      {/* Hero */}
      <div className="text-center max-w-2xl">
        <h1 className="text-4xl font-bold text-slate-800 mb-3">{t.title}</h1>
        <p className="text-slate-600 text-lg leading-relaxed">{t.subtitle}</p>
      </div>

      {/* Start card */}
      <div className="bg-white rounded-2xl shadow-sm border border-slate-200 w-full max-w-md p-8 flex flex-col gap-6">
        <h2 className="text-xl font-semibold text-slate-700">{t.startTitle}</h2>

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
                    ? "bg-blue-600 border-blue-600 text-white"
                    : "bg-white border-slate-300 text-slate-600 hover:border-blue-400"
                }`}
              >
                {l === "en" ? "🇬🇧 English" : "🇹🇷 Türkçe"}
              </button>
            ))}
          </div>
        </div>

        {/* Topic */}
        <div className="flex flex-col gap-1.5">
          <label className="text-sm font-semibold text-slate-700">{t.topicLabel}</label>
          <select
            className="bg-white border border-slate-300 rounded-lg px-3 py-2 text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
          >
            <option value="">{t.topicPlaceholder}</option>
            {(data?.topics ?? []).map((tp) => (
              <option key={tp} value={tp}>{tp}</option>
            ))}
          </select>
        </div>

        {/* Difficulty */}
        <div className="flex flex-col gap-1.5">
          <label className="text-sm font-semibold text-slate-700">{t.diffLabel}</label>
          <div className="flex gap-3">
            {(data?.difficulties ?? ["Beginner", "Intermediate", "Advanced"]).map((d) => (
              <button
                key={d}
                onClick={() => setDifficulty(d)}
                className={`flex-1 py-2 rounded-lg text-sm font-medium border transition-colors ${
                  difficulty === d
                    ? "bg-blue-600 border-blue-600 text-white"
                    : "bg-white border-slate-300 text-slate-600 hover:border-blue-400"
                }`}
              >
                {d}
              </button>
            ))}
          </div>
        </div>

        {error && <p className="text-red-500 text-sm">{error}</p>}

        <button
          onClick={handleStart}
          disabled={loading}
          className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-blue-300 text-white font-semibold py-3 rounded-xl transition-colors text-base"
        >
          {loading ? t.loadingBtn : t.startBtn}
        </button>
      </div>

      {/* Feature grid */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 w-full max-w-2xl text-center">
        {features.map((f) => (
          <div key={f.title} className="bg-white border border-slate-200 rounded-xl p-5 shadow-sm">
            <div className="text-3xl mb-2">{f.icon}</div>
            <div className="font-semibold text-slate-800 mb-1">{f.title}</div>
            <div className="text-slate-600 text-sm leading-relaxed">{f.desc}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
