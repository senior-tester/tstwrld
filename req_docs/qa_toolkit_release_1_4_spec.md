# Task 4 of 6 — Dirty Strings Catalog: `dirty_strings/presets.py`

Depends on: Task 1 (the `dirty_strings/` app package exists). Independent of Tasks 2 and 3 (pure data + trivial helpers, no UI). The view/UI wiring comes in Task 5.

## Goal
Build the curated catalog of Special & Dirty Strings as a structured, pure-Python data module in `dirty_strings/presets.py`, plus its custom-length string generator helper, with unit tests. This is the single source of truth for all payloads and categories in the spec.

## Prerequisites (already done in Task 1)
- `dirty_strings/` app package exists.

## What to build

### 1. Data model
A structured catalog, e.g.:

```python
@dataclass(frozen=True)
class Payload:
    label: str          # human-readable, e.g. "XSS via Image Tag"
    value: str          # the actual string
    note: str = ""      # optional explanation

PRESETS: list[PresetCategory]  # ordered list of {key, title, payloads}
```

Categories (order and contents exactly per spec section 3):

1. **Whitespace & Empty Strings** — empty string `""`; whitespace-only (`"   "`, tab, newline); zero-width spaces (`\u200B`, `\uFEFF`, `\u200C`); `"  leading and trailing  "`.
2. **Long Strings & Buffer Limits** — fixed-length strings of exactly `255`, `256`, `512`, `1024`, `4096` characters; one long continuous string without spaces (UI overflow probe). Note: the *interactive custom generator* is a UI concern (Task 5), but expose the pure helper here.
3. **Unicode, Emojis & Internationalization** — single emoji (`🔥`), compound ZWJ sequence (`👨‍👩‍👧‍👦`), skin-tone modifier (`👍🏽`); non-Latin scripts & diacritics (`日本語`, `中文`, `Zålgø tēxt`); RTL strings (`مرحبا`, `שלום`).
4. **Security & Injection Payloads (Basic)** — XSS: `<script>alert(1)</script>`, `<img src=x onerror=alert(1)>`; SQLi: `' OR '1'='1`, `admin' --`, `1; DROP TABLE users;`; HTML/template injection: `<b>bold</b>`, `{{ 7*7 }}`, `${7*7}`, `%s%s%s%s`; path traversal: `../../../../etc/passwd`, `..\..\..\windows\win.ini`.
5. **Numeric & System Edge Cases** — `0`, `-0`, `000123`, `NaN`, `Infinity`, `-Infinity`, `1e308`, `null`, `undefined`, `true`, `false` (as literal strings).

Every payload needs a label/description (invent clear ones where the spec doesn't name them).

### 2. Helper functions
```python
def all_payloads() -> list[Payload]               # flattened, ordered
def search_payloads(query: str) -> list[Payload]  # case-insensitive match on label/value
def generate_custom_string(length: int, char: str = "a") -> str
```
- `generate_custom_string` validates `length >= 0` and a single-character filler (allow explicit "random" mode returning random printable ASCII of the requested length).

### 3. Tests
- Unit-test in `dirty_strings/tests.py`: every category present and non-empty; fixed-length strings have exact lengths; ZWJ/emoji values contain the expected codepoints; search finds known labels case-insensitively; generator length/edge behavior (`0`, `1`, large) and validation errors.

## Done when
- `python manage.py test dirty_strings` passes.
- `presets.py` imports no Django modules (pure data module).
