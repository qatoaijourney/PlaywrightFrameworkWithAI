from typing import Optional
import re

from playwright.sync_api import Page, Locator, expect

from pages.base_page import BasePage
from config.settings import UI_TESTING_PLAYGROUND_URL, DEFAULT_TIMEOUT


class SampleLoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def _username_locator(self) -> Locator:
        candidates = [
            lambda: self.page.get_by_placeholder("Username"),
            lambda: self.page.get_by_placeholder("username"),
            lambda: self.page.get_by_label("Username"),
            lambda: self.page.get_by_label("username"),
            lambda: self.page.locator("input[name='username']"),
            lambda: self.page.locator("input[type='text']").first,
        ]
        for c in candidates:
            try:
                loc = c()
                if loc is not None and loc.count() and loc.is_visible():
                    return loc
            except Exception:
                continue
        return self.page.locator("input").first

    def _password_locator(self) -> Locator:
        candidates = [
            lambda: self.page.get_by_placeholder("Password"),
            lambda: self.page.get_by_placeholder("password"),
            lambda: self.page.get_by_label("Password"),
            lambda: self.page.locator("input[type='password']"),
        ]
        for c in candidates:
            try:
                loc = c()
                if loc is not None and loc.count() and loc.is_visible():
                    return loc
            except Exception:
                continue
        return self.page.locator("input[type='password']")

    def _login_button_locator(self) -> Locator:
        try:
            btn = self.page.get_by_role("button", name=re.compile(r"Log In|Log Out", re.I))
            if btn.count():
                return btn
        except Exception:
            pass
        return self.page.locator("button:has-text('Log In')").first

    def open_login_page(self) -> None:
        target = f"{UI_TESTING_PLAYGROUND_URL.rstrip('/')}/sampleapp"
        self.open(target)

    def enter_username(self, username: str) -> None:
        loc = self._username_locator()
        expect(loc).to_be_visible(timeout=DEFAULT_TIMEOUT)
        loc.fill(username)

    def enter_password(self, password: str) -> None:
        loc = self._password_locator()
        expect(loc).to_be_visible(timeout=DEFAULT_TIMEOUT)
        loc.fill(password)

    def click_login(self) -> None:
        btn = self._login_button_locator()
        expect(btn).to_be_visible(timeout=DEFAULT_TIMEOUT)
        btn.click()

    def submit_login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_status_text(self) -> str:
        for txt in ("User logged out.", "Invalid username/password", "Welcome"):
            loc = self.page.locator(f"text={txt}")
            try:
                if loc.count() and loc.is_visible():
                    return loc.inner_text()
            except Exception:
                continue
        return ""

    def get_error_message(self) -> str:
        loc = self.page.locator("text=Invalid username/password")
        try:
            if loc.count():
                return loc.inner_text()
        except Exception:
            pass
        return ""

    def is_login_button_text(self, text: str) -> bool:
        try:
            btn = self.page.get_by_role("button", name=text)
            return btn.count() > 0 and btn.is_visible()
        except Exception:
            loc = self.page.locator(f"button:has-text('{text}')")
            try:
                return loc.count() > 0 and loc.is_visible()
            except Exception:
                return False

    def are_fields_empty(self) -> bool:
        try:
            u = self._username_locator()
            p = self._password_locator()
            return (u.input_value().strip() == "") and (p.input_value().strip() == "")
        except Exception:
            return False

    def click_logout(self) -> None:
        btn = self.page.get_by_role("button", name="Log Out")
        if btn.count():
            btn.click()
        else:
            self.page.locator("button:has-text('Log Out')").first.click()

    def is_logged_in(self, username: Optional[str] = None) -> bool:
        if username:
            welcome = f"Welcome, {username}!"
            loc = self.page.locator(f"text={welcome}")
            try:
                return loc.count() > 0 and loc.is_visible()
            except Exception:
                return False
        loc = self.page.get_by_text("Welcome")
        try:
            return loc.count() > 0 and loc.is_visible()
        except Exception:
            return False
