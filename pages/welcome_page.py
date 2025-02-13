from playwright.sync_api import Page, expect

from datetime import datetime
import pytz

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

        self.eight_day_forecast_dropdown_button_open = self.page.locator(
            'ul.day-list li div.day-list-values span.chevron-container')
        self.eight_day_forecast_dropdown_button_close = self.page.locator(
            '.scrolling-container-header span.chevron-container')

        self.units_toggle_css = self.page.locator('div#selected')

        self.current_temperature = self.page.locator('div.current-temp span')
        self.current_weather_items = self.page.locator('ul.weather-items')

        self.eight_day_forecast = self.page.locator('ul.day-list')
        self.eight_day_forecast_item = self.page.locator('ul.day-list li')
        self.eight_day_forecast_day = self.page.locator('ul.day-list li span:first-child')
        self.eight_day_forecast_dropdown_header = self.page.locator('.scrolling-container-header ul li')
        self.eight_day_forecast_dropdown_header_selected_day = self.page.locator('.scrolling-container-header ul li.active')
        self.eight_day_forecast_dropdown_content = self.page.locator('.scrolling-container-content')
        self.eight_day_forecast_dropdown_top_section = self.page.locator('.top-section')

        self.different_weather = self.page.get_by_text("Different Weather?")
        self.different_weather_pop_up = self.page.get_by_role("heading", name="Different weather")
        self.different_weather_pop_up_items = self.different_weather_pop_up_items = self.page.locator('ul.icons li')
        self.different_weather_pop_up_send_button = self.page.get_by_text('Send')

        self.small_map = self.page.locator('div.map')
        self.small_map_center = self.page.locator('.leaflet-map-pane')

        self.date_and_time = self.page.locator('div.current-container.mobile-padding div span.orange-text')
        self.location = self.date_and_time.locator('+ h2')

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

    def open_dropdown_of_eight_day_forecast(self, count):
        self.eight_day_forecast_dropdown_button_open.nth(count).click()

    def close_eight_day_forecast_dropdown(self):
        self.eight_day_forecast_dropdown_button_close.click()

    def open_different_weather_pop_up(self):
        self.different_weather.click()

    def move_small_map(self):
        self.small_map.drag_to(
            self.small_map,
            source_position={"x": 5, "y": 5},
            target_position={"x": 15, "y": 15}
        )

    def choose_different_weather_first_option(self):
        self.different_weather_pop_up_items.first.click()

    def different_weather_click_send_button(self):
        self.different_weather_pop_up_send_button.click()

    def get_date_and_time_at_showed_location(self):
        city, _ = self.location.text_content().split(', ')
        timezone = [tz for tz in pytz.all_timezones if F'{city}' in tz][0]
        datetime_at_location = datetime.now(pytz.timezone(timezone)).strftime('%b %d, %I:%M%p').replace("PM",
                                                                                                        "pm").replace(
            "AM", "am")
        return datetime_at_location