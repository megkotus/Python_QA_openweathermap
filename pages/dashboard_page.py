from playwright.sync_api import Page

from data.urls import Urls

urls = Urls()


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
