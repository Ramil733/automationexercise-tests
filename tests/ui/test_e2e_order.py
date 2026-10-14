import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Checkout")
@pytest.mark.ui
@pytest.mark.e2e
class TestCheckout:
    @allure.story("TC14: Place order - Register while checkout")
    def test_place_order_register_while_checkout(
        self, products_page, cart_page, checkout_page, login_page, signup_page, page
    ):
        import time

        products_page.open()
        products_page.add_first_to_cart()
        cart_page.open()
        cart_page.expect_items_count(1)

        page.click("a:has-text('Proceed To Checkout')")
        page.click("u:has-text('Register / Login')")

        email = f"order_{int(time.time())}@example.com"
        login_page.start_signup("Order User", email)

        signup_page.fill_account_info("TestPass123")
        signup_page.fill_address_info(
            {
                "first_name": "Order",
                "last_name": "User",
                "company": "OrderCo",
                "address1": "789 Order St",
                "address2": "Suite 1",
                "state": "Texas",
                "city": "Austin",
                "zipcode": "73301",
                "mobile": "5551234567",
            }
        )
        signup_page.create_account()
        signup_page.expect_account_created()
        signup_page.continue_after_creation()

        page.click("a[href='/view_cart']")
        page.click("a:has-text('Proceed To Checkout')")
        checkout_page.place_order_with_comment("Please deliver fast")
        checkout_page.enter_payment_details(
            "Order User", "4111111111111111", "123", "12", "2028"
        )
        checkout_page.expect_order_success()

    @allure.story("TC6: Contact us form")
    def test_contact_us_form(self, contact_page):
        contact_page.open()
        contact_page.submit_form(
            "Test User",
            "contact_test@example.com",
            "Test Subject",
            "This is a test message for the contact form.",
        )
        contact_page.expect_success()
