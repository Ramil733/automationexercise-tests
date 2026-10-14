import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Cart")
@pytest.mark.ui
class TestCart:

    @allure.story("TC12: Add products in cart")
    def test_add_products_in_cart(self, products_page, cart_page):
        products_page.open()

        first_product = products_page.page.locator(".productinfo").first
        first_product.hover()
        first_product.locator(".add-to-cart").click()
        products_page.page.click("button:has-text('Continue Shopping')")

        second_product = products_page.page.locator(".productinfo").nth(1)
        second_product.hover()
        second_product.locator(".add-to-cart").click()
        products_page.page.click("u:has-text('View Cart')")

        cart_page.expect_items_count(2)

    @allure.story("TC17: Remove products from cart")
    def test_remove_product_from_cart(self, products_page, cart_page, page):
        products_page.open()
        products_page.add_first_to_cart()

        cart_page.open()
        cart_page.expect_items_count(1)

        page.click(".cart_quantity_delete")
        cart_page.expect_empty()