# Task 3 of 6 — BVA Business Logic: `bva/services.py` (Pure Python, Unit-Testable)

Depends on: Task 1 (the `bva/` app package exists) and Python/Django environment from Task 1. Does NOT depend on Task 2 (pure logic, no UI). The view/UI wiring for BVA comes in Task 4.

## Goal
Implement the complete Boundary Value Analysis calculation engine as pure Python functions in `bva/services.py`, decoupled from Django, with thorough unit tests. This module is the single source of truth for BVA math and string generation.

## Prerequisites (already done in Task 1)
- `bva/` app package exists; Python 3.11+ environment is set up.

## What to build

### 1. Public API
Design a small, typed interface. Suggested shape (adapt naming as you see fit, but keep logic framework-free):

```python
def compute_bva_points(min_value, max_value, *, inclusive=True, step=1) -> list[BvaPoint]
def compute_string_length_points(min_len, max_len, *, filler="a") -> list[BvaPoint]
```

- `BvaPoint` is a dataclass with fields matching the output contract: `status` (`"valid" | "invalid" | "boundary"`), `description` (e.g. `"Min - 1 (Below boundary)"`, `"Nominal (Middle)"`), `value` (the generated value as string/int).
- Inputs are validated; raise `ValueError` on nonsensical input (min > max, step <= 0, negative string lengths beyond what's handled).

### 2. 7-Point Boundary Model (numeric ranges)
For range `[Min, Max]` with step `S` produce exactly:
- `Min - S` → Invalid / Out of bounds
- `Min` → Valid / Exact lower boundary (badge: Boundary)
- `Min + S` → Valid / Inside boundary
- Nominal: `floor((Min + Max) / 2)` → Valid / Middle
- `Max - S` → Valid / Inside boundary
- `Max` → Valid / Exact upper boundary (badge: Boundary)
- `Max + S` → Invalid / Out of bounds

Support:
- **Integer:** straightforward integer arithmetic.
- **Float / Decimal:** `Step / Precision` honored (e.g. `0.1`, `0.01`; default step `1`). Use `decimal.Decimal` internally to avoid float artifacts like `0.30000000000000004`; format output values cleanly (strip trailing zeros).
- **Date:** `Min`/`Max` are dates; step is one of `1 Day`, `1 Month`, `1 Year` (default `1 Day`). Calendar-aware arithmetic: month/year stepping must handle month lengths, leap years, and end-of-month anchoring sensibly (e.g., Jan 31 + 1 month = Feb 28/29, not Mar 3). Output dates as strings per requested format: `YYYY-MM-DD` (default) or `DD.MM.YYYY`.

### 3. `inclusive=False` behavior
When the boundaries are exclusive, treat `Min` and `Max` as invalid (out of bounds) and derive the nearest valid interior points (`Min + S`, `Max - S`) as the boundary-adjacent valid values; badge accordingly. (Spec lists inclusive checkbox as a form option; define the semantics here.)

### 4. String Length generator
Given `Min`/`Max` lengths and a filler strategy (`Repeat char`, e.g. `'a'`, or `Random ASCII`), generate actual strings of lengths: `0`, `Min-1`, `Min`, `Min+1`, `Nominal`, `Max-1`, `Max`, `Max+1` — deduplicated, sorted ascending — handling `0` and negative length bounds safely (skip lengths < 0; length `0` yields empty string, description notes it).
- Status mapping: lengths `Min..Max` (inclusive) → Valid/Boundary at the edges; lengths outside → Invalid. Nominal length = middle of range.

### 5. Tests
- `bva/tests.py` (or `tests/` package): unit-test `services.py` directly with plain assertions (Django TestCase or pytest-style, runner available via `manage.py test`).
- Cover: integer happy path, floats with decimal precision, date steps incl. leap year (Feb 29) and month-end, inclusive vs exclusive, string-length deduplication and zero/negative handling, error cases.

## Done when
- `python manage.py test bva` passes with full coverage of the above cases.
- `services.py` imports no Django modules (pure Python + stdlib only).
