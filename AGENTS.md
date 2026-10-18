# AGENTS.md

## Repo state

- **Greenfield project.** Only a spec exists (`req_docs/qa_toolkit_release_1_spec.md`); no code yet. Treat the spec as the source of truth for architecture and features.
- `README.md` is a placeholder (a stray `tstwrld` line, likely accidental).

## Project: QA Toolkit (Django)

- Python 3.11+ (system python3 is 3.12; `.venv/` exists but is empty — install Django yourself, it's not there).
- Django 5.x, Django templates + Tailwind via CDN + vanilla JS/Alpine.js. **No Node.js build pipeline** — don't add one.
- Planned structure per spec: `manage.py`, `config/` (settings/urls/wsgi), `core/` (shared header/sidebar templates), `bva/` (Boundary Value Analysis), `dirty_strings/` (Special & Dirty Strings).
- Key convention: business logic lives in `bva/services.py` and `dirty_strings/presets.py`, decoupled from views, so it stays unit-testable. BVA uses the standard 7-point boundary model with a `step` parameter.

## Working style

- This repo uses the Kilo code-authoring pipeline (`.kilo/skills/code-authoring-pipeline/`, sub-agents in `.kilo/agent/`): DRIVER owns branches; only CODER edits code; planner/reviewer are read-only.
- Domain skills exist in `.kilo/skills/` (django-patterns, django-tdd, django-verification, python-patterns) — load the relevant one before writing Django code.
