"use client";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  LineElement,
  RadialLinearScale,
  Filler,
  Tooltip,
  Legend,
  type ChartOptions,
} from "chart.js";
import { Bar, Line, Radar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  LineElement,
  RadialLinearScale,
  Filler,
  Tooltip,
  Legend
);

/* ── Types (re-used from api.ts to avoid circular deps) ────────────── */
interface WeakTopicItem {
  topic: string;
  frequency: number;
  last_seen: string;
}

interface SessionListItem {
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

/* ── Color palette ─────────────────────────────────────────────────── */
const COLORS = {
  blue: "rgba(59, 130, 246, 1)",
  blueFaded: "rgba(59, 130, 246, 0.15)",
  emerald: "rgba(16, 185, 129, 1)",
  emeraldFaded: "rgba(16, 185, 129, 0.15)",
  amber: "rgba(245, 158, 11, 1)",
  amberFaded: "rgba(245, 158, 11, 0.25)",
  red: "rgba(239, 68, 68, 1)",
  redFaded: "rgba(239, 68, 68, 0.25)",
  purple: "rgba(139, 92, 246, 1)",
  purpleFaded: "rgba(139, 92, 246, 0.15)",
  slate200: "rgba(226, 232, 240, 1)",
  slate400: "rgba(148, 163, 184, 1)",
};

function frequencyColor(freq: number): string {
  if (freq >= 5) return COLORS.red;
  if (freq >= 3) return COLORS.amber;
  return COLORS.blue;
}

function frequencyBgColor(freq: number): string {
  if (freq >= 5) return COLORS.redFaded;
  if (freq >= 3) return COLORS.amberFaded;
  return COLORS.blueFaded;
}

/* ── 1. Weak Topic Frequency Bar Chart ─────────────────────────────── */
export function WeakTopicBarChart({
  weakTopics,
}: {
  weakTopics: WeakTopicItem[];
}) {
  if (weakTopics.length === 0) return null;

  const sorted = [...weakTopics].sort((a, b) => b.frequency - a.frequency);
  const labels = sorted.map((t) =>
    t.topic.length > 28 ? t.topic.slice(0, 26) + "…" : t.topic
  );

  const data = {
    labels,
    datasets: [
      {
        label: "Frequency",
        data: sorted.map((t) => t.frequency),
        backgroundColor: sorted.map((t) => frequencyBgColor(t.frequency)),
        borderColor: sorted.map((t) => frequencyColor(t.frequency)),
        borderWidth: 1.5,
        borderRadius: 6,
        barPercentage: 0.7,
      },
    ],
  };

  const options: ChartOptions<"bar"> = {
    responsive: true,
    maintainAspectRatio: false,
    indexAxis: "y" as const,
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: "rgba(15, 23, 42, 0.9)",
        titleFont: { size: 13, weight: "bold" },
        bodyFont: { size: 12 },
        padding: 10,
        cornerRadius: 8,
        callbacks: {
          title: (items) => sorted[items[0].dataIndex]?.topic ?? "",
          label: (item) => `Seen ${item.raw} time${(item.raw as number) > 1 ? "s" : ""}`,
        },
      },
    },
    scales: {
      x: {
        beginAtZero: true,
        ticks: { stepSize: 1, color: COLORS.slate400, font: { size: 11 } },
        grid: { color: "rgba(226, 232, 240, 0.5)" },
      },
      y: {
        ticks: { color: COLORS.slate400, font: { size: 11 } },
        grid: { display: false },
      },
    },
  };

  return (
    <div className="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden">
      <div className="px-6 py-4 border-b border-slate-100">
        <h2 className="font-semibold text-slate-700 flex items-center gap-2">
          <span className="text-lg">📊</span> Weak Topic Frequency
        </h2>
        <p className="text-slate-500 text-xs mt-0.5">
          How often each weak topic has been detected
        </p>
      </div>
      <div className="px-6 py-4" style={{ height: Math.max(weakTopics.length * 44, 160) }}>
        <Bar data={data} options={options} />
      </div>
    </div>
  );
}

