from pages.BasePage import BasePage
from playwright.sync_api import expect


class ProductPage(BasePage):
    URL = "https://automationexercise.com/products"

    SEARCH_INPUT = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    PRODUCT_CARDS = ".productinfo"
    ADD_TO_CART_BTN = ".add-to-cart"
    CONTINUE_SHOPPING_BTN = "button:has-text('Continue Shopping')"
    VIEW_CART_LINK = "u:has-text('View Cart')"

    def open(self):
        self.navigate_to(self.URL)
        return self

    def search_for(self, product_name: str):
        self.page.fill(self.SEARCH_INPUT, product_name)
        self.page.click(self.SEARCH_BUTTON)
        return self

    def add_first_to_cart(self):
        first_card = self.page.locator(self.PRODUCT_CARDS).first
        first_card.hover()
        first_card.locator(self.ADD_TO_CART_BTN).click()
        expect(self.page.locator(".modal-content")).to_be_visible()
        self.page.click(self.CONTINUE_SHOPPING_BTN)
        return self

    def expect_results_count(self, count: int):
        expect(self.page.locator(self.PRODUCT_CARDS)).to_have_count(count)
        return self

    def expect_no_results(self):
        expect(self.page.locator(self.PRODUCT_CARDS)).to_have_count(0)
        return self