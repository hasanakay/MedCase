"use client";

/* eslint-disable @typescript-eslint/no-explicit-any */

import { useState, useEffect, useCallback, useRef } from "react";

/* ── Web Speech API type shim ──────────────────────────────────── */
interface SpeechRecognitionEvent {
  results: SpeechRecognitionResultList;
}
interface SpeechRecognitionResultList {
  length: number;
  [index: number]: SpeechRecognitionResult;
}
interface SpeechRecognitionResult {
  [index: number]: SpeechRecognitionAlternative;
  isFinal: boolean;
}
interface SpeechRecognitionAlternative {
  transcript: string;
  confidence: number;
}

interface SpeechRecognitionInstance {
  continuous: boolean;
  interimResults: boolean;
  lang: string;
  onresult: ((event: SpeechRecognitionEvent) => void) | null;
  onerror: (() => void) | null;
  onend: (() => void) | null;
  start: () => void;
  stop: () => void;
}

/* ── Types ─────────────────────────────────────────────────────────── */
interface VoiceInputProps {
  /** Called with the latest transcript text */
  onTranscript: (text: string) => void;
  /** Language: "en" or "tr" */
  language?: "en" | "tr";
  /** Optional class for positioning */
  className?: string;
  /** Disabled state */
  disabled?: boolean;
}

type Status = "idle" | "listening" | "unsupported";

const LANG_MAP: Record<string, string> = {
  en: "en-US",
  tr: "tr-TR",
};

/* ── Component ─────────────────────────────────────────────────────── */
export function VoiceInput({
  onTranscript,
  language = "en",
  className = "",
  disabled = false,
}: VoiceInputProps) {
  const [status, setStatus] = useState<Status>("idle");
  const [supported, setSupported] = useState(true);
  const recognitionRef = useRef<SpeechRecognitionInstance | null>(null);

  /* Check browser support */
  useEffect(() => {
    const win = window as any;
    const SpeechRecognitionCtor = win.SpeechRecognition || win.webkitSpeechRecognition;

    if (!SpeechRecognitionCtor) {
      setSupported(false);
      setStatus("unsupported");
      return;
    }

    const recognition: SpeechRecognitionInstance = new SpeechRecognitionCtor();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = LANG_MAP[language] || "en-US";

    recognition.onresult = (event: SpeechRecognitionEvent) => {
      let transcript = "";
      for (let i = 0; i < event.results.length; i++) {
        transcript += event.results[i][0].transcript;
      }
      onTranscript(transcript);
    };

    recognition.onerror = () => {
      setStatus("idle");
    };

    recognition.onend = () => {
      setStatus("idle");
    };

    recognitionRef.current = recognition;

    return () => {
      try {
        recognition.stop();
      } catch {
        /* ignore */
      }
    };
  }, [language]); // eslint-disable-line react-hooks/exhaustive-deps

  /* Update language dynamically */
  useEffect(() => {
    if (recognitionRef.current) {
      recognitionRef.current.lang = LANG_MAP[language] || "en-US";
    }
  }, [language]);

  const toggle = useCallback(() => {
    if (!recognitionRef.current || disabled) return;

    if (status === "listening") {
      recognitionRef.current.stop();
      setStatus("idle");
    } else {
      try {
        recognitionRef.current.start();
        setStatus("listening");
      } catch {
        /* already started */
      }
    }
  }, [status, disabled]);

  if (!supported) return null;

  const isListening = status === "listening";

  return (
    <button
      type="button"
      onClick={toggle}
      disabled={disabled}
      title={isListening ? "Stop recording" : "Start voice input"}
      className={`
        voice-input-btn
        relative flex items-center justify-center
        w-10 h-10 rounded-xl border transition-all duration-200
        ${
          isListening
            ? "bg-red-50 border-red-300 text-red-600 shadow-md shadow-red-100"
            : "bg-slate-50 border-slate-200 text-slate-400 hover:text-blue-600 hover:border-blue-300 hover:bg-blue-50"
        }
        disabled:opacity-40 disabled:cursor-not-allowed
        ${className}
      `}
    >
      {/* Pulse ring when listening */}
      {isListening && (
        <span className="absolute inset-0 rounded-xl border-2 border-red-400 animate-ping opacity-30" />
      )}

      {/* Microphone icon */}
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth={2}
        strokeLinecap="round"
        strokeLinejoin="round"
        className="w-5 h-5"
      >
        <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z" />
        <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
        <line x1="12" x2="12" y1="19" y2="22" />
      </svg>
    </button>
  );
}
