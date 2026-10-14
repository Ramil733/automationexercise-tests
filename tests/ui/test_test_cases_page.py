import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Misc")
@pytest.mark.ui
class TestMiscPages:
    @allure.story("TC7: Verify test cases page")
    def test_open_test_cases_page(self, page):
        page.goto("https://automationexercise.com/test_cases")
        expect(page.locator("h2.title.text-center b")).to_contain_text("Test Cases")
