from pages.BasePage import BasePage
from playwright.sync_api import expect


class CartPage(BasePage):
    URL = "https://automationexercise.com/view_cart"

    CART_ROWS = "#cart_info_table tbody tr"
    EMPTY_CART = "#empty_cart"

    def open(self):
        self.navigate_to(self.URL)
        return self

    def expect_items_count(self, count: int):
        expect(self.page.locator(self.CART_ROWS)).to_have_count(count)
        return self

    def expect_empty(self):
        expect(self.page.locator(self.EMPTY_CART)).to_be_visible()
        return self