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

    BRAND_LINK = "a[href='/brand_products/{brand}']"
    WRITE_REVIEW_LINK = "a:has-text('Write Your Review')"
    REVIEW_NAME = "#name"
    REVIEW_EMAIL = "#email"
    REVIEW_TEXT = "#review"
    REVIEW_SUBMIT = "#button-review"
    REVIEW_SUCCESS = "span:has-text('Thank you for your review.')"
    RECOMMENDED_ITEMS = ".recommended_items"
    RECOMMENDED_ADD_TO_CART = ".recommended_items .add-to-cart"

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

    def open_brand(self, brand_name: str):
        self.page.click(f"a[href='/brand_products/{brand_name}']")
        return self

    def submit_review(self, name: str, email: str, review: str):
        self.page.click(self.WRITE_REVIEW_LINK)
        self.page.fill(self.REVIEW_NAME, name)
        self.page.fill(self.REVIEW_EMAIL, email)
        self.page.fill(self.REVIEW_TEXT, review)
        self.page.click(self.REVIEW_SUBMIT)
        return self

    def expect_review_success(self):
        expect(self.page.locator(self.REVIEW_SUCCESS)).to_be_visible()
        return self

    def add_recommended_to_cart(self):
        self.page.locator(self.RECOMMENDED_ADD_TO_CART).first.click()
        expect(self.page.locator(".modal-content")).to_be_visible()
        return self
