"use client";

import React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import type { Components } from "react-markdown";

/* ── Custom Markdown renderers ─────────────────────────────────────── */
const mdComponents: Components = {
  /* Headings */
  h1: ({ children }) => (
    <h3 className="text-lg font-bold text-slate-800 mt-4 mb-2">{children}</h3>
  ),
  h2: ({ children }) => (
    <h4 className="text-base font-bold text-slate-700 mt-3 mb-1.5">{children}</h4>
  ),
  h3: ({ children }) => (
    <h5 className="text-sm font-bold text-slate-700 mt-2 mb-1">{children}</h5>
  ),

  /* Paragraphs */
  p: ({ children }) => (
    <p className="text-slate-700 leading-relaxed mb-2 last:mb-0">{children}</p>
  ),

  /* Bold — used for medical term highlighting */
  strong: ({ children }) => (
    <strong className="font-semibold text-slate-800 bg-blue-50 px-1 py-0.5 rounded">
      {children}
    </strong>
  ),

  /* Italic */
  em: ({ children }) => (
    <em className="text-slate-600 italic">{children}</em>
  ),

  /* Inline code — medical term / dosage highlights */
  code: ({ children, className }) => {
    // Block code gets a className from remark, inline doesn't
    if (className) {
      return (
        <code className="block bg-slate-50 border border-slate-200 rounded-lg p-3 text-sm font-mono text-slate-700 my-2 overflow-x-auto">
          {children}
        </code>
      );
    }
    return (
      <code className="bg-emerald-50 text-emerald-800 px-1.5 py-0.5 rounded text-sm font-medium border border-emerald-200">
        {children}
      </code>
    );
  },

  /* Lists */
  ul: ({ children }) => (
    <ul className="space-y-1.5 my-2 ml-1">{children}</ul>
  ),
  ol: ({ children }) => (
    <ol className="space-y-1.5 my-2 ml-1 list-decimal list-inside">{children}</ol>
  ),
  li: ({ children }) => (
    <li className="text-sm text-slate-700 flex gap-2 items-start">
      <span className="text-blue-500 mt-0.5 shrink-0">•</span>
      <span>{children}</span>
    </li>
  ),

  /* Block quote — used for references / important notes */
  blockquote: ({ children }) => (
    <blockquote className="border-l-3 border-blue-400 bg-blue-50 pl-4 py-2 pr-3 rounded-r-lg my-2 text-sm text-slate-700 italic">
      {children}
    </blockquote>
  ),

  /* Horizontal rule */
  hr: () => <hr className="border-slate-200 my-3" />,

  /* Links — for source references */
  a: ({ href, children }) => (
    <a
      href={href}
      target="_blank"
      rel="noopener noreferrer"
      className="text-blue-600 hover:text-blue-700 underline underline-offset-2 decoration-blue-300 hover:decoration-blue-500 transition-colors"
    >
      {children}
    </a>
  ),

  /* Tables */
  table: ({ children }) => (
    <div className="overflow-x-auto my-2">
      <table className="w-full text-sm border-collapse">{children}</table>
    </div>
  ),
  th: ({ children }) => (
    <th className="text-left text-xs font-semibold text-slate-600 uppercase tracking-wider px-3 py-2 border-b border-slate-200 bg-slate-50">
      {children}
    </th>
  ),
  td: ({ children }) => (
    <td className="px-3 py-2 border-b border-slate-100 text-slate-700">
      {children}
    </td>
  ),
};

/* ── Rich Feedback Component ───────────────────────────────────────── */
interface RichFeedbackProps {
  /** Markdown-formatted feedback string from AI */
  content: string;
  /** Optional class name */
  className?: string;
}

export function RichFeedback({ content, className = "" }: RichFeedbackProps) {
  if (!content) return null;

  return (
    <div className={`rich-feedback ${className}`}>
      <ReactMarkdown remarkPlugins={[remarkGfm]} components={mdComponents}>
        {content}
      </ReactMarkdown>
    </div>
  );
}

/* ── Reference Section ─────────────────────────────────────────────── */
interface ReferenceItem {
  title: string;
  url?: string;
}

export function ReferenceSection({
  references,
}: {
  references: ReferenceItem[];
}) {
  if (!references || references.length === 0) return null;

  return (
    <div className="mt-3 pt-3 border-t border-slate-200">
      <p className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-2">
        📚 References
      </p>
      <ul className="space-y-1">
        {references.map((ref, i) => (
          <li key={i} className="text-xs text-slate-500 flex gap-1.5 items-start">
            <span className="text-slate-400 shrink-0">[{i + 1}]</span>
            {ref.url ? (
              <a
                href={ref.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-500 hover:text-blue-600 underline underline-offset-2 decoration-blue-200"
              >
                {ref.title}
              </a>
            ) : (
              <span>{ref.title}</span>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
