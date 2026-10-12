import pytest
from pages.HomePage import HomePage
from pages.ProductPage import ProductPage
from pages.CartPage import CartPage


@pytest.fixture
def home_page(page):
    return HomePage(page)


@pytest.fixture
def products_page(page):
    return ProductPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)