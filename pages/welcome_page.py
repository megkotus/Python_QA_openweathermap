from playwright.sync_api import Page, expect

from data.urls import Urls

urls = Urls()
class WelcomePage():
    def __init__(self, page: Page):
        self.page = page
        self.search_city_input = self.page.get_by_role('textbox', name='Search city')
        self.search_city_button = self.page.get_by_role('button', name='Search')
        self.dropdown_search_list = self.page.locator('ul.search-dropdown-menu li')
        self.location_header = self.page.locator('.current-container h2')

    def visit(self):
        self.page.goto(urls.base_url)
        expect(self.page).to_have_url(urls.base_url)

    def fill_search_city_input(self, location):
        self.search_city_input.fill(location)

    def click_search_city_button(self):
        self.search_city_button.click()
