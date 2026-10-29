from playwright.sync_api import Page

from pageObjects.base_page import BasePage


class AuthPage(BasePage):
    def __init__(self, page: Page, inventory_heading: str):
        super().__init__(page)
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_role("alert")
        self.inventory_heading = page.get_by_text(
            inventory_heading, exact=True
        )

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def submit_login(self) -> None:
        self.login_button.click()
