from pages.BasePage import BasePage
from playwright.sync_api import expect


class SignupPage(BasePage):
    # Локаторы формы
    TITLE_MR = "#id_gender1"
    PASSWORD = "#password"
    DAY = "#days"
    MONTH = "#months"
    YEAR = "#years"
    NEWSLETTER = "#newsletter"
    OPTIN = "#optin"

    FIRST_NAME = "#first_name"
    LAST_NAME = "#last_name"
    COMPANY = "#company"
    ADDRESS1 = "#address1"
    ADDRESS2 = "#address2"
    COUNTRY = "#country"
    STATE = "#state"
    CITY = "#city"
    ZIPCODE = "#zipcode"
    MOBILE = "#mobile_number"

    CREATE_ACCOUNT_BUTTON = "button[data-qa='create-account']"
    ACCOUNT_CREATED = "h2:has-text('Account Created!')"
    CONTINUE_BUTTON = "a[data-qa='continue-button']"

    def fill_account_info(self, password: str):
        self.page.check(self.TITLE_MR)
        self.page.fill(self.PASSWORD, password)
        self.page.select_option(self.DAY, "15")
        self.page.select_option(self.MONTH, "6")
        self.page.select_option(self.YEAR, "1995")
        self.page.check(self.NEWSLETTER)
        self.page.check(self.OPTIN)
        return self

    def fill_address_info(self, data: dict):
        self.page.fill(self.FIRST_NAME, data["first_name"])
        self.page.fill(self.LAST_NAME, data["last_name"])
        self.page.fill(self.COMPANY, data["company"])
        self.page.fill(self.ADDRESS1, data["address1"])
        self.page.fill(self.ADDRESS2, data["address2"])
        self.page.select_option(self.COUNTRY, "United States")
        self.page.fill(self.STATE, data["state"])
        self.page.fill(self.CITY, data["city"])
        self.page.fill(self.ZIPCODE, data["zipcode"])
        self.page.fill(self.MOBILE, data["mobile"])
        return self

    def create_account(self):
        self.page.click(self.CREATE_ACCOUNT_BUTTON)
        return self

    def expect_account_created(self):
        expect(self.page.locator(self.ACCOUNT_CREATED)).to_be_visible()
        return self

    def continue_after_creation(self):
        self.page.click(self.CONTINUE_BUTTON)
        return self
