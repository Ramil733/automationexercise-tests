import allure
import pytest
from api.BrandsApi import BrandsApi


@allure.feature("API: Brands")
@pytest.mark.api
class TestBrandsApi:

    @allure.story("API 3: GET all brands")
    def test_get_all_brands(self):
        response = BrandsApi().get_all_brands()
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 200
        assert len(data["brands"]) > 0
        first_brand = data["brands"][0]
        assert "id" in first_brand
        assert "brand" in first_brand

    @allure.story("API 4: PUT brandsList not supported")
    def test_put_brands_method_not_allowed(self):
        response = BrandsApi().put_brands()
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 405
        assert data["message"] == "This request method is not supported."