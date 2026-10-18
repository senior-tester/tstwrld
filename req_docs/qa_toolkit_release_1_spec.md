# Specification: Release 1 (QA Toolkit MVP)

## 1. Overview & UI/UX Guidelines
A lightweight, modern web application for QA engineers, test automation practitioners, and learners. Built with Python/Django.

### Tech Stack & Design Requirements
- **Backend:** Python 3.11+, Django 5.x.
- **Frontend / Styling:** Django Templates + Tailwind CSS (via CDN) + lightweight Vanilla JS / Alpine.js (no Node.js build pipeline required).
- **Theme:** Clean modern developer aesthetic (Linear / Vercel style). Dark and light mode support with automatic system detection. Monospace font for code and test data snippets.
- **Responsiveness:** Desktop-first with clean fluid scaling for mobile/tablet.

### General Layout
- **Header:**
  - App Name: `QA Toolkit` (with subtle badge `v0.1.0-alpha`).
  - Theme toggle (Dark / Light).
  - Link to GitHub repository.
- **Sidebar (Left Navigation):**
  - 📐 Boundary Values (BVA) *(Active)*
  - 🧪 Special & Dirty Strings *(Active)*
  - ⏳ *All Pairs (Coming in v0.2)*
  - ⏳ *JSON/JWT Inspector (Coming in v0.2)*
- **Main Content Area:**
  - Two-column split layout on desktop:
    - Left column: Input parameters & configuration form.
    - Right column: Real-time generated output tables/cards with one-click copy buttons (`Copy` per row and `Copy All`).

---

## 2. Feature 1: Boundary Value Analysis (BVA) Generator

### Goal
Calculate and present boundary points and equivalence class values for numeric ranges, dates, and string lengths based on standard testing techniques.

### Input Parameters (Form)
1. **Data Type Selector (Tabs / Dropdown):**
   - `Integer`
   - `Float / Decimal`
   - `String Length`
   - `Date`
2. **Range Boundaries:**
   - `Min` input field (lower bound).
   - `Max` input field (upper bound).
   - `Inclusive` checkbox for boundaries (default: checked `[x]`).
3. **Data Type Specific Inputs:**
   - **For Float:** `Step / Precision` field (e.g. `0.1`, `0.01`; default: `1`).
   - **For Date:**
     - `Step` dropdown (`1 Day`, `1 Month`, `1 Year`; default: `1 Day`).
     - `Format` dropdown (`YYYY-MM-DD`, `DD.MM.YYYY`).
   - **For String Length:** Character filler option (`Repeat char` e.g., 'a', or `Random ASCII`).
4. **Action:** `Generate Points` button (plus reactive auto-generate on input changes).

### Calculation Logic (7-Point Boundary Model)
For a range $[Min, Max]$ with step $S$:
- **Lower Boundary:**
  - $Min - S$ (Invalid / Out of bounds)
  - $Min$ (Valid / Exact lower boundary)
  - $Min + S$ (Valid / Inside boundary)
- **Nominal Value:**
  - Center value: $\lfloor(Min + Max) / 2\rfloor$ (Valid)
- **Upper Boundary:**
  - $Max - S$ (Valid / Inside boundary)
  - $Max$ (Valid / Exact upper boundary)
  - $Max + S$ (Invalid / Out of bounds)

*For String Length:* Generate actual strings of lengths: $0$, $Min-1$, $Min$, $Min+1$, $Nominal$, $Max-1$, $Max$, $Max+1$ (handling $0$ and negative length bounds safely).

### Output Display
- Table / Cards with columns:
  - **Status / Class Badge:** `Valid` (green), `Invalid` (red), `Boundary` (blue).
  - **Description:** e.g., `Min - 1 (Below boundary)`, `Min (Exact boundary)`, `Nominal (Middle)`.
  - **Generated Value:** Monospace code container.
  - **Actions:** Quick copy icon `📋` per row.
- Header actions: `Copy All (Raw List)`, `Copy as JSON`, `Copy as Markdown Table`.

---

## 3. Feature 2: Special & Dirty Strings Generator (Fuzzing / Boundary Strings)

### Goal
Curated catalog of payloads and corner-case strings for testing input fields against crashes, encoding issues, layout breakage, and basic vulnerabilities.

### Categories & Data Presets
Organized in tabbed cards or accordion sections:

1. **Whitespace & Empty Strings:**
   - Empty string `""`
   - Whitespace only (`"   "`, tab `\t`, newline `\n`)
   - Zero-width spaces (`\u200B`, `\uFEFF`, `\u200C`)
   - Leading / trailing whitespaces (`"  leading and trailing  "`)

2. **Long Strings & Buffer Limits:**
   - Fixed lengths: `255`, `256`, `512`, `1024`, `4096` characters.
   - Long continuous string without spaces (to test UI container overflows).
   - Custom length string generator (input length $N$ + character selection).

3. **Unicode, Emojis & Internationalization:**
   - Emojis: single (`🔥`), compound/ZWJ sequences (`👨‍👩‍👧‍👦`, `👍🏽`).
   - Non-Latin scripts & diacritics: `日本語`, `中文`, `Zålgø tēxt`.
   - Right-to-Left (RTL) strings: Arabic / Hebrew text (`مرحبا`, `שלום`).

4. **Security & Injection Payloads (Basic):**
   - XSS payloads: `<script>alert(1)</script>`, `<img src=x onerror=alert(1)>`
   - SQL Injection: `' OR '1'='1`, `admin' --`, `1; DROP TABLE users;`
   - HTML / Template injections: `<b>bold</b>`, `{{ 7*7 }}`, `${7*7}`, `%s%s%s%s`
   - Path Traversal: `../../../../etc/passwd`, `..\..\..\windows\win.ini`

5. **Numeric & System Edge Cases:**
   - Number edge cases: `0`, `-0`, `000123`, `NaN`, `Infinity`, `-Infinity`, `1e308`, `null`, `undefined`, `true`, `false`.

### UI Interaction
- Search / filter bar across all payloads.
- Each payload item displayed with:
  - Label / Description (e.g., *XSS via Image Tag*).
  - Value preview in a monospace box.
  - `Copy` button with instant toast feedback (`Copied!`).
- Interactive custom generator widget for arbitrary length strings.

---

## 4. Project Architecture & Directory Structure

```text
qa_toolkit/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── base.html
│       └── components/
│           ├── header.html
│           └── sidebar.html
├── bva/
│   ├── services.py       # Pure Python calculation logic (easy to unit test)
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── bva/
│           └── index.html
└── dirty_strings/
    ├── presets.py        # Structured catalog of dirty strings & payloads
    ├── views.py
    ├── urls.py
    └── templates/
        └── dirty_strings/
            └── index.html
```

### Implementation Notes
- Keep business logic in `services.py` / `presets.py` decoupled from Django views for clean testability.
- Use lightweight AJAX/fetch endpoints or HTMX to update result panels without full page reloads.
