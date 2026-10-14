import allure
import pytest


@allure.feature("Subscription")
@pytest.mark.ui
class TestSubscription:

    @allure.story("TC10: Verify subscription in home page")
    def test_subscription_home(self, home_page):
        home_page.open()
        home_page.subscribe("subscriber@example.com")
        home_page.expect_subscription_success()

    @allure.story("TC11: Verify subscription in cart page")
    def test_subscription_cart(self, cart_page):
        cart_page.open()
        cart_page.subscribe("subscriber@example.com")
        cart_page.expect_subscription_success()