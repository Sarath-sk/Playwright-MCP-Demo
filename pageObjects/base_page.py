from typing import Optional

from playwright.sync_api import Page, Response

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str) -> Optional[Response]:
        return self.page.goto(url, wait_until="domcontentloaded")

    def wait_for_url(self, url_pattern: str):
        self.page.wait_for_url(url_pattern)
