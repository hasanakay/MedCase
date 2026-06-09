"use client";

import { useState, useEffect, useCallback, useRef } from "react";

interface StationTimerProps {
  /** Total seconds for this station */
  totalSeconds: number;
  /** Called when time runs out */
  onTimeUp: () => void;
  /** Whether the timer is paused */
  paused?: boolean;
}

export function StationTimer({
  totalSeconds,
  onTimeUp,
  paused = false,
}: StationTimerProps) {
  const [remaining, setRemaining] = useState(totalSeconds);
  const onTimeUpRef = useRef(onTimeUp);
  onTimeUpRef.current = onTimeUp;

  useEffect(() => {
    setRemaining(totalSeconds);
  }, [totalSeconds]);

  useEffect(() => {
    if (paused || remaining <= 0) return;

    const interval = setInterval(() => {
      setRemaining((prev) => {
        if (prev <= 1) {
          clearInterval(interval);
          onTimeUpRef.current();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [paused, remaining <= 0]); // eslint-disable-line react-hooks/exhaustive-deps

  const minutes = Math.floor(remaining / 60);
  const seconds = remaining % 60;
  const progress = remaining / totalSeconds;
  const isWarning = remaining <= 60;
  const isCritical = remaining <= 10;

  /* SVG circular progress */
  const size = 88;
  const strokeWidth = 5;
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference * (1 - progress);

  const progressColor = isCritical
    ? "stroke-red-500"
    : isWarning
    ? "stroke-amber-500"
    : "stroke-blue-500";

  const textColor = isCritical
    ? "text-red-600"
    : isWarning
    ? "text-amber-600"
    : "text-slate-700";

  return (
    <div
      className={`station-timer relative flex flex-col items-center ${
        isCritical ? "animate-pulse" : ""
      }`}
    >
      <div className="relative" style={{ width: size, height: size }}>
        {/* Background circle */}
        <svg
          className="absolute inset-0"
          width={size}
          height={size}
          viewBox={`0 0 ${size} ${size}`}
        >
          <circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            fill="none"
            stroke="currentColor"
            strokeWidth={strokeWidth}
            className="text-slate-100"
          />
          {/* Progress arc */}
          <circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            fill="none"
            strokeWidth={strokeWidth}
            strokeLinecap="round"
            className={`${progressColor} transition-all duration-1000 ease-linear`}
            strokeDasharray={circumference}
            strokeDashoffset={offset}
            transform={`rotate(-90 ${size / 2} ${size / 2})`}
          />
        </svg>

        {/* Time text */}
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className={`text-xl font-bold tabular-nums ${textColor}`}>
            {String(minutes).padStart(2, "0")}:{String(seconds).padStart(2, "0")}
          </span>
        </div>
      </div>

      {/* Label */}
      <span
        className={`text-xs font-semibold mt-1 ${
          isCritical ? "text-red-500" : isWarning ? "text-amber-500" : "text-slate-500"
        }`}
      >
        {isCritical ? "⚠️ Time's up!" : isWarning ? "⏰ Hurry!" : "Time Left"}
      </span>
    </div>
  );
}
