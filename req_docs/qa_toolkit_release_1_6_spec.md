# Task 6 of 6 — Integration Hardening, README & Release Checklist

Depends on: Tasks 1–5 (all features implemented). This is the final acceptance task: verify the whole spec end-to-end, polish gaps, and document the project. No new features.

## Goal
Make the app release-ready as `v0.1.0-alpha` per the spec: full automated verification, cross-feature consistency checks, and a README.

## Prerequisites (all done in Tasks 1–5)
- Runnable Django app with BVA and Dirty Strings features, shared layout, tested pure-logic modules.

## What to build

### 1. Full test suite & verification
- Run `python manage.py test` — all tests green (units from Tasks 3–4 plus any view/endpoint tests added here).
- Add integration tests for the AJAX endpoints (`/bva/generate/`, dirty-strings endpoints): valid inputs → 200 + correct JSON shape; invalid input → 4xx with a safe error message (no stack traces).
- Sanity-check spec conformance item by item:
  - Header: `QA Toolkit` + `v0.1.0-alpha` badge, theme toggle, GitHub link.
  - Sidebar: two active entries linking to working pages, two "Coming in v0.2" disabled entries.
  - BVA: 4 data types, Min/Max/Inclusive, Float precision, Date step+format, String Length filler, Generate button + reactive regeneration, 7-point model incl. nominal center, 0/negative-length safety.
  - Dirty Strings: all 5 categories, search bar, per-item copy + toast, custom generator.
  - Outputs: Valid/Invalid/Boundary badges in green/red/blue, mono value containers, Copy All / Copy as JSON / Copy as Markdown.
- Clean startup check: fresh clone path — create venv, `pip install -r requirements.txt`, `migrate`, `runserver` works. Ensure a `requirements.txt` exists (pin Django 5.x). No Node/npm artifacts anywhere.

### 2. Polish
- Consistent visual language across both features (spacing, badge colors, mono boxes).
- Error states: form validation errors surface as friendly inline messages; endpoint failures show a non-breaking message in the results panel.
- Keyboard + a11y basics: focus styles, labels tied to inputs, aria-live on the results panel update region and toast.

### 3. README
Write a real `README.md` (replacing the stray placeholder): project purpose, feature screenshots-or-description, tech stack, setup & run instructions, how to run tests, project layout tree (matching spec section 4), roadmap note (All Pairs and JSON/JWT Inspector coming in v0.2).

## Done when
- Full test suite passes from a fresh environment.
- Every checklist item in section 1 above is confirmed against the running app.
- README accurate and complete; repo is presentable as the Release 1 MVP.
