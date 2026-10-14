import time
import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Checkout")
@pytest.mark.ui
@pytest.mark.e2e
class TestCheckoutVariants:

    def _prepare_cart_and_login(self, products_page, cart_page, page, registered_user, login_page):
        products_page.open()
        products_page.add_first_to_cart()
        cart_page.open()
        cart_page.expect_items_count(1)

        login_page.open()
        login_page.login(registered_user["email"], registered_user["password"])
        login_page.expect_logged_in()

        cart_page.open()
        page.click("a:has-text('Proceed To Checkout')")

    def _fill_payment_and_verify(self, checkout_page):
        checkout_page.place_order_with_comment("Fast delivery please")
        checkout_page.enter_payment_details(
            "Test User", "4111111111111111", "123", "12", "2028"
        )
        checkout_page.expect_order_success()

    @allure.story("TC16: Place order - login before checkout")
    def test_place_order_login_before_checkout(
        self, products_page, cart_page, page, registered_user, login_page, checkout_page
    ):
        self._prepare_cart_and_login(products_page, cart_page, page, registered_user, login_page)
        self._fill_payment_and_verify(checkout_page)

    @allure.story("TC23: Verify address details in checkout")
    def test_verify_address_in_checkout(
        self, products_page, cart_page, page, registered_user, login_page, checkout_page
    ):
        self._prepare_cart_and_login(products_page, cart_page, page, registered_user, login_page)
        checkout_page.expect_delivery_address_contains(registered_user["data"]["firstname"])
        checkout_page.expect_delivery_address_contains(registered_user["data"]["city"])

    @allure.story("TC24: Download invoice after purchase")
    def test_download_invoice(
        self, products_page, cart_page, page, registered_user, login_page, checkout_page
    ):
        self._prepare_cart_and_login(products_page, cart_page, page, registered_user, login_page)
        self._fill_payment_and_verify(checkout_page)

        download = checkout_page.download_invoice()
        assert download.suggested_filename.startswith("invoice")