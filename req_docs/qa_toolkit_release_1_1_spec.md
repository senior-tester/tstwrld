# Task 1 of 6 — Project Skeleton: Django Setup & Core Layout

Full spec for this milestone: see `req_docs/qa_toolkit_release_1_spec.md` (section 4 for structure, section 1 for UI guidelines). This task is the foundation for all subsequent tasks; nothing from the spec's features is implemented yet, but the app must run and render the shared layout.

## Goal
Set up a runnable Django 5.x project with the exact directory structure from the spec, and implement the shared UI shell (base template, header, sidebar) that both feature apps will inherit from.

## Prerequisites
- None. This is the first task. The `.venv/` exists but is empty — create it or install Django 5.x (Python 3.11+) into it.

## What to build

### 1. Project bootstrap
- Create `manage.py` and the `config/` package (`settings.py`, `urls.py`, `wsgi.py`) via `django-admin startproject config`.
- Create two Django apps: `core/`, plus empty placeholder apps `bva/` and `dirty_strings/` (only `apps.py`, `views.py`, `urls.py`, `templates/` skeleton — no feature logic yet). Final structure must match the tree in spec section 4:
  ```text
  manage.py
  config/{settings.py, urls.py, wsgi.py}
  core/{views.py, urls.py, templates/base.html, templates/components/header.html, templates/components/sidebar.html}
  bva/{views.py, urls.py, templates/bva/index.html}
  dirty_strings/{views.py, urls.py, templates/dirty_strings/index.html}
  ```
- Register `core`, `bva`, `dirty_strings` in `INSTALLED_APPS`; wire their `urls.py` includes in `config/urls.py` (`/`, `/bva/`, `/dirty-strings/`).

### 2. Shared layout (`core/templates/`)
- `base.html`: loads **Tailwind CSS via CDN** and **Alpine.js via CDN** (no Node build pipeline). Defines the overall two-column page structure: header on top, left sidebar, main content area. Provides `{% block content %}` for feature pages.
- `components/header.html`: app name `QA Toolkit` with a subtle badge `v0.1.0-alpha`, a theme toggle button (Dark/Light), and a link to the GitHub repository.
- `components/sidebar.html`: left navigation with entries:
  - 📐 Boundary Values (BVA) — active, links to `/bva/`
  - 🧪 Special & Dirty Strings — active, links to `/dirty-strings/`
  - ⏳ *All Pairs* — disabled, labeled "Coming in v0.2"
  - ⏳ *JSON/JWT Inspector* — disabled, labeled "Coming in v0.2"

### 3. Theme (dark/light mode)
- Automatic system preference detection on first visit (prefers-color-scheme), manual toggle persisted in `localStorage`. Implement with a tiny inline vanilla JS snippet in `base.html` (set the `dark` class on `<html>` before paint to avoid flicker).
- Aesthetic: clean modern developer style (Linear/Vercel-like). Monospace font utility class for code/test-data snippets (used heavily in later tasks).

### 4. Placeholder feature pages
- `bva/templates/bva/index.html` and `dirty_strings/templates/dirty_strings/index.html`: minimal pages extending `base.html`, each with a heading only. Their two-column input/output split will be filled by later tasks.

## Done when
- `python manage.py migrate` and `runserver` succeed; `/`, `/bva/`, `/dirty-strings/` render the shared header/sidebar with theme toggle working in both directions.
- Directory structure matches the spec exactly.
