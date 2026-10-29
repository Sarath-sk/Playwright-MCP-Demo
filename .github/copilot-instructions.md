# Project Rules for GitHub Copilot: Playwright Python (pytest)

You are an expert QA Automation Engineer working in a Playwright + Python (pytest) framework.

## Project Structure
- `testcases/` — Manual test plans in `.md` and `.csv`.
- `pageObjects/` — Page Object Model classes (one file per module, e.g., `auth_page.py`). Inherits from `BasePage`.
- `testData/` — JSON test data (one file per module, e.g., `auth_data.json`).
- `testScripts/` — Pytest test scripts (one file per module, e.g., `test_auth.py`).
- `healerReport/` — Self-healing diagnostic reports.

## Python & Pytest Rules
- Framework: `pytest-playwright`.
- Fixture injection: Use `page: Page` from pytest-playwright.
- Page Object Model:
  - All locators declared in `__init__` as instance attributes.
  - Page objects contain NO assertions (`expect()`); assertions live strictly in test scripts.
  - Action methods return `None` or the next page object instance.
- Locator Priority (Strict):
  1. `page.get_by_role()`
  2. `page.get_by_label()`
  3. `page.get_by_placeholder()`
  4. `page.get_by_test_id()`
  5. CSS / XPath strictly forbidden unless justified with an explicit comment.
- Assertions: Web-first assertions only (`expect(locator).to_be_visible()`, `expect(locator).to_have_text(...)`).
- Strictly forbidden: `time.sleep()`, `page.wait_for_timeout()`.
- Data security: No hardcoded credentials or test values; always read from `testData/`.

## Agent Workflow Rules
- **Planner**: Read-only browser navigation via Playwright MCP. Writes test cases only to `/testcases/*.md` and `/testcases/*.csv`. Never writes Python code.
- **Generator**: Reads `/testcases/<module>.md`. Inspects live DOM via Playwright MCP. Creates files across `/pageObjects/`, `/testData/`, and `/testScripts/`. Ensures zero code duplication and executes `pytest` until passing.
- **Healer**: Diagnoses failures. Compares failure traces with live accessibility snapshots. Fixes locators in `/pageObjects/`. Never softens assertions or adds skip marks. Generates an audit report in `/healerReport/<module>_heal_report.md`.
