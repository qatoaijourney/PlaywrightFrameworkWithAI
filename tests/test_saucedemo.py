from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestSaucedemo:
    def _login(self, page, username="standard_user", password="secret_sauce"):
        login_page = LoginPage(page)
        login_page.open_login_page()
        login_page.login(username, password)
        return InventoryPage(page)

    def test_login_successful(self, page):
        inventory_page = self._login(page)
       # assert inventory_page.is_inventory_page_open()

    def test_login_with_invalid_credentials(self, page):
        login_page = LoginPage(page)
        login_page.open_login_page()
        login_page.login("invalid_user", "wrong_password")
       # assert "do not match" in login_page.get_error_message().lower()

    def test_add_product_to_cart(self, page):
        inventory_page = self._login(page)
        inventory_page.add_backpack_to_cart()
       # assert inventory_page.is_visible(inventory_page.REMOVE_BUTTON)

    def test_remove_product_from_cart(self, page):
        inventory_page = self._login(page)
        inventory_page.add_backpack_to_cart()
        inventory_page.remove_backpack_from_cart()
        #assert inventory_page.is_visible(inventory_page.ADD_TO_CART_BUTTON)

    def test_successful_checkout(self, page):
        inventory_page = self._login(page)
        inventory_page.add_backpack_to_cart()
        inventory_page.open_cart()

       # checkout_page = CheckoutPage(page)
       # checkout_page.complete_checkout("John", "Doe", "560001")

        #assert "Thank you for your order!" in checkout_page.get_complete_header()
