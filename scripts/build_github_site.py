#!/usr/bin/env python3
"""
Build the unified static GitHub website and PWA bundle for both:
  1. GoodNotes Pro (from ../goodnotes-pro-app/web)
  2. Oxbridge Maths Interviewer AI (from ./web)

Outputs self-contained single-file apps and PWA assets into BOTH the repository
root and ./docs so the site works cleanly on GitHub Pages (/ or /docs or gh-pages)
and instant GitHub HTML preview (htmlpreview.github.io).
"""

import json
import shutil
from pathlib import Path

OXBRIDGE_DIR = Path(__file__).resolve().parent.parent
WORKSPACE_ROOT = OXBRIDGE_DIR.parent
GOODNOTES_DIR = WORKSPACE_ROOT / "goodnotes-pro-app"

TARGETS = [OXBRIDGE_DIR, OXBRIDGE_DIR / "docs"]


def build_inlined_html(html_path: Path, data_js_path: Path, script_tag_target: str) -> str:
    """Inline an external preset/question JS file directly into an HTML app."""
    html = html_path.read_text(encoding="utf-8")
    if script_tag_target not in html:
        raise RuntimeError(f"Could not find {script_tag_target!r} in {html_path}")
    raw_js = data_js_path.read_text(encoding="utf-8")
    safe_js = raw_js.replace("</script>", "<\\/script>")
    return html.replace(script_tag_target, f"<script>\n{safe_js}\n</script>", 1)


def to_subdir_variant(html: str, replacements: list[tuple[str, str]]) -> str:
    """Adjust relative hub/sibling links and SW registration for nested /app/ URLs."""
    out = html
    for old, new in replacements:
        out = out.replace(old, new)
    return out


