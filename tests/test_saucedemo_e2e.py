from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_saucedemo_end_to_end(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_inventory_page_open()

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    checkout_page.open("/checkout-step-one.html")
    checkout_page.complete_checkout("John", "Doe", "560001")

    assert "Thank you for your order!" in checkout_page.get_complete_header()
