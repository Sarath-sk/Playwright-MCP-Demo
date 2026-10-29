import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://www.saucedemo.com"
