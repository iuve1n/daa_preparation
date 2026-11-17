# DAA Fieldnotes
A complete static Java 17 study companion mapped to the supplied AITU 2026–2027 syllabus. Ten lessons, ten interactive traces, 76 assessment questions (including 10 exam-only transfer items), locally saved notes, sequential mastery gates, midterm/endterm checkpoints, cumulative final rehearsal, and a project rubric.

## Run locally
From this directory: `python3 -m http.server 8000`. Visit http://localhost:8000. No install or build is required. Do not open index.html using file://, because JSON fetches need a server.

## Deploy to GitHub Pages
1. Create a GitHub repository and upload the **contents of this folder**, including `.github/workflows/pages.yml`, to its root on the `main` branch.
2. In Settings → Pages → Build and deployment, select **GitHub Actions**.
3. Push to main or run “Deploy course to GitHub Pages” from Actions.
4. Open the deployment URL reported by the workflow. Relative asset paths support repository subpaths.

Alternatively, select “Deploy from a branch”, main, /(root) in Pages settings; no build is needed. Do not use both deployment methods.

## Course behavior
Pass each lesson at 80%; complete 1–5 and pass the midterm to access 6; complete 6–10 and pass the endterm to access the capstone. The final rehearsal is cumulative. Retakes shuffle questions/options; feedback appears after submission. Notes, passes, and milestones use browser localStorage. Export and restore JSON on the Reference desk. This is self-study, not a secure testing platform: answers and gates are client-side.

The official syllabus includes a final exam, not a final project. The capstone is an independent addition requested by the learner. The syllabus overview's NP-completeness/approximation topics are covered in a reference extension. Videos are optional YouTube search links rather than unverified embedded videos; duration and availability have not been verified. Java snippets are study examples, not an in-browser compiler. Some implementation briefs intentionally require completing an algorithm independently.

## Content and assessment sources
- Supplied syllabus: assets/syllabus.pdf (contains instructor contact information; review before publishing publicly).
- User-supplied teacher sample concepts and implementation list.
- Princeton Algorithms: https://algs4.cs.princeton.edu/
- CP-Algorithms: https://cp-algorithms.com/
- Quiz design: https://uwaterloo.ca/centre-for-teaching-excellence/catalogs/tip-sheets/designing-multiple-choice-questions

Questions use one-best-answer stems, plausible misconceptions, shuffled options, numeric retrieval, and explanatory feedback. They cannot guarantee guessing is eliminated. Question bank source is build_questions.py → questions.json; lessons are build_content.py → content.json. Regenerate with Python 3 after editing. Plain static HTML/CSS/JS; Google Fonts is optional and falls back to local sans-serif. No analytics, account, or API keys.

## Comprehensive preparation update
- Gradelyy-inspired blue/dark workspace with a persistent light-mode choice. Original DAA layout and course content; not affiliated with Gradelyy.
- Expanded all ten lectures with explicit learning objectives, deeper proof/edge-case sections, worked examples, and explanation prompts.
- 76 questions: 66 lecture/practice questions plus 10 held for exams. Includes numerical recall, traces, counterexamples, and plausible distractors.
- Grade analysis records the last 250 submitted attempts and uses the latest response per question to diagnose gaps. Targeted practice retries missed items; it never unlocks new lectures. Passing a later review updates the diagnosis without rewriting earlier scores. Previous version progress survives; historical per-question answers cannot be recovered retroactively.
- Official grade calculator follows the syllabus weights, separate from mastery percentages and self-reported coding evidence.
- Eight implementation workspaces cover the teacher's complete implementation list. Each has a precise contract, starter, expected examples, hints, saved draft, downloadable standalone Java test harness, and self-reported test status. Java executes locally with a JDK, not in the browser. No automatic code grading or AI grading is claimed.

Rebuild authored sources with `python3 regenerate.py` (supersedes the individual regeneration commands above). Validate downloadable harnesses against reference adapters with `python3 tests/check_java_tasks.py`. Requires a JDK with source-file execution. A runnable starter intentionally fails until the learner implements it.

Public visual reference: https://www.gradelyy.com/ (blue #0072f5, dark #050810, Sora/DM Sans; optional cool light palette). No private dashboard or account was accessed.

For the browser regression: install Python Playwright and Chromium, serve this folder on port 8000, then run `python3 tests/check_browser.py`. Tests use an isolated browser profile.
