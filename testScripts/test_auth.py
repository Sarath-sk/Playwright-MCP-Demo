import json
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

from pageObjects.auth_page import AuthPage


with (Path(__file__).resolve().parents[1] / "testData" / "auth_data.json").open(
    encoding="utf-8"
) as data_file:
    AUTH_DATA = json.load(data_file)


@pytest.mark.smoke
@pytest.mark.regression
def test_successful_login_with_standard_user(page: Page, base_url: str) -> None:
    auth_page = AuthPage(page, AUTH_DATA["inventory_heading"])
    auth_page.navigate_to(base_url)
    user = AUTH_DATA["valid_user"]

    auth_page.login(user["username"], user["password"])

    expect(auth_page.inventory_heading).to_be_visible()
    expect(page).to_have_url(f"{base_url}{AUTH_DATA['inventory_path']}")


@pytest.mark.regression
def test_locked_out_user_validation(page: Page, base_url: str) -> None:
    auth_page = AuthPage(page, AUTH_DATA["inventory_heading"])
    auth_page.navigate_to(base_url)
    user = AUTH_DATA["locked_user"]

    auth_page.login(user["username"], user["password"])

    expect(auth_page.error_message).to_contain_text(user["error_message"])
    expect(auth_page.username_input).to_be_visible()


@pytest.mark.regression
def test_empty_username_submission(page: Page, base_url: str) -> None:
    auth_page = AuthPage(page, AUTH_DATA["inventory_heading"])
    auth_page.navigate_to(base_url)

    auth_page.submit_login()

    expect(auth_page.error_message).to_contain_text(
        AUTH_DATA["empty_username_error"]
    )
    expect(auth_page.username_input).to_be_visible()


@pytest.mark.regression
def test_empty_password_submission(page: Page, base_url: str) -> None:
    auth_page = AuthPage(page, AUTH_DATA["inventory_heading"])
    auth_page.navigate_to(base_url)
    user = AUTH_DATA["valid_user"]

    auth_page.login(user["username"], AUTH_DATA["empty_value"])

    expect(auth_page.error_message).to_contain_text(
        AUTH_DATA["empty_password_error"]
    )
    expect(auth_page.username_input).to_be_visible()


@pytest.mark.regression
def test_invalid_credentials(page: Page, base_url: str) -> None:
    auth_page = AuthPage(page, AUTH_DATA["inventory_heading"])
    auth_page.navigate_to(base_url)
    user = AUTH_DATA["invalid_user"]

    auth_page.login(user["username"], user["password"])

    expect(auth_page.error_message).to_contain_text(user["error_message"])
    expect(auth_page.username_input).to_be_visible()
