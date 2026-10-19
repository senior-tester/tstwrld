# Task 2 of 6 — Result Panel Component & Copy-to-Clipboard UX

Depends on: Task 1 (base layout, header/sidebar, Tailwind + Alpine.js via CDN are in place). This task builds the reusable right-column output UI used by both features; it delivers no business data itself.

## Goal
Implement a reusable, self-contained result-panel UI component (template partial + small vanilla JS/Alpine helper) that later tasks feed rows into. It must render rows with status badges, monospace values, per-row copy, and global export/copy actions.

## Prerequisites (already done in Task 1)
- `base.html` with Tailwind CDN and Alpine.js loaded, theme toggle, header/sidebar.
- `core/` app exists and serves the layout.

## What to build

### 1. Reusable row rendering (`core/templates/components/result_panel.html` or similar partial)
Accepts a list of result rows via context (each row: `badge`, `description`, `value`). Renders the spec's output format:
- **Status / Class Badge:** `Valid` (green), `Invalid` (red), `Boundary` (blue) — colored pill badge per row.
- **Description:** free text, e.g. `Min - 1 (Below boundary)` (the wording itself is supplied by callers in later tasks).
- **Generated Value:** monospace code container (use the monospace utility from Task 1).
- **Actions:** quick copy icon `📋` per row — copies the row's raw value only.

### 2. Copy + export actions
- `Copy All (Raw List)` — copies one raw value per line.
- `Copy as JSON` — copies rows as a JSON array of objects `{status, description, value}`.
- `Copy as Markdown Table` — copies a GitHub-flavored markdown table with the three columns.
- All copy buttons show instant toast feedback (`Copied!`), auto-dismissing after ~1.5 s.

### 3. Live-update wiring
- The panel must be updateable without full page reloads. Implement a `renderResults(rows)` JS function (vanilla JS/Alpine, module in `core/static/js/`) that takes the row list and re-renders the panel. Expose it so feature pages (Tasks 3–5) can call it after a fetch.
- Add a static demo trigger (e.g., a hidden dev button or demo route `/demo/results/` in `core`) that renders 3 sample rows — this is scaffolding to prove the component works and may stay or be removed later.

### 4. Responsiveness
- Panel scales fluidly on mobile/tablet (rows stack, table converts to cards or scrolls horizontally) per spec's desktop-first responsive requirement.

## Done when
- Visiting the demo route shows rows with correctly colored badges, mono values, per-row copy, Copy All / JSON / Markdown all producing correct clipboard content, and toast feedback firing.
- `renderResults()` can be called repeatedly to swap content (this is what Tasks 3 and 4 will use).
