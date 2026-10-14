from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")
        return self

    def get_title(self) -> str:
        return self.page.title()

    def expect_url_contains(self, text: str):
        expect(self.page).to_have_url(lambda url: text in url)
