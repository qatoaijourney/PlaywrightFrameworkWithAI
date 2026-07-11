from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    # Locators
    SHOPPING_CART = ".shopping_cart_link"
    TITLE = ".title"
    ADD_TO_CART_BUTTON = "button[data-test='add-to-cart-sauce-labs-backpack']"
    REMOVE_BUTTON = "button[data-test='remove-sauce-labs-backpack']"

    def open_inventory(self) -> None:
        self.open("/inventory.html")

    def is_inventory_page_open(self) -> bool:
        return self.is_visible(self.TITLE)

    def add_backpack_to_cart(self) -> None:
        self.click(self.ADD_TO_CART_BUTTON)

    def remove_backpack_from_cart(self) -> None:
        self.click(self.REMOVE_BUTTON)

    def open_cart(self) -> None:
        self.click(self.SHOPPING_CART)

    def get_page_title(self) -> str:
        return self.get_text(self.TITLE)
