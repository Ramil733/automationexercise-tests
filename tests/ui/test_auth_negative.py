import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Authentication")
@pytest.mark.ui
class TestAuthNegative:

    @allure.story("TC5: Register user with existing email")
    def test_register_with_existing_email(self, login_page, registered_user):
        login_page.open()
        login_page.start_signup("Test User", registered_user["email"])

        expect(
            login_page.page.locator("p:has-text('Email Address already exist!')")
        ).to_be_visible()