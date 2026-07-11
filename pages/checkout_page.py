from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    # Locators
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    COMPLETE_HEADER = ".complete-header"

    def enter_first_name(self, first_name: str) -> None:
        self.type_text(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.type_text(self.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self) -> None:
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self) -> None:
        self.click(self.FINISH_BUTTON)

    def complete_checkout(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()
        self.click_finish()

    def get_complete_header(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)
