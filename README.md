# Playwright MCP Demo

A Python + pytest-playwright UI automation project for the SauceDemo application. It contains a manual auth test plan and Page Object Model automation for its login scenarios.

## Requirements

- macOS or another supported Playwright platform
- Python 3.9 or later
- A browser-capable desktop session: `pytest.ini` configures Chromium to run headed

## Set up the project

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pytest pytest-playwright
playwright install chromium
```

If the virtual environment already exists, activate it with `source .venv/bin/activate` and continue with the test command.

## Run the auth tests

```bash
pytest testScripts/test_auth.py
```

The project configuration also supports running all discovered tests with:

```bash
pytest
```

Pytest uses `pytest.ini` to add the repository root to the Python import path, discover tests under `testScripts/`, and launch Chromium headed.

## Auth test coverage

The manual scenarios are documented in [testcases/auth.md](testcases/auth.md) and [testcases/auth.csv](testcases/auth.csv). Automated coverage in [testScripts/test_auth.py](testScripts/test_auth.py) includes:

- Successful login with the standard user
- Locked-out user validation
- Empty username submission
- Empty password submission
- Invalid credentials

Test credentials and expected validation messages are maintained in [testData/auth_data.json](testData/auth_data.json). Login page interactions and locators are encapsulated in [pageObjects/auth_page.py](pageObjects/auth_page.py), which inherits from [pageObjects/base_page.py](pageObjects/base_page.py).

## Work completed and verification

The auth module was created from the manual test scenarios, then its test collection and browser locators were corrected:

1. Added test data, the auth page object, and pytest tests for all five scenarios.
2. Configured `pythonpath = .` in `pytest.ini` so imports such as `pageObjects.auth_page` resolve when pytest is run from the repository root.
3. Updated the `BasePage.navigate_to` return annotation to `Optional[Response]`, which is compatible with the project's Python 3.9 runtime.
4. Matched the inventory and login-error locators to the observed accessibility snapshot: the inventory title is text and validation errors have the `alert` role.
5. Ran `pytest testScripts/test_auth.py` twice consecutively after the locator fix. Both runs completed successfully with **5 passed**.

The locator fix and test results are recorded in [healerReport/auth_heal_report.md](healerReport/auth_heal_report.md).