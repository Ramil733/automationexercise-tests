import pytest
from pages.HomePage import HomePage
from pages.ProductPage import ProductPage
from pages.CartPage import CartPage
from pages.LoginPage import LoginPage
from pages.SignupPage import SignupPage


@pytest.fixture
def home_page(page):
    return HomePage(page)


@pytest.fixture
def products_page(page):
    return ProductPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def signup_page(page):
    return SignupPage(page)