import allure
import pytest
from api.ProductsApi import ProductsApi


@allure.feature("API: Products")
@pytest.mark.api
class TestProductsApi:

    @allure.story("API 1: GET all products")
    def test_get_all_products(self):
        response = ProductsApi().get_all_products()
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 200
        assert len(data["products"]) > 0

    @allure.story("API 2: POST productsList not supported")
    def test_post_products_method_not_allowed(self):
        response = ProductsApi().post_products()
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 405
        assert data["message"] == "This request method is not supported."

    @allure.story("API 5: POST search product")
    def test_search_product(self):
        response = ProductsApi().search_product("Blue Top")
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 200
        assert len(data["products"]) > 0

    @allure.story("API 6: POST search product without parameter")
    def test_search_product_without_param(self):
        response = ProductsApi().search_product_without_param()
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 400
        assert "search_product parameter is missing" in data["message"]