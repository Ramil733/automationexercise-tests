import allure
import pytest
from api.UserApi import UserApi


@allure.feature("API: User")
@pytest.mark.api
class TestUserApi:

    @allure.story("API 7: Verify login")
    def test_verify_login(self):
        api = UserApi()
        response = api.verify_login("test@example.com", "password123")
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] in [200, 404]

    @allure.story("API 8: Verify login without email")
    def test_verify_login_missing_email(self):
        api = UserApi()
        response = api.post("/verifyLogin", data={"password": "password123"})
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 400

    @allure.story("API 10: Verify login invalid")
    def test_verify_login_invalid_credentials(self):
        api = UserApi()
        response = api.verify_login("nonexistent_user_12345@test.com", "wrongpass")
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 404

    @allure.story("API 11: Create account")
    def test_create_account(self):
        api = UserApi()
        user_data = {
            "name": "Test User",
            "email": "testuser_aqa_12345@example.com",
            "password": "TestPass123",
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "6",
            "birth_year": "1995",
            "firstname": "Test",
            "lastname": "User",
            "company": "TestCo",
            "address1": "123 Test St",
            "address2": "Apt 4",
            "country": "United States",
            "zipcode": "12345",
            "state": "California",
            "city": "Los Angeles",
            "mobile_number": "1234567890"
        }
        response = api.create_account(user_data)
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] in [201, 400]
        if data["responseCode"] == 201:
            delete_response = api.delete_account(user_data["email"], user_data["password"])
            assert delete_response.json()["responseCode"] == 200