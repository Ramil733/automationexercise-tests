import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Products")
@pytest.mark.ui
class TestProducts:

    @allure.story("TC8: Verify all products and product detail page")
    def test_verify_all_products_and_detail(self, products_page, page):
        products_page.open()

        first_product = page.locator(".productinfo").first
        first_product.hover()
        page.locator("a:has-text('View Product')").first.click()

        expect(page.locator(".product-information h2")).to_be_visible()
        expect(page.locator(".product-information p:has-text('Category')")).to_be_visible()
        expect(page.locator(".product-information span:has-text('Rs.')").first).to_be_visible()

    @allure.story("TC9: Search product")
    def test_search_product(self, products_page):
        products_page.open()
        products_page.search_for("Dress")
        expect(products_page.page.locator(".productinfo")).not_to_have_count(0)

    @allure.story("TC18: View category products")
    def test_view_category_products(self, home_page, page):
        home_page.open()
        home_page.expect_loaded()

        page.click("a[href='#Women']")
        page.click("a:has-text('Dress')")

        expect(page.locator(".title.text-center")).to_contain_text("Women - Dress Products")