import time
import pytest
from api.UserApi import UserApi


@pytest.fixture
def registered_user():
    api = UserApi()
    email = f"aqa_test_{int(time.time() * 1000)}@example.com"
    password = "TestPass123"

    user_data = {
        "name": "Test User",
        "email": email,
        "password": password,
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
        "mobile_number": "1234567890",
    }

    response = api.create_account(user_data)
    assert response.json()["responseCode"] == 201, "Failed to create user for test"

    yield {"email": email, "password": password, "name": "Test User", "data": user_data}

    api.delete_account(email, password)