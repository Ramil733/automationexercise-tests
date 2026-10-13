from pages.BasePage import BasePage
from playwright.sync_api import expect


class LoginPage(BasePage):
    URL = "https://automationexercise.com/login"

    # Локаторы для логина
    LOGIN_EMAIL = "input[data-qa='login-email']"
    LOGIN_PASSWORD = "input[data-qa='login-password']"
    LOGIN_BUTTON = "button[data-qa='login-button']"

    # Локаторы для регистрации
    SIGNUP_NAME = "input[data-qa='signup-name']"
    SIGNUP_EMAIL = "input[data-qa='signup-email']"
    SIGNUP_BUTTON = "button[data-qa='signup-button']"

    # Сообщения
    LOGIN_ERROR = "p:has-text('Your email or password is incorrect!')"
    LOGGED_IN_AS = "a:has-text('Logged in as')"
    LOGOUT_LINK = "a[href='/logout']"

    def open(self):
        self.navigate_to(self.URL)
        return self

    def login(self, email: str, password: str):
        self.page.fill(self.LOGIN_EMAIL, email)
        self.page.fill(self.LOGIN_PASSWORD, password)
        self.page.click(self.LOGIN_BUTTON)
        return self

    def start_signup(self, name: str, email: str):
        self.page.fill(self.SIGNUP_NAME, name)
        self.page.fill(self.SIGNUP_EMAIL, email)
        self.page.click(self.SIGNUP_BUTTON)
        return self

    def expect_login_error(self):
        expect(self.page.locator(self.LOGIN_ERROR)).to_be_visible()
        return self

    def expect_logged_in(self, username: str = None):
        expect(self.page.locator(self.LOGGED_IN_AS)).to_be_visible()
        if username:
            expect(self.page.locator(self.LOGGED_IN_AS)).to_contain_text(username)
        return self

    def logout(self):
        self.page.click(self.LOGOUT_LINK)
        return self