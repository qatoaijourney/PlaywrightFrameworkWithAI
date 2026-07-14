import re

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    # Locators
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    # added few new methiodss

    #dsfsdfs

    def open_login_page(self) -> None:
        self.open("/")

    def enter_username(self, username: str) -> None:
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password: str) -> None:
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        expect(self.page).to_have_url(re.compile(r".*/inventory\.html"), timeout=10000)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_login_button_visible(self) -> bool:
        return self.is_visible(self.LOGIN_BUTTON)
