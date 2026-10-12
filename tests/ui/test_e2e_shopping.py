import allure
import pytest


@allure.feature("Shopping")
@allure.story("Add product to cart")
@pytest.mark.ui
@pytest.mark.e2e
def test_add_product_to_cart(products_page, cart_page):
    products_page.open()
    products_page.search_for("Blue Top")
    products_page.expect_results_count(1)
    products_page.add_first_to_cart()
    
    cart_page.open()
    cart_page.expect_items_count(1)