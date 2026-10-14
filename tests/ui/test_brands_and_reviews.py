import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Products")
@pytest.mark.ui
class TestBrandsAndReviews:

    @allure.story("TC19: View brand products")
    def test_view_brand_products(self, products_page):
        products_page.open()
        products_page.open_brand("Polo")
        expect(products_page.page.locator(".title.text-center")).to_contain_text("Polo")

    @allure.story("TC21: Add review on product")
    def test_add_review(self, products_page, page):
        products_page.open()
        page.locator("a:has-text('View Product')").first.click()
        products_page.submit_review("Reviewer", "review@example.com", "Great product!")
        products_page.expect_review_success()