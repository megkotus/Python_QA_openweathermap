import pytest
from playwright.sync_api import Page

from pages.dashboard_page import DashboardPage
from pages.welcome_page import WelcomePage

@pytest.fixture
def welcome_page(page:Page):
    return WelcomePage(page)

@pytest.fixture
def dashboard_page(page:Page):
    return DashboardPage(page)