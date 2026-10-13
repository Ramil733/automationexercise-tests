import allure
import pytest
import time

@allure.feature("Authentication")
@pytest.mark.ui
class TestAuthentication:

    @allure.story("TC3: Login with invalid credentials")
    def test_login_invalid(self, login_page):
        login_page.open()
        unique_email = f"wrong_{int(time.time() * 1000)}@example.com"
        login_page.login(unique_email, "wrongpass")
        login_page.expect_login_error()

    @allure.story("TC2: Login with valid credentials")
    def test_login_valid(self, login_page, registered_user):
        login_page.open()
        login_page.login(registered_user["email"], registered_user["password"])
        login_page.expect_logged_in(registered_user["name"])

    @allure.story("TC1: Register new user via UI")
    def test_register_user(self, login_page, signup_page):
        email = f"ui_signup_{int(__import__('time').time())}@example.com"

        login_page.open()
        login_page.start_signup("UI Test User", email)
        signup_page.fill_account_info("TestPass123")
        signup_page.fill_address_info({
            "first_name": "UI",
            "last_name": "Tester",
            "company": "UICo",
            "address1": "456 UI St",
            "address2": "Apt 8",
            "state": "New York",
            "city": "New York",
            "zipcode": "10001",
            "mobile": "9876543210",
        })
        signup_page.create_account()
        signup_page.expect_account_created()
        signup_page.continue_after_creation()
        login_page.expect_logged_in("UI Test User")