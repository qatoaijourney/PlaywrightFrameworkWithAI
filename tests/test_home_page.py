from pages.home_page import HomePage


def test_home_page_title(page):
    home_page = HomePage(page)
    home_page.open_home()

    assert "Example Domain" in home_page.get_title()
