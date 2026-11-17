# Verification

- JavaScript syntax: `node --check app.js` passed.
- Chromium desktop (1440px) and mobile (390px): screenshots inspected.
- Browser flows passed: interactive trace next step, correct quiz scoring, successful lecture progression, locked midterm boundary, saved notes after reload, complete endterm bank, persisted project checklist, mobile menu navigation, no horizontal overflow on home/lesson, no uncaught browser errors.
- Java reference assertions passed using the installed Java source launcher, including 500 seeded randomized suffix-array comparisons with explicit suffix sorting and brute-force LCP checks. Installed runtime is Java 21; `--source 17` is unsupported by this environment's stripped compiler distribution. Source uses Java 17-compatible language/API features, but a Java 17 runtime was not available for direct verification.
- Independent design/content review: ship disposition, followed by accessible progress labeling, monochrome arrow rendering, exam-only transfer questions, and downloadable complete implementations of all teacher-named tasks.
- Impeccable launcher/detector unavailable in this environment. Browser checks and screenshot inspection were used.
- GitHub Pages workflow is included but has not been executed against a GitHub repository. No live deployment was performed.

To run the Java reference harness with a JDK: `java assets/Algorithms.java` (Java 17+) or compile with `javac assets/Algorithms.java` and run `java -cp assets Algorithms`.

## Expanded preparation update
- Browser verification passed legacy data migration; recording a partly incorrect quiz; missed-question diagnosis; targeted retry; removal of corrected misses; persistence of code and self-reported test evidence; light-mode switch; and absence of overflow on five mobile routes.
- Official grade calculator: all nine entries at 80 produced 80.0 overall. Calculation uses exact syllabus coefficients.
- All eight downloadable test harnesses executed successfully using reference adapters (tests/check_java_tasks.py), validating their expected cases against the implemented algorithms.
- Expanded bank has 76 unique IDs, including 10 exam-only questions. All ten lectures have additional worked reasoning and learning objectives.
- Screenshot review covers dark desktop home, dark desktop analysis, and light mobile analysis. No external backend required.
