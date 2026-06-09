"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import {
  api,
  type DashboardResponse,
  type SessionListItem,
} from "@/lib/api";
import {
  WeakTopicBarChart,
  ScoreTrendLineChart,
  TopicRadarChart,
} from "./PerformanceCharts";

const STUDENT_ID = "demo_user";

/* ── Skeleton placeholder ──────────────────────────────────────────── */
function Skeleton({ className = "" }: { className?: string }) {
  return (
    <div
      className={`animate-pulse bg-slate-200 rounded-lg ${className}`}
      aria-hidden
    />
  );
}

function StatCardSkeleton() {
  return (
    <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm flex flex-col gap-2">
      <Skeleton className="h-4 w-24" />
      <Skeleton className="h-10 w-20" />
    </div>
  );
}

/* ── Stat Card ─────────────────────────────────────────────────────── */
function StatCard({
  label,
  value,
  icon,
  accent = "text-slate-800",
}: {
  label: string;
  value: string | number;
  icon: string;
  accent?: string;
}) {
  return (
    <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm flex items-center justify-between hover:shadow-md transition-shadow">
      <div>
        <p className="text-xs text-slate-500 uppercase tracking-wider font-semibold mb-1">
          {label}
        </p>
        <p className={`text-3xl font-bold ${accent}`}>{value}</p>
      </div>
      <span className="text-4xl">{icon}</span>
    </div>
  );
}

/* ── Status Badge ──────────────────────────────────────────────────── */
function StatusBadge({ status }: { status: string }) {
  const isActive = status === "active";
  return (
    <span
      className={`inline-flex items-center gap-1 text-xs font-semibold px-2.5 py-1 rounded-full ${
        isActive
          ? "bg-emerald-100 text-emerald-700"
          : "bg-slate-100 text-slate-500"
      }`}
    >
      <span
        className={`w-1.5 h-1.5 rounded-full ${
          isActive ? "bg-emerald-500 animate-pulse" : "bg-slate-400"
        }`}
      />
      {isActive ? "Active" : "Completed"}
    </span>
  );
}

/* ── Difficulty Badge ──────────────────────────────────────────────── */
function DifficultyBadge({ difficulty }: { difficulty: string }) {
  const colors: Record<string, string> = {
    Beginner: "bg-green-100 text-green-700",
    Intermediate: "bg-amber-100 text-amber-700",
    Advanced: "bg-red-100 text-red-700",
  };
  return (
    <span
      className={`text-xs font-medium px-2 py-0.5 rounded-full ${
        colors[difficulty] ?? "bg-slate-100 text-slate-600"
      }`}
    >
      {difficulty}
    </span>
  );
}

/* ── Score Bar ──────────────────────────────────────────────────────── */
function ScoreBar({ score }: { score: number }) {
  const color =
    score >= 80
      ? "bg-emerald-500"
      : score >= 50
      ? "bg-amber-400"
      : "bg-red-400";
  return (
    <div className="flex items-center gap-2 min-w-[100px]">
      <div className="flex-1 h-2 bg-slate-100 rounded-full overflow-hidden">
        <div
          className={`h-full rounded-full transition-all duration-500 ${color}`}
          style={{ width: `${Math.min(score, 100)}%` }}
        />
      </div>
      <span className="text-sm font-semibold text-slate-600 w-8 text-right">
        {score}
      </span>
    </div>
  );
}

/* ── Main Page ─────────────────────────────────────────────────────── */
export default function DashboardPage() {
  const router = useRouter();
  const [data, setData] = useState<DashboardResponse | null>(null);
  const [error, setError] = useState("");
  const [resumingId, setResumingId] = useState<string | null>(null);

  useEffect(() => {
    api
      .getDashboard(STUDENT_ID)
      .then(setData)
      .catch((e: unknown) =>
        setError(e instanceof Error ? e.message : "Failed to load dashboard")
      );
  }, []);

  async function handleResume(session: SessionListItem) {
    setResumingId(session.session_id);
    try {
      const res = await api.resumeSession(session.session_id);
      router.push(
        `/simulation?session=${res.session_id}` +
          `&case=${encodeURIComponent(res.case_title)}` +
          `&q=${encodeURIComponent(res.question)}` +
          `&lang=${res.language}` +
          `&scenario=${encodeURIComponent(res.scenario_update)}` +
          `&step=${res.current_step}`
      );
    } catch {
      setError("Could not resume session.");
      setResumingId(null);
    }
  }

  /* ── Loading state ── */
  if (!data && !error) {
    return (
      <div className="flex flex-col gap-8 max-w-4xl mx-auto">
        <div className="flex items-center justify-between">
          <div>
            <Skeleton className="h-8 w-40 mb-2" />
            <Skeleton className="h-4 w-28" />
          </div>
          <Skeleton className="h-10 w-36 rounded-xl" />
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <StatCardSkeleton />
          <StatCardSkeleton />
          <StatCardSkeleton />
        </div>
        <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">
          {[1, 2, 3].map((i) => (
            <div key={i} className="flex gap-4 py-4">
              <Skeleton className="h-5 flex-1" />
              <Skeleton className="h-5 w-20" />
              <Skeleton className="h-5 w-16" />
            </div>
          ))}
        </div>
      </div>
    );
  }

  const scoreAccent =
    (data?.average_score ?? 0) >= 80
      ? "text-emerald-600"
      : (data?.average_score ?? 0) >= 50
      ? "text-amber-500"
      : "text-red-500";

  return (
    <div className="flex flex-col gap-8 max-w-4xl mx-auto">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-slate-800">Dashboard</h1>
          <p className="text-slate-500 text-sm mt-1">
            {data?.student_name ?? "Student"}
          </p>
        </div>
        <Link
          href="/"
          className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-5 py-2.5 rounded-xl text-sm transition-colors"
        >
          New Session →
        </Link>
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 rounded-xl px-4 py-3 text-sm">
          {error}
        </div>
      )}

      {/* Stat cards */}
      {data && (
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <StatCard
            label="Average Score"
            value={data.average_score}
            icon={data.average_score >= 80 ? "🏆" : data.average_score >= 50 ? "📈" : "📚"}
            accent={scoreAccent}
          />
          <StatCard
            label="Total Sessions"
            value={data.total_sessions}
            icon="🩺"
          />
          <StatCard
            label="Completed"
            value={data.completed_sessions}
            icon="✅"
          />
        </div>
      )}

      {/* Performance Charts */}
      {data && (
        <>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
            <ScoreTrendLineChart sessions={data.sessions} />
            <WeakTopicBarChart weakTopics={data.weak_topics} />
          </div>
          <TopicRadarChart sessions={data.sessions} />
        </>
      )}

      {/* Session history table */}
      {data && (
        <div className="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden">
          <div className="px-6 py-4 border-b border-slate-100">
            <h2 className="font-semibold text-slate-700">Session History</h2>
            <p className="text-slate-500 text-xs mt-0.5">
              All clinical simulation sessions
            </p>
          </div>

          {data.sessions.length === 0 ? (
            <div className="px-6 py-10 text-center text-slate-400">
              No sessions yet. Start your first clinical simulation!
            </div>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="text-left text-xs text-slate-500 uppercase tracking-wider border-b border-slate-100">
                    <th className="px-6 py-3 font-medium">Case</th>
                    <th className="px-4 py-3 font-medium">Topic</th>
                    <th className="px-4 py-3 font-medium">Level</th>
                    <th className="px-4 py-3 font-medium">Score</th>
                    <th className="px-4 py-3 font-medium">Status</th>
                    <th className="px-4 py-3 font-medium">Date</th>
                    <th className="px-4 py-3 font-medium" />
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-50">
                  {data.sessions.map((s) => (
                    <tr
                      key={s.session_id}
                      className="hover:bg-slate-50 transition-colors"
                    >
                      <td className="px-6 py-4 font-medium text-slate-700">
                        {s.case_title}
                      </td>
                      <td className="px-4 py-4 text-slate-600">{s.topic}</td>
                      <td className="px-4 py-4">
                        <DifficultyBadge difficulty={s.difficulty} />
                      </td>
                      <td className="px-4 py-4">
                        <ScoreBar score={s.total_score} />
                      </td>
                      <td className="px-4 py-4">
                        <StatusBadge status={s.status} />
                      </td>
                      <td className="px-4 py-4 text-slate-500 text-sm whitespace-nowrap">
                        {new Date(s.created_at).toLocaleDateString()}
                      </td>
                      <td className="px-4 py-4">
                        {s.status === "active" ? (
                          <button
                            onClick={() => handleResume(s)}
                            disabled={resumingId === s.session_id}
                            className="text-blue-600 hover:text-blue-700 font-medium text-xs disabled:opacity-50 whitespace-nowrap"
                          >
                            {resumingId === s.session_id
                              ? "Resuming…"
                              : "Resume →"}
                          </button>
                        ) : (
                          <Link
                            href={`/summary?session=${s.session_id}`}
                            className="text-slate-400 hover:text-blue-600 font-medium text-xs whitespace-nowrap"
                          >
                            View Summary
                          </Link>
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}

      {/* Weak topics */}
      {data && data.weak_topics.length > 0 && (
        <div className="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden">
          <div className="px-6 py-4 border-b border-slate-100">
            <h2 className="font-semibold text-slate-700">Weak Topics</h2>
            <p className="text-slate-500 text-xs mt-0.5">
              Topics where gaps have been detected across sessions
            </p>
          </div>
          <ul className="divide-y divide-slate-100">
            {data.weak_topics.map((t) => (
              <li
                key={t.topic}
                className="px-6 py-4 flex items-center justify-between hover:bg-slate-50 transition-colors"
              >
                <div>
                  <p className="font-medium text-slate-700">{t.topic}</p>
                  <p className="text-xs text-slate-500 mt-0.5">
                    Last seen: {t.last_seen}
                  </p>
                </div>
                <span className="bg-amber-100 text-amber-700 text-xs font-semibold px-2.5 py-1 rounded-full">
                  ×{t.frequency}
                </span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Recommended practice */}
      {data && data.weak_topics.length > 0 && (
        <div className="bg-blue-50 border border-blue-200 rounded-2xl p-6">
          <h2 className="font-semibold text-blue-800 mb-3">
            Recommended Practice
          </h2>
          <p className="text-slate-700 text-sm mb-4">
            Based on your weak topics, we recommend practising these areas:
          </p>
          <ul className="space-y-2">
            {data.weak_topics.slice(0, 3).map((t) => (
              <li key={t.topic} className="text-sm text-slate-700 flex gap-2">
                <span className="text-blue-500">→</span>
                {t.topic}
              </li>
            ))}
          </ul>
          <Link
            href="/"
            className="inline-block mt-4 bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold px-4 py-2 rounded-lg transition-colors"
          >
            Start a Focused Session →
          </Link>
        </div>
      )}
    </div>
  );
}
