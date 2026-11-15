# GoodNotes Pro (`GoodNotesPro.ipa`)

A zero-delay, full-featured iPad & iOS note-taking app engineered around the complete **Goodnotes 6** toolset, smooth Apple Pencil handwriting (`pointerrawupdate` + `getCoalescedEvents()` + `getPredictedEvents()` + `desynchronized` 3-layer canvas), and built-in **Google Drive Backup & Auto-Sync**.

## Core Features
- **Zero-Delay Ink Engine:** 3-layer Retina canvas (`bgCanvas` templates/PDFs + `dryCanvas` layered ink + `wetCanvas` with `{ desynchronized: true }`), Apple Pencil coalesced/predicted points, Fountain/Ball/Brush pens, Stroke Stabilization (`0–100%`), and **Pencil Only (Palm Rejection)**.
- **All 13 Goodnotes 6 Tools & Gestures:**
  - **Pen** (`Fountain`, `Ball`, `Brush`, **Draw & Hold** auto-shape snap, **Scribble to Erase**, **Circle to Lasso**).
  - **Highlighter** (automatically layered *behind* ink + **Straight Line** mode).
  - **Eraser** (`Precision`, `Standard`, `Stroke` + **Erase Highlighter Only** + **Auto-Deselect**).
  - **Shapes** (Line, Arrow, Rectangle, Ellipse, Triangle, Diamond, Coordinate Axes, Wave + optional **Fill Color**).
  - **Lasso** (Filter toggles, Move, Resize/Rotate, Recolor, Convert to Text/LaTeX, Save as Element, Screenshot, Duplicate, Delete).
  - **Elements & Stickers** (Sticky Notes, Study Stamps, STEM Diagrams, plus custom saved elements).
  - **Image Tool**, **Text Box Tool**, **Study Tape** (active-recall cover strips that reveal/hide on tap), **Zoom Window** (magnified precision box + auto-advance margin), **Draggable/Rotatable Ruler**, **Laser Pointer** (Dot & Fading Trail), and **Timer / Stopwatch**.
- **Library, Organization & Study Sets:**
  - Nested color-coded **Folders**, **12 Covers**, **18 Dynamic Templates**, **6 Paper Colors**, **Favorites / Starred Pages**, **Global Search**, **Trash Bin**, **Document Tabs**, **Side-by-Side Split View**, **4-Tab Page Manager** (Thumbnails, Bookmarks, Outlines, Audio Clips), and **Spaced Repetition Flashcard Study Sets**.
- **Audio Sync & AI Suite (`Ask Goodnotes` + Math Assist):**
  - Record voice notes synced to stroke timestamps + play back with live stroke highlighting.
  - Built-in local Math Assist + optional **Google Gemini Vision** integration for handwritten step-checking, OCR, summarization, and flashcard generation.
- **Google Drive Backup & Export:**
  - Direct **Google Drive REST API v3**, zero-config **Google Apps Script Web App Bridge**, native **iPadOS Share Sheet** (`UIActivityViewController` to Google Drive / Files), and built-in offline **PDF Exporter** + native iOS `PDFKit` **PDF Importer**.

---

## Building `GoodNotesPro.ipa` on GitHub Actions (No Mac Required)
1. Push this repo to GitHub (`push-to-github.bat` or `git push`).
2. Open the repository's **Actions** tab and select **Build GoodNotes Pro iOS IPA (No Mac Required)**.
3. Download the **`GoodNotesPro-ipa`** artifact, unzip it to obtain `GoodNotesPro.ipa`, and sideload onto your iPad/iPhone using **`iloader`**, **Sideloadly**, **AltStore**, or **SideStore**.

## Instant Local Preview (PC / iPad Safari)
Double-click **`start-local-server.bat`** and open `http://<YOUR-PC-IP>:8090` in iPad Safari (or `http://localhost:8090` on Windows).
