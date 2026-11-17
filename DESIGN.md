---
name: DAA Fieldnotes
description: A focused algorithms course and Java practice workspace.
colors:
  background: "#050810"
  surface: "#0d1117"
  raised: "#161b26"
  soft: "#102544"
  ink: "#f0f4ff"
  muted: "#a2adc2"
  line: "#263044"
  accent: "#0072f5"
  button: "#0064d9"
  button-hover: "#0058c4"
  highlight: "#64a8ff"
  success: "#5ce2a2"
  focus: "#ffb34c"
  light-background: "#f6f7f9"
  light-surface: "#fcfcfd"
  light-raised: "#eff1f4"
  light-soft: "#e8f1ff"
  light-ink: "#1e293b"
  light-muted: "#526278"
  light-line: "#d5dce7"
  light-success: "#116b45"
  light-focus: "#995800"
typography:
  display:
    fontFamily: "Sora, Manrope, sans-serif"
    fontSize: "clamp(34px, 4vw, 55px)"
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: "-0.03em"
  headline:
    fontFamily: "Sora, Manrope, sans-serif"
    fontSize: "27px"
    lineHeight: 1.18
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Sora, Manrope, sans-serif"
    fontSize: "19px"
    lineHeight: 1.18
    letterSpacing: "-0.03em"
  body:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "16px"
    lineHeight: 1.65
  button:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "13px"
    fontWeight: 700
rounded:
  field: "8px"
  control: "10px"
  code: "12px"
  panel: "14px"
  hero: "20px"
spacing:
  compact: "8px"
  control-gap: "12px"
  row-gap: "16px"
  grid-gap: "20px"
  panel-inset: "25px"
components:
  button-primary:
    backgroundColor: "{colors.button}"
    textColor: "white"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "12px 21px"
  button-primary-hover:
    backgroundColor: "{colors.button-hover}"
  button-secondary:
    backgroundColor: "{colors.raised}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "12px 21px"
  text-field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    padding: "12px"
---

# Design System: DAA Fieldnotes

## Overview

**Creative North Star: "The Algorithm Workspace"**

A Gradelyy-inspired dark workspace uses blue actions, crisp typography, and layered neutral surfaces to support sustained study. Reading remains central; performance evidence and Java practice extend the original sequential course without replacing it.

**Key Characteristics:**
- Dark neutral surfaces with purposeful blue accents.
- Sora headings and DM Sans reading text.
- Sequential lessons, explicit algorithm states, and targeted review.
- Optional light appearance with the same component structure.

## Colors

The frontmatter records the active dark palette and optional light palette. CSS variables retain legacy names: paper maps to background, green to accent, lime to highlight, white to surface, and orange to focus. The separate button variable supplies darker blue for white button text. Blue identifies actions and active algorithm cells; success color identifies completion, while orange highlights work to revisit and keyboard focus.

Light appearance is applied by the light class on the root element. It changes neutral surfaces, text, success, and focus colors while preserving the blue action palette. Code remains dark in both appearances.

## Typography

Sora heads pages, sections, course names, and scores, with Manrope and sans-serif fallbacks. DM Sans supplies prose and controls. Code and algorithm cells use ui-monospace with monospace fallback. Body text measures at most 72ch; introductory text uses 17px at 55ch. The overview title uses clamp(34px, 3.8vw, 53px), becoming 39px on narrow screens. Page headings become 37px on narrow screens. Smaller navigation and evidence labels preserve a compact hierarchy.

## Layout

A fixed 276px course rail offsets the main shell. The header is 85px high. Main content has a 1240px maximum width and 55px 6% 80px padding. Desktop lessons pair a flexible reading column with a 185px sticky contents column and 40px gap. Course rows retain numbers, titles, and statuses in sequence.

At 1100px and below the rail becomes 235px, the hero stacks, and lesson contents navigation hides. At 900px and below three summary cards stack and analysis rows simplify to two columns. At 650px and below the rail becomes a toggleable 280px menu, shell offset disappears, header becomes 65px, and main padding becomes 34px 6% 60px. Workspace links stack; grade fields change from three columns to two; histories and trace controls wrap.

## Elevation & Depth

Tonal surfaces and thin borders define hierarchy. Raised panels hold examples, traces, summaries, and notices. The mobile rail has a structural 10px 0 25px #2223 shadow. Current navigation has an inset blue 2px marker. Ordinary panels do not float above the workspace.

## Shapes

Controls use rounded corners, panels use a broader curve, and the hero graphic has the widest radius. Course rows remain open with bottom separators. Code and wide source content scroll horizontally. Input and code-editor surfaces use clear thin borders.

## Components

Primary buttons use the separate button blue and white text; hover deepens the blue. Secondary buttons use raised surfaces and neutral text, changing to a soft blue surface and blue border on hover. Disabled controls use half opacity. Keyboard focus uses a 3px outline offset by 5px.

Navigation uses a soft blue hover/current surface, neutral text, and a blue inset marker for the current lesson. Tags use raised surfaces, thin borders, and muted labels. Algorithm cells retain real finite states, blue active cells, explanatory text, and disabled boundary controls.

Assessment options use surface backgrounds and blue selected borders. Correct feedback is green-tinted; review feedback is warm amber. Their text/background pairs change together in light appearance.

Performance summaries show the latest attempt, latest incorrect question evidence, and self-reported implementation status. Topic rows connect evidence to the next action; history remains a compact separated list. Targeted review retries questions whose latest response was incorrect and does not unlock lessons.

Eight coding workspaces pair acceptance examples, editable Java methods, hints, downloads, and self-reported testing evidence. Monospace editors use 13px/1.8 text and at least 300px height. Java runs locally. The official grade calculator groups nine entered marks, with a live result and a clear separation from mastery scores.

Motion is limited to bar height (0.5s ease-out) and primary/option background transitions (0.15s ease-out), enabled only when reduced motion is not requested.

## Do's and Don'ts

- Do preserve the original lesson sequence and mastery progression.
- Do distinguish latest learning evidence, self-reported testing, and entered official marks.
- Do keep both appearances readable with visible focus and explicit feedback.
- Don't present local Java testing as automatic grading.
- Don't replace concrete algorithm states with decorative graphics.
