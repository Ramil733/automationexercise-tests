import allure
import pytest
from api.ProductsApi import ProductsApi

    
@allure.feature("API: Products")
@pytest.mark.api
class TestProductsApi:

    @allure.story("Get all products")
    def test_get_all_products(self):
        api = ProductsApi()
        response = api.get_all_products()
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 200
        assert len(data["products"]) > 0

    @allure.story("Search product")
    def test_search_product(self):
        api = ProductsApi()
        response = api.search_product("Blue Top")
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 200
        assert len(data["products"]) > 0