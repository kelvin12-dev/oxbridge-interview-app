# Oxbridge Maths Interviewer AI (iPad App + Cloud `.ipa` Build)

A full **React Native (Expo)** iPad application and standalone Safari/PWA bundle containing all **85 Oxford & Cambridge Mathematics Interview Questions** with a **pressure-sensitive Apple Pencil whiteboard** and **Live Gemini Vision Auto-Hints**.

## Features
- **Complete 85-Problem Oxbridge Archive:** Every problem across all 6 sections (Anonymous Sets 1–8, Oxford Admissions & College Interviews, Cambridge College Interviews, Archive Sheets G & H, and Handwritten Sheets B1 & C1–C6), complete with KaTeX math rendering, 3 progressive Socratic hints per problem, and full worked solutions.
- **iPad Whiteboard Built for Apple Pencil:**
  - Smooth quadratic Bézier ink rendering with Apple Pencil pressure sensitivity.
  - **Pencil Only (Palm Rejection)** toggle so resting your palm on the iPad never leaves stray marks.
  - Multi-page scratchpad per problem (auto-saved locally), Grid / Dots / Lined / Blank paper, Pen / Highlighter / Stroke Eraser, Undo / Redo, and toggleable **$x$-$y$ Coordinate Axes** for graph-sketching questions.
- **Live Gemini Vision Interviewer (`Auto-See Canvas`):**
  - Automatically watches your iPad whiteboard as you write.
  - When you pause writing (default `3.5s`, configurable `2s–8s`), it automatically snapshots your handwriting and sends it to **Google Gemini Vision** (`gemini-2.5-flash` or `gemini-2.5-pro`).
  - Pops up an animated **AI Tutor Hint Card** showing what Gemini read on your iPad (`Saw on iPad`), pointing out any algebraic/sign slip or giving a Socratic nudge/follow-up question—with optional **voice readout** (`🔊`).
  - Includes a full **Tutor Chat Drawer** that automatically attaches your current iPad canvas to every question you ask.

---

## Option A: Build a Downloadable `.ipa` on Cloud Macs (No Mac Required)

This repository is already initialized with Git and configured for **three** no-Mac cloud `.ipa` workflows:

### Method 1: Free GitHub Actions Cloud Mac Build (Recommended for Sideloading)
1. Create a new empty repository on [GitHub](https://github.com/new) (e.g., `oxbridge-interview-ai`).
2. Double-click **`push-to-github.bat`** (or run `git remote add origin <URL> && git push -u origin main`).
3. Go to your GitHub repo → **Actions** tab → wait for **Build iOS IPA (No Mac Required)** to finish (~6–10 minutes on `macos-15`).
4. Download the **`OxbridgeInterviewAI-ipa`** artifact (unzip to get `OxbridgeInterviewAI.ipa`).
5. Install `OxbridgeInterviewAI.ipa` onto your iPad using **`iloader`** (`D:\sideload\iloader.exe`), **Sideloadly**, **AltStore**, or **SideStore** (automatically signs with your Apple ID—no \$99/yr developer account required!).

### Method 2: Expo EAS Build (Signed `.ipa`)
```bash
npm install -g eas-cli
eas login
eas build --platform ios --profile preview
```
*(Requires an Apple Developer account for ad-hoc/App Store signed `.ipa`.)*

### Method 3: Codemagic (`codemagic.yaml`)
Connect your pushed GitHub repo in [Codemagic](https://codemagic.io/) and trigger **`Oxbridge Interview AI - iOS IPA Build`** — Codemagic builds on a cloud `mac_mini_m2` and outputs `OxbridgeInterviewAI.ipa` under Artifacts.

---

## Option B: Use Immediately on Your iPad Today (Over Wi-Fi)
1. Double-click **`start-local-server.bat`** on your Windows PC.
2. Open **Safari** on your iPad (connected to the same Wi-Fi) and visit the printed `http://<YOUR-PC-IP>:8080` URL.
3. Tap Safari's **Share** icon → **"Add to Home Screen"** to launch it full-screen just like a native iPad app!

---

## Connecting Your Gemini API Key
1. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).
2. Inside the app, tap **⚙️ Settings** (top right) → paste your key → tap **🧪 Test Gemini Connection** → **Save Settings**.
3. Ensure **👁️ Auto-See: ON** is lit green in the top bar, write on the iPad canvas, pause briefly, and watch the AI interviewer automatically inspect your handwriting and pop up hints!
