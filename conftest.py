import pytest
from playwright.sync_api import Page
from pages.welcome_page import WelcomePage


@pytest.fixture
def welcome_page(page: Page):
    return WelcomePage(page)