/* ── 2. Score Trend Line Chart ─────────────────────────────────────── */
export function ScoreTrendLineChart({
  sessions,
}: {
  sessions: SessionListItem[];
}) {
  const completed = sessions
    .filter((s) => s.status === "completed")
    .sort(
      (a, b) =>
        new Date(a.created_at).getTime() - new Date(b.created_at).getTime()
    );

  if (completed.length < 2) return null;

  const labels = completed.map((s) =>
    new Date(s.created_at).toLocaleDateString(undefined, {
      month: "short",
      day: "numeric",
    })
  );

  const pointColors = completed.map((s) =>
    s.total_score >= 80
      ? COLORS.emerald
      : s.total_score >= 50
      ? COLORS.amber
      : COLORS.red
  );

  const data = {
    labels,
    datasets: [
      {
        label: "Score",
        data: completed.map((s) => s.total_score),
        borderColor: COLORS.blue,
        backgroundColor: COLORS.blueFaded,
        fill: true,
        tension: 0.35,
        pointBackgroundColor: pointColors,
        pointBorderColor: pointColors,
        pointRadius: 5,
        pointHoverRadius: 7,
        borderWidth: 2.5,
      },
    ],
  };

  const options: ChartOptions<"line"> = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: "rgba(15, 23, 42, 0.9)",
        titleFont: { size: 13, weight: "bold" },
        bodyFont: { size: 12 },
        padding: 10,
        cornerRadius: 8,
        callbacks: {
          title: (items) => {
            const idx = items[0].dataIndex;
            return completed[idx]?.case_title ?? "";
          },
          label: (item) => `Score: ${item.raw}/100`,
        },
      },
    },
    scales: {
      y: {
        min: 0,
        max: 100,
        ticks: { stepSize: 20, color: COLORS.slate400, font: { size: 11 } },
        grid: { color: "rgba(226, 232, 240, 0.5)" },
      },
      x: {
        ticks: { color: COLORS.slate400, font: { size: 11 } },
        grid: { display: false },
      },
    },
  };

  return (
    <div className="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden">
      <div className="px-6 py-4 border-b border-slate-100">
        <h2 className="font-semibold text-slate-700 flex items-center gap-2">
          <span className="text-lg">📈</span> Score Trend
        </h2>
        <p className="text-slate-500 text-xs mt-0.5">
          Your score progression across completed sessions
        </p>
      </div>
      <div className="px-6 py-4" style={{ height: 260 }}>
        <Line data={data} options={options} />
      </div>
    </div>
  );
}

/* ── 3. Topic Radar Chart ──────────────────────────────────────────── */
export function TopicRadarChart({
  sessions,
}: {
  sessions: SessionListItem[];
}) {
  const completed = sessions.filter((s) => s.status === "completed");
  if (completed.length < 2) return null;

  // Group by topic, compute average score
  const topicMap = new Map<string, { total: number; count: number }>();
  for (const s of completed) {
    const entry = topicMap.get(s.topic) ?? { total: 0, count: 0 };
    entry.total += s.total_score;
    entry.count += 1;
    topicMap.set(s.topic, entry);
  }

  if (topicMap.size < 3) return null; // Need 3+ topics for a meaningful radar

  const topicLabels = Array.from(topicMap.keys()).map((t) =>
    t.length > 20 ? t.slice(0, 18) + "…" : t
  );
  const avgScores = Array.from(topicMap.values()).map((e) =>
    Math.round(e.total / e.count)
  );

  const data = {
    labels: topicLabels,
    datasets: [
      {
        label: "Avg Score",
        data: avgScores,
        backgroundColor: COLORS.purpleFaded,
        borderColor: COLORS.purple,
        borderWidth: 2,
        pointBackgroundColor: COLORS.purple,
        pointBorderColor: "#fff",
        pointRadius: 4,
        pointHoverRadius: 6,
      },
    ],
  };

  const options: ChartOptions<"radar"> = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: "rgba(15, 23, 42, 0.9)",
        titleFont: { size: 13, weight: "bold" },
        bodyFont: { size: 12 },
        padding: 10,
        cornerRadius: 8,
        callbacks: {
          label: (item) => `Avg: ${item.raw}/100`,
        },
      },
    },
    scales: {
      r: {
        min: 0,
        max: 100,
        ticks: {
          stepSize: 20,
          color: COLORS.slate400,
          backdropColor: "transparent",
          font: { size: 10 },
        },
        pointLabels: {
          color: COLORS.slate400,
          font: { size: 11 },
        },
        grid: { color: "rgba(226, 232, 240, 0.5)" },
        angleLines: { color: "rgba(226, 232, 240, 0.5)" },
      },
    },
  };

  return (
    <div className="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden">
      <div className="px-6 py-4 border-b border-slate-100">
        <h2 className="font-semibold text-slate-700 flex items-center gap-2">
          <span className="text-lg">🎯</span> Topic Performance
        </h2>
        <p className="text-slate-500 text-xs mt-0.5">
          Average score per clinical topic
        </p>
      </div>
      <div className="px-6 py-4 flex justify-center" style={{ height: 300 }}>
        <Radar data={data} options={options} />
      </div>
    </div>
  );
}