def make_hub_html() -> str:
    """Render the responsive App Suite Hub landing page."""
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
  <meta name="apple-mobile-web-app-title" content="Study Studio" />
  <meta name="mobile-web-app-capable" content="yes" />
  <meta name="theme-color" content="#0b1120" />
  <link rel="manifest" href="manifest.json" />
  <link rel="apple-touch-icon" href="icon.png" />
  <title>GoodNotes Pro &amp; Oxbridge Maths AI — Web Studio</title>
  <style>
    :root {
      --bg: #0b1120;
      --surface: #131c31;
      --surface-2: #1a2642;
      --border: rgba(148, 163, 184, 0.2);
      --text: #f8fafc;
      --muted: #94a3b8;
      --blue: #38bdf8;
      --blue-strong: #0284c7;
      --gold: #f59e0b;
      --green: #10b981;
    }
    * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
    body {
      margin: 0;
      min-height: 100dvh;
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif;
      background: radial-gradient(circle at 15% 15%, #172554 0%, var(--bg) 52%, #070b14 100%);
      color: var(--text);
      padding: max(24px, env(safe-area-inset-top)) 20px max(32px, env(safe-area-inset-bottom));
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .wrap {
      width: 100%;
      max-width: 1040px;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }
    .hero {
      text-align: center;
      padding: 18px 12px 4px;
    }
    .pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: 999px;
      background: rgba(56, 189, 248, 0.14);
      border: 1px solid rgba(56, 189, 248, 0.35);
      color: var(--blue);
      font-size: 13px;
      font-weight: 600;
      margin-bottom: 14px;
    }
    h1 {
      margin: 0 0 10px;
      font-size: clamp(28px, 4.5vw, 44px);
      letter-spacing: -0.02em;
      line-height: 1.15;
    }
    .subtitle {
      margin: 0 auto;
      max-width: 680px;
      color: var(--muted);
      font-size: 16px;
      line-height: 1.55;
    }
    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
    }
    .card {
      background: rgba(19, 28, 49, 0.9);
      border: 1px solid var(--border);
      border-radius: 22px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      box-shadow: 0 18px 40px rgba(0, 0, 0, 0.35);
      backdrop-filter: blur(12px);
    }
    .card-head {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .app-icon {
      width: 56px;
      height: 56px;
      border-radius: 15px;
      display: grid;
      place-items: center;
      font-size: 28px;
      flex-shrink: 0;
    }
    .icon-gn { background: linear-gradient(135deg, #0284c7, #38bdf8); }
    .icon-ox { background: linear-gradient(135deg, #1d4ed8, #7c3aed); }
    .card h2 { margin: 0; font-size: 21px; }
    .card-tag { font-size: 12.5px; color: var(--blue); font-weight: 600; margin-top: 2px; }
    .card p { margin: 0; color: var(--muted); font-size: 14px; line-height: 1.55; }
    .feature-list {
      margin: 0;
      padding: 0 0 0 18px;
      color: #cbd5e1;
      font-size: 13.5px;
      line-height: 1.65;
      flex: 1;
    }
    .actions {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 6px;
    }
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 12px 18px;
      border-radius: 12px;
      font-weight: 700;
      font-size: 14.5px;
      text-decoration: none;
      border: 1px solid transparent;
      cursor: pointer;
      transition: transform 0.12s, filter 0.12s;
    }
    .btn:hover { transform: translateY(-1px); filter: brightness(1.06); }
    .btn-primary { background: linear-gradient(135deg, var(--blue-strong), var(--blue)); color: #04121f; flex: 1; }
    .btn-gold { background: linear-gradient(135deg, #d97706, var(--gold)); color: #1f1300; flex: 1; }
    .btn-ghost { background: var(--surface-2); border-color: var(--border); color: var(--text); }
    .guide {
      background: rgba(19, 28, 49, 0.72);
      border: 1px solid rgba(16, 185, 129, 0.3);
      border-radius: 18px;
      padding: 20px 22px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
    }
    .guide h3 {
      margin: 0 0 6px;
      font-size: 15px;
      color: var(--green);
    }
    .guide p {
      margin: 0;
      font-size: 13.5px;
      color: #cbd5e1;
      line-height: 1.55;
    }
    .footer {
      text-align: center;
      color: var(--muted);
      font-size: 12.5px;
      padding-top: 4px;
    }
  </style>
</head>
<body>
  <div class="wrap">
    <section class="hero">
      <div class="pill">🌐 Live Web Apps • No .IPA Sideloading or Certificates Needed</div>
      <h1>iPad Study &amp; Note-Taking Suite</h1>
      <p class="subtitle">
        Run both apps straight from your browser or add them to your iPad Home Screen for a full-screen, offline-ready, zero-delay Apple Pencil experience.
      </p>
    </section>

    <section class="cards">
      <article class="card">
        <div class="card-head">
          <div class="app-icon icon-gn">✒️</div>
          <div>
            <h2>GoodNotes Pro</h2>
            <div class="card-tag">Zero-Delay Apple Pencil Note Studio</div>
          </div>
        </div>
        <p>Full Goodnotes feature suite running directly in Safari or Chrome with IndexedDB storage and Google Drive backup.</p>
        <ul class="feature-list">
          <li>0-delay 3-layer canvas (<code>pointerrawupdate</code>, coalesced &amp; predicted strokes)</li>
          <li>Fountain / Ball / Brush pens, Highlighter under ink, Eraser modes, Draw &amp; Hold shapes, Scribble-to-Erase &amp; Circle-to-Lasso</li>
          <li>Elements, Sticky Notes, Text Box, Study Tape, Zoom Window, Ruler, Laser Pointer, Timer &amp; Stroke-Synced Audio</li>
          <li>Study Sets (spaced repetition), Split View, Document Tabs, PDF Import/Export, Ask AI &amp; Google Drive Backup</li>
        </ul>
        <div class="actions">
          <a class="btn btn-primary" href="goodnotes.html">🚀 Launch GoodNotes Pro</a>
          <a class="btn btn-ghost" href="goodnotes/">PWA App</a>
        </div>
      </article>

      <article class="card">
        <div class="card-head">
          <div class="app-icon icon-ox">🎓</div>
          <div>
            <h2>Oxbridge Maths Interviewer AI</h2>
            <div class="card-tag">85 Problems • Live Gemini Vision Canvas</div>
          </div>
        </div>
        <p>Interactive Oxford &amp; Cambridge Mathematics admissions mock interviewer with an Apple Pencil scratchpad.</p>
        <ul class="feature-list">
          <li>85 curated Oxbridge interview &amp; STEP-style problems rendered cleanly with LaTeX (KaTeX)</li>
          <li>Multi-page grid / dot / lined / blank Apple Pencil workspace with palm rejection</li>
          <li>Auto-See Gemini Vision canvas tutor, progressive 3-stage hints &amp; full worked solutions</li>
          <li>Interview timer, spoken voice responses, and interactive follow-up tutor chat</li>
        </ul>
        <div class="actions">
          <a class="btn btn-gold" href="interview.html">🚀 Launch Oxbridge Interviewer</a>
          <a class="btn btn-ghost" href="interview/">PWA App</a>
        </div>
      </article>
    </section>

    <section class="guide">
      <div>
        <h3>1. Instant Browser Use</h3>
        <p>Tap either launch button above. All notebooks, handwriting strokes, flashcards, settings, and API keys save locally in your browser (plus Google Drive backup in GoodNotes Pro).</p>
      </div>
      <div>
        <h3>2. Full-Screen iPad Home Screen Install</h3>
        <p>Open the app in <strong>Safari</strong> on iPad/iPhone, tap the <strong>Share (⬆️)</strong> button, and choose <strong>Add to Home Screen</strong>. It runs full-screen without Safari toolbars or 7-day .ipa expiry.</p>
      </div>
      <div>
        <h3>3. Switch Anytime</h3>
        <p>Both apps include a topbar shortcut to jump directly between <strong>GoodNotes Pro</strong> and the <strong>Oxbridge Interviewer</strong>.</p>
      </div>
    </section>

    <footer class="footer">
      Hosted directly from GitHub • Hosted for Safari, iPadOS, Chrome &amp; Edge
    </footer>
  </div>

  <script>
    if ("serviceWorker" in navigator && location.protocol.startsWith("http") && !location.hostname.includes("htmlpreview")) {
      window.addEventListener("load", () => {
        navigator.serviceWorker.register("./sw.js").catch(() => {});
      });
    }
  </script>
</body>
</html>
"""


def make_manifest(name: str, short_name: str, start_url: str, theme_color: str, bg_color: str) -> str:
    """Return a clean Web App Manifest JSON string."""
    return json.dumps(
        {
            "name": name,
            "short_name": short_name,
            "start_url": start_url,
            "display": "standalone",
            "background_color": bg_color,
            "theme_color": theme_color,
            "orientation": "any",
            "icons": [
                {"src": "icon.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"},
                {"src": "icon.png", "sizes": "192x192", "type": "image/png"},
            ],
        },
        indent=2,
    ) + "\n"


def make_service_worker() -> str:
    """Generate a network-first offline-capable Service Worker."""
    return """const CACHE_NAME = 'study-suite-pwa-v1';
const CORE_ASSETS = [
  './',
  './index.html',
  './goodnotes.html',
  './interview.html',
  './manifest.json',
  './icon.png',
  './data_presets.js',
  './questions.js'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(CORE_ASSETS).catch(() => {}))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  if (url.origin !== location.origin) return;
  event.respondWith(
    fetch(event.request)
      .then((res) => {
        if (res && res.ok) {
          const copy = res.clone();
          caches.open(CACHE_NAME).then((c) => c.put(event.request, copy));
        }
        return res;
      })
      .catch(() => caches.match(event.request).then((m) => m || caches.match('./index.html')))
  );
});
"""


def write_site_dir(
    out_dir: Path,
    goodnotes_html: str,
    interview_html: str,
    hub_html: str,
    gn_presets_src: Path,
    ox_questions_src: Path,
    gn_icon_src: Path,
    ox_icon_src: Path,
) -> None:
    """Write the full static website and subfolder PWA variants into out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    gn_sub = out_dir / "goodnotes"
    ox_sub = out_dir / "interview"
    gn_sub.mkdir(parents=True, exist_ok=True)
    ox_sub.mkdir(parents=True, exist_ok=True)

    (out_dir / ".nojekyll").write_text("", encoding="utf-8")
    (out_dir / "index.html").write_text(hub_html, encoding="utf-8")
    (out_dir / "goodnotes.html").write_text(goodnotes_html, encoding="utf-8")
    (out_dir / "interview.html").write_text(interview_html, encoding="utf-8")

    (gn_sub / "index.html").write_text(
        to_subdir_variant(
            goodnotes_html,
            [
                ('href="interview.html"', 'href="../interview.html"'),
                ('href="index.html"', 'href="../index.html"'),
                ("navigator.serviceWorker.register('./sw.js')", "navigator.serviceWorker.register('../sw.js')"),
            ],
        ),
        encoding="utf-8",
    )
    (ox_sub / "index.html").write_text(
        to_subdir_variant(
            interview_html,
            [
                ('href="goodnotes.html"', 'href="../goodnotes.html"'),
                ('href="index.html"', 'href="../index.html"'),
                ('navigator.serviceWorker.register("./sw.js")', 'navigator.serviceWorker.register("../sw.js")'),
            ],
        ),
        encoding="utf-8",
    )

    shutil.copyfile(gn_presets_src, out_dir / "data_presets.js")
    shutil.copyfile(ox_questions_src, out_dir / "questions.js")
    shutil.copyfile(ox_icon_src, out_dir / "icon.png")
    shutil.copyfile(ox_icon_src, ox_sub / "icon.png")
    shutil.copyfile(gn_icon_src, gn_sub / "icon.png")

    (out_dir / "manifest.json").write_text(
        make_manifest("Study Studio — GoodNotes & Oxbridge AI", "Study Studio", "./", "#0b1120", "#0b1120"),
        encoding="utf-8",
    )
    (gn_sub / "manifest.json").write_text(
        make_manifest("GoodNotes Pro", "GoodNotes Pro", "./", "#0284c7", "#f3f5f9"),
        encoding="utf-8",
    )
    (ox_sub / "manifest.json").write_text(
        make_manifest("Oxbridge Maths Interviewer AI", "Oxbridge AI", "./", "#0d1321", "#0d1321"),
        encoding="utf-8",
    )
    (out_dir / "sw.js").write_text(make_service_worker(), encoding="utf-8")


def main() -> None:
    gn_html_path = GOODNOTES_DIR / "web" / "index.html"
    gn_presets_path = GOODNOTES_DIR / "web" / "data_presets.js"
    gn_icon_path = GOODNOTES_DIR / "assets" / "icon.png"

    ox_html_path = OXBRIDGE_DIR / "web" / "index.html"
    ox_questions_path = OXBRIDGE_DIR / "web" / "questions.js"
    ox_icon_path = OXBRIDGE_DIR / "assets" / "icon.png"

    goodnotes_html = build_inlined_html(gn_html_path, gn_presets_path, '<script src="data_presets.js"></script>')
    interview_html = build_inlined_html(ox_html_path, ox_questions_path, '<script src="questions.js"></script>')
    hub_html = make_hub_html()

    for target in TARGETS:
        write_site_dir(
            target,
            goodnotes_html,
            interview_html,
            hub_html,
            gn_presets_path,
            ox_questions_path,
            gn_icon_path,
            ox_icon_path,
        )
        print(f"Built unified static site & PWA bundle in {target}")

    print(
        f"Sizes: goodnotes.html={len(goodnotes_html):,} chars, "
        f"interview.html={len(interview_html):,} chars, index.html={len(hub_html):,} chars"
    )


if __name__ == "__main__":
    main()
