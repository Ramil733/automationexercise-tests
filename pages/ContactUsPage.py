from pages.BasePage import BasePage
from playwright.sync_api import expect


class ContactUsPage(BasePage):
    URL = "https://automationexercise.com/contact_us"

    NAME = "input[data-qa='name']"
    EMAIL = "input[data-qa='email']"
    SUBJECT = "input[data-qa='subject']"
    MESSAGE = "textarea[data-qa='message']"
    SUBMIT_BTN = "input[data-qa='submit-button']"
    SUCCESS_MSG = ".status.alert.alert-success"

    def open(self):
        self.navigate_to(self.URL)
        return self

    def submit_form(self, name: str, email: str, subject: str, message: str):
        self.page.fill(self.NAME, name)
        self.page.fill(self.EMAIL, email)
        self.page.fill(self.SUBJECT, subject)
        self.page.fill(self.MESSAGE, message)

        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.click(self.SUBMIT_BTN)
        return self

    def expect_success(self):
        expect(self.page.locator(self.SUCCESS_MSG)).to_be_visible()
        return self