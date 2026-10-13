import time
import allure
import pytest
from api.UserApi import UserApi


@allure.feature("API: User")
@pytest.mark.api
class TestUserApi:

    @allure.story("API 7: Verify login valid")
    def test_verify_login_success(self, registered_user):
        response = UserApi().verify_login(registered_user["email"], registered_user["password"])
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 200
        assert data["message"] == "User exists!"

    @allure.story("API 8: Verify login without email")
    def test_verify_login_missing_email(self):
        response = UserApi().post("/verifyLogin", data={"password": "password123"})
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 400
        assert "email or password parameter is missing" in data["message"]

    @allure.story("API 9: DELETE verifyLogin not supported")
    def test_verify_login_delete_not_supported(self):
        response = UserApi().delete("/verifyLogin")
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 405
        assert data["message"] == "This request method is not supported."

    @allure.story("API 10: Verify login invalid")
    def test_verify_login_invalid(self):
        email = f"nonexistent_{int(time.time() * 1000)}@test.com"
        response = UserApi().verify_login(email, "wrongpass")
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 404
        assert data["message"] == "User not found!"

    @allure.story("API 11: Create account")
    def test_create_account(self):
        email = f"create_{int(time.time() * 1000)}@example.com"
        user_data = {
            "name": "Create Test",
            "email": email,
            "password": "TestPass123",
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "6",
            "birth_year": "1995",
            "firstname": "Create",
            "lastname": "Test",
            "company": "TestCo",
            "address1": "123 Test St",
            "address2": "Apt 4",
            "country": "United States",
            "zipcode": "12345",
            "state": "California",
            "city": "Los Angeles",
            "mobile_number": "1234567890",
        }
        api = UserApi()
        response = api.create_account(user_data)
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 201
        assert data["message"] == "User created!"
        api.delete_account(email, "TestPass123")

    @allure.story("API 12: Delete account")
    def test_delete_account(self):
        api = UserApi()
        email = f"delete_{int(time.time() * 1000)}@example.com"
        user_data = {
            "name": "Delete Test",
            "email": email,
            "password": "TestPass123",
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "6",
            "birth_year": "1995",
            "firstname": "Delete",
            "lastname": "Test",
            "company": "TestCo",
            "address1": "123 Test St",
            "address2": "Apt 4",
            "country": "United States",
            "zipcode": "12345",
            "state": "California",
            "city": "Los Angeles",
            "mobile_number": "1234567890",
        }
        api.create_account(user_data)

        response = api.delete_account(email, "TestPass123")
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 200
        assert data["message"] == "Account deleted!"

    @allure.story("API 13: Update account")
    def test_update_account(self, registered_user):
        api = UserApi()
        updated = dict(registered_user["data"])
        updated["firstname"] = "UpdatedName"
        updated["city"] = "San Francisco"

        response = api.update_account(updated)
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 200
        assert data["message"] == "User updated!"

    @allure.story("API 14: Get user detail by email")
    def test_get_user_detail_by_email(self, registered_user):
        response = UserApi().get_user_detail(registered_user["email"])
        assert response.status_code == 200
        data = response.json()
        assert data["responseCode"] == 200
        user = data["user"]
        assert user["email"] == registered_user["email"]
        assert user["name"] == registered_user["name"]