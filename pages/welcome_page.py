from playwright.sync_api import Page, expect

from data.urls import Urls

urls = Urls()
class WelcomePage():
    def __init__(self, page: Page):
        self.page = page
        self.search_city_input = self.page.get_by_role('textbox', name='Search city')

    def visit(self):
        self.page.goto(urls.base_url)
        expect(self.page).to_have_url(urls.base_url)