# Task 5 of 6 — Feature Pages: BVA UI + Dirty Strings UI

Depends on: Tasks 1–4. Task 1 gives layout/theme; Task 2 gives the result panel + `renderResults()`; Task 3 gives `bva/services.py`; Task 4 gives `dirty_strings/presets.py`. This task wires everything into the two working feature pages and replaces the placeholders.

## Goal
Deliver both feature pages fully functional end-to-end: forms → AJAX endpoints → services/presets → live result panel.

## Prerequisites (all done in prior tasks)
- Shared layout, theme toggle, sidebar links (`/bva/`, `/dirty-strings/`).
- `renderResults(rows)` result panel with badges, per-row copy, Copy All / JSON / Markdown, toasts.
- Pure logic modules: `bva.services` and `dirty_strings.presets`.

## What to build

### 1. BVA page (`bva/views.py`, `bva/urls.py`, `bva/templates/bva/index.html`)
Two-column split (desktop): left = config form, right = live results.

**Left column form:**
- Data type selector (tabs or dropdown): `Integer`, `Float / Decimal`, `String Length`, `Date`.
- `Min` and `Max` inputs; `Inclusive` checkbox, default checked.
- Type-specific inputs shown/hidden dynamically (vanilla JS/Alpine):
  - Float: `Step / Precision` field (default `1`).
  - Date: `Step` dropdown (`1 Day`, `1 Month`, `1 Year`, default `1 Day`); `Format` dropdown (`YYYY-MM-DD`, `DD.MM.YYYY`).
  - String Length: character filler option (`Repeat char` with a char input, e.g. `a`, or `Random ASCII` radio).
- `Generate Points` button **plus** reactive auto-generate on input changes (debounced).

**Backend endpoint** (e.g. `POST /bva/generate/` returning JSON): validates input, calls `compute_bva_points` / `compute_string_length_points`, returns `[{status, description, value}, ...]`. Client calls `renderResults(rows)` from Task 2 — no page reload.

### 2. Dirty Strings page (`dirty_strings/views.py`, `dirty_strings/urls.py`, `dirty_strings/templates/dirty_strings/index.html`)
- Presets organized as tabbed cards or accordion sections, one per category from `presets.PRESETS`. Render server-side from the preset data (no hardcoding of payload strings in templates).
- Search/filter bar filtering across all payloads — implement client-side filtering over the rendered items (instant, as-you-type).
- Each payload item: label/description, monospace value preview box, `Copy` button with `Copied!` toast (reuse Task 2 copy/toast machinery).
- Interactive custom generator widget: length `N` input + character selection (single char or Random ASCII) → generates preview locally (client-side) or via a small endpoint calling `generate_custom_string`; result shown in a mono box with its own copy button.
- Escape rendering: payload values must be HTML-escaped by Django templates so XSS samples display literally (do not mark safe).

### 3. Quality pass
- Desktop-first with clean scaling on mobile/tablet for both pages.
- Sidebar active-state highlights correct page per section.
- No build pipeline: all interactivity via Alpine.js/vanilla JS loaded from CDN/static, per spec.

## Done when
- BVA: every data type produces the correct 7-point (+ string variants) table live in the panel, with working copies and exports.
- Dirty Strings: all 5 categories render from presets, search filters instantly, copy works everywhere, custom generator produces requested strings.
- Manual smoke of both pages at common desktop and mobile widths; `python manage.py test` still green.
