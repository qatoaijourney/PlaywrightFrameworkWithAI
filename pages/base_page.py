from pathlib import Path
from typing import Union

from playwright.sync_api import Locator, Page, expect

from config.settings import BASE_URL, DEFAULT_TIMEOUT, REPORTS_DIR


class BasePage:
    def __init__(self, page: Page, base_url: str = BASE_URL):
        self.page = page
        self.base_url = base_url.rstrip("/") if base_url else ""

    def open(self, path: str = "/") -> None:
        target = path if path.startswith("http") else f"{self.base_url}{path}"
        self.page.goto(target, wait_until="load")
        self.page.wait_for_load_state("domcontentloaded")

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_element(self, locator: Union[Locator, str], timeout: int = DEFAULT_TIMEOUT) -> Locator:
        element = self.page.locator(locator) if isinstance(locator, str) else locator
        expect(element).to_be_visible(timeout=timeout)
        return element

    def click(self, locator: Union[Locator, str], timeout: int = DEFAULT_TIMEOUT) -> None:
        element = self.wait_for_element(locator, timeout=timeout)
        element.click()

    def type_text(self, locator: Union[Locator, str], text: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        element = self.wait_for_element(locator, timeout=timeout)
        element.fill(text)

    def get_text(self, locator: Union[Locator, str], timeout: int = DEFAULT_TIMEOUT) -> str:
        element = self.wait_for_element(locator, timeout=timeout)
        return element.inner_text()

    def is_visible(self, locator: Union[Locator, str], timeout: int = DEFAULT_TIMEOUT) -> bool:
        element = self.page.locator(locator) if isinstance(locator, str) else locator
        try:
            expect(element).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False

    def scroll_into_view(self, locator: Union[Locator, str], timeout: int = DEFAULT_TIMEOUT) -> None:
        element = self.wait_for_element(locator, timeout=timeout)
        element.scroll_into_view_if_needed()

    def take_screenshot(self, name: str, full_page: bool = True) -> Path:
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        file_path = REPORTS_DIR / f"{name}.png"
        self.page.screenshot(path=str(file_path), full_page=full_page)
        return file_path
