"use client";

import { useEffect, useState, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import { api, type SessionSummary } from "@/lib/api";

function SummaryContent() {
  const params = useSearchParams();
  const sessionId = params.get("session") ?? "";
  const [summary, setSummary] = useState<SessionSummary | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!sessionId) return;
    api.getSummary(sessionId).then(setSummary).catch((e: unknown) =>
      setError(e instanceof Error ? e.message : "Failed to load summary")
    );
  }, [sessionId]);

  if (error) return <p className="text-red-500">{error}</p>;
  if (!summary) return <p className="text-slate-400">Loading summary…</p>;

  const scoreColor =
    summary.total_score >= 80
      ? "text-emerald-600"
      : summary.total_score >= 50
      ? "text-amber-500"
      : "text-red-500";

  return (
    <div className="flex flex-col gap-6 max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold text-slate-800">Session Summary</h1>

      {/* Score */}
      <div className="bg-white border border-slate-200 rounded-2xl p-6 flex items-center justify-between shadow-sm">
        <div>
          <p className="text-sm text-slate-500 font-medium mb-1">Overall Score</p>
          <p className={`text-5xl font-bold ${scoreColor}`}>
            {summary.total_score}
            <span className="text-lg font-normal text-slate-500">/100</span>
          </p>
        </div>
        <div className="text-5xl">
          {summary.total_score >= 80 ? "🏆" : summary.total_score >= 50 ? "📈" : "📚"}
        </div>
      </div>

      {/* Strong / Weak topics */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {(summary.strong_topics ?? []).length > 0 && (
          <div className="bg-emerald-50 border border-emerald-200 rounded-xl p-5">
            <h3 className="text-xs font-semibold text-emerald-700 uppercase mb-3">Strong Topics</h3>
            <ul className="space-y-1.5">
              {(summary.strong_topics ?? []).map((t) => (
                <li key={t} className="text-sm text-slate-700 flex gap-2">
                  <span className="text-emerald-500">✓</span>{t}
                </li>
              ))}
            </ul>
          </div>
        )}
        {(summary.weak_topics ?? []).length > 0 && (
          <div className="bg-amber-50 border border-amber-200 rounded-xl p-5">
            <h3 className="text-xs font-semibold text-amber-700 uppercase mb-3">Weak Topics</h3>
            <ul className="space-y-1.5">
              {(summary.weak_topics ?? []).map((t) => (
                <li key={t} className="text-sm text-slate-700 flex gap-2">
                  <span className="text-amber-500">⚠</span>{t}
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>

      {/* Recommendations */}
      <div className="bg-white border border-slate-200 rounded-xl p-5 shadow-sm">
        <h3 className="font-semibold text-slate-700 mb-3">Recommendations</h3>
        <ul className="space-y-2">
          {(summary.recommendations ?? []).map((r) => (
            <li key={r} className="text-sm text-slate-600 flex gap-2">
              <span className="text-blue-500">→</span>{r}
            </li>
          ))}
        </ul>
      </div>

      {/* Recommended next case */}
      <div className="bg-blue-50 border border-blue-200 rounded-xl p-5">
        <p className="text-xs font-semibold text-blue-600 uppercase mb-1">Recommended Next Case</p>
        <p className="text-slate-700 font-medium">{summary.recommended_next_case}</p>
      </div>

      {/* Actions */}
      <div className="flex gap-3">
        <Link
          href="/"
          className="flex-1 text-center bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-xl transition-colors"
        >
          Start New Case →
        </Link>
        <Link
          href="/dashboard"
          className="flex-1 text-center bg-white hover:bg-slate-50 border border-slate-300 text-slate-700 font-semibold py-3 rounded-xl transition-colors"
        >
          View Dashboard
        </Link>
      </div>
    </div>
  );
}

export default function SummaryPage() {
  return (
    <Suspense fallback={<div className="text-slate-400">Loading summary…</div>}>
      <SummaryContent />
    </Suspense>
  );
}
