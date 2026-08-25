import base64
import os
from typing import Any

import pytest
from playwright.sync_api import sync_playwright

from config.settings import BASE_URL

try:
    from pytest_html import extras as html_extras
    from pytest_html.fixtures import extras_stash_key
except ImportError:  # pragma: no cover - pytest-html may be absent in some environments
    html_extras = None
    extras_stash_key = None


os.environ.setdefault("BASE_URL", BASE_URL)


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="function")
def browser(playwright_instance):
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    browser = playwright_instance.chromium.launch(headless=headless)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page


@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_makereport(item: Any, call: Any):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed and html_extras is not None and extras_stash_key is not None:
        page = item.funcargs.get("page")
        if page is not None:
            screenshot_bytes = page.screenshot(full_page=True)
            item.config.stash.setdefault(extras_stash_key, []).append(
                html_extras.image(
                    base64.b64encode(screenshot_bytes).decode("utf-8"),
                    name=f"{item.name} failure screenshot",
                )
            )
