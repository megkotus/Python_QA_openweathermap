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

        self.imperial_units_button = self.page.get_by_text('Imperial')
        self.metric_units_button = self.page.get_by_text('Metric')

        self.eight_day_forecast_dropdown_button = self.page.locator(
            'ul.day-list li:first-child div.day-list-values span.chevron-container')

        self.units_toggle_css = self.page.locator('div#selected')

        self.current_temperature = self.page.locator('div.current-temp span')
        self.current_weather_items = self.page.locator('ul.weather-items')
        self.eight_day_forecast = self.page.locator('ul.day-list')
        self.eight_day_forecast_dropdown = self.page.locator('.scrolling-container-content')


    def visit(self):
        self.page.goto(urls.base_url)
        expect(self.page).to_have_url(urls.base_url)

    def fill_search_city_input(self, location):
        self.search_city_input.fill(location)

    def click_search_city_button(self):
        self.search_city_button.click()

    def switch_to_imperial_units(self):
        self.imperial_units_button.click()

    def switch_to_metric_units(self):
        self.metric_units_button.click()

    def open_first_day_dropdown_of_eight_day_forecast(self):
        self.eight_day_forecast_dropdown_button.click()