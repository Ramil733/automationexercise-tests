from pages.BasePage import BasePage
from playwright.sync_api import expect


class CheckoutPage(BasePage):
    URL = "https://automationexercise.com/checkout"

    ADDRESS_DETAILS = "#address_delivery"
    REVIEW_ORDER = "#cart_info"
    COMMENT_INPUT = "textarea[name='message']"
    PLACE_ORDER_BTN = "a:has-text('Place Order')"

    NAME_ON_CARD = "input[data-qa='name-on-card']"
    CARD_NUMBER = "input[data-qa='card-number']"
    CVC = "input[data-qa='cvc']"
    EXPIRY_MONTH = "input[data-qa='expiry-month']"
    EXPIRY_YEAR = "input[data-qa='expiry-year']"
    PAY_BTN = "button[data-qa='pay-button']"

    SUCCESS_MSG = "h2:has-text('Order Placed!')"

    DELIVERY_ADDRESS = "#address_delivery"
    INVOICE_DOWNLOAD = "a:has-text('Download Invoice')"

    def open(self):
        self.navigate_to(self.URL)
        return self

    def place_order_with_comment(self, comment: str):
        self.page.fill(self.COMMENT_INPUT, comment)
        self.page.click(self.PLACE_ORDER_BTN)
        return self

    def enter_payment_details(
        self, name: str, card: str, cvc: str, month: str, year: str
    ):
        self.page.fill(self.NAME_ON_CARD, name)
        self.page.fill(self.CARD_NUMBER, card)
        self.page.fill(self.CVC, cvc)
        self.page.fill(self.EXPIRY_MONTH, month)
        self.page.fill(self.EXPIRY_YEAR, year)
        self.page.click(self.PAY_BTN)
        return self

    def expect_order_success(self):
        expect(self.page.locator(self.SUCCESS_MSG)).to_be_visible()
        return self

    def expect_delivery_address_contains(self, text: str):
        expect(self.page.locator(self.DELIVERY_ADDRESS)).to_contain_text(text)
        return self

    def download_invoice(self):
        with self.page.expect_download() as download_info:
            self.page.click(self.INVOICE_DOWNLOAD)
        download = download_info.value
        return download
