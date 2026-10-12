from pages.BasePage import BasePage
from playwright.sync_api import expect


class HomePage(BasePage):
    URL = "https://automationexercise.com"

    # Локаторы
    PRODUCTS_LINK = "a[href='/products']"
    CART_LINK = "a[href='/view_cart']"
    SIGNUP_LOGIN_LINK = "a[href='/login']"
    
    def open(self):
        self.navigate_to(self.URL)
        return self

    def go_to_products(self):
        self.page.click(self.PRODUCTS_LINK)
        return self

    def go_to_cart(self):
        self.page.click(self.CART_LINK)
        return self

    def go_to_login(self):
        self.page.click(self.SIGNUP_LOGIN_LINK)
        return self

    def expect_loaded(self):
        expect(self.page).to_have_title("Automation Exercise")
        return self