import re
from pytest_bdd import given, scenarios, when, then, parsers
from playwright.sync_api import expect

from pages.sample_login_page import SampleLoginPage

scenarios("../features/sample_app_login.feature")
@given(parsers.parse('I open the Sample Application login page at "{url}"'))
def open_sample_login(page, url):
    p = SampleLoginPage(page)
    p.open(url)
    return p


@given('I am on the login page')
def on_login_page(page):
    p = SampleLoginPage(page)
    p.open_login_page()
    return p


@when('the page finishes loading')
def page_loaded(page):
    page.wait_for_load_state("domcontentloaded")


@given(parsers.parse('the username field is populated with "{username}"'))
def populate_username(page, username):
    p = SampleLoginPage(page)
    p.enter_username(username)


@given('the username field is empty')
def given_username_empty(page):
    p = SampleLoginPage(page)
    loc = p._username_locator()
    loc.fill("")


@given(parsers.parse('the password field is populated with "{password}"'))
def populate_password(page, password):
    p = SampleLoginPage(page)
    p.enter_password(password)


@when('I submit the login form')
def submit_login(page):
    p = SampleLoginPage(page)
    p.click_login()


@then(parsers.parse('the status should state "{text}"'))
def assert_status(page, text):
    p = SampleLoginPage(page)
    status = p.get_status_text()
    assert text in status


@then(parsers.parse('the login button should display "{text}"'))
def assert_button_text(page, text):
    p = SampleLoginPage(page)
    assert p.is_login_button_text(text)


@then(parsers.parse('the login button should continue to display "{text}"'))
def assert_button_text_continue(page, text):
    p = SampleLoginPage(page)
    assert p.is_login_button_text(text)


@then('the username and password fields should be empty')
def assert_fields_empty(page):
    p = SampleLoginPage(page)
    assert p.are_fields_empty()


@then('the username and password fields should be cleared or not visible as part of logged-in UI')
def fields_cleared_or_hidden(page):
    p = SampleLoginPage(page)
    empty = p.are_fields_empty()
    u_vis = False
    p_vis = False
    try:
        u_vis = p._username_locator().is_visible()
    except Exception:
        u_vis = False
    try:
        p_vis = p._password_locator().is_visible()
    except Exception:
        p_vis = False
    assert empty or (not u_vis and not p_vis)


@then(parsers.parse('I should see "{welcome}"'))
def assert_welcome(page, welcome):
    p = SampleLoginPage(page)
    assert welcome == p.get_status_text()


@then(parsers.parse('the username field should be empty'))
def username_empty(page):
    p = SampleLoginPage(page)
    u = p._username_locator()
    assert u.input_value().strip() == ""


@then(parsers.parse('the password field should be empty'))
def password_empty(page):
    p = SampleLoginPage(page)
    pwd = p._password_locator()
    assert pwd.input_value().strip() == ""


@given(parsers.parse('I am logged in as "{username}"'))
def ensure_logged_in(page, username):
    p = SampleLoginPage(page)
    p.open_login_page()
    p.submit_login(username, "pwd")
    assert p.is_logged_in(username)
    return p


@when('I click the "Log Out" button')
def click_logout(page):
    p = SampleLoginPage(page)
    p.click_logout()


@then('the user should be logged out')
def assert_logged_out(page):
    p = SampleLoginPage(page)
    assert "User logged out." in p.get_status_text()
