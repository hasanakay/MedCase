import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "MedCase Agent — Clinical Reasoning Tutor",
  description:
    "Autonomous clinical reasoning practice for medical students. Educational use only.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={`${inter.className} bg-slate-50 min-h-screen`}>
        {/* Top disclaimer bar */}
        <div className="bg-blue-700 text-white text-sm text-center py-2 px-4 font-medium tracking-wide">
          ⚕️ This tool is for medical education and simulated clinical reasoning
          practice only. It does not provide real patient diagnosis or treatment.
        </div>

        {/* Navigation */}
        <header className="bg-white border-b border-slate-200 shadow-sm">
          <div className="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
            <a href="/" className="flex items-center gap-2">
              <span className="text-blue-700 text-xl font-bold tracking-tight">
                MedCase<span className="text-emerald-500">Agent</span>
              </span>
            </a>
            <div className="flex items-center gap-4">
              <a
                href="/osce"
                className="text-sm text-purple-700 hover:text-purple-900 font-semibold transition-colors flex items-center gap-1"
              >
                🏥 OSCE
              </a>
              <a
                href="/dashboard"
                className="text-sm text-slate-700 hover:text-blue-700 font-semibold transition-colors"
              >
                Dashboard
              </a>
            </div>
          </div>
        </header>

        <main className="max-w-5xl mx-auto px-4 py-8">{children}</main>
      </body>
    </html>
  );
}
