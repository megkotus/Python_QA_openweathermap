from playwright.sync_api import expect

import re

# TC 01.02.01 See the forecast in C/F | The unit toggle button is working
def test_units_toggle_button(welcome_page):
    welcome_page.visit()
    welcome_page.switch_to_imperial_units()
    expect(welcome_page.units_toggle_css).to_have_css('left', '96px')
    welcome_page.switch_to_metric_units()
    expect(welcome_page.units_toggle_css).to_have_css('left', '2.66667px')


# TC 01.02.02 See the forecast in C/F | The units are converted to F and mph on button toggle throughout the page
def test_units_convertion(welcome_page):
    welcome_page.visit()
    welcome_page.switch_to_imperial_units()

    # Current weather
    expect(welcome_page.current_temperature).to_contain_text('°F')

    # Current weather items
    expect(welcome_page.current_weather_items).to_contain_text('mph')
    expect(welcome_page.current_weather_items).to_contain_text('°F')

    # 8-day forecast
    expect(welcome_page.eight_day_forecast).to_have_text(re.compile('°F'))

    # 8-day forecast dropdown
    welcome_page.open_dropdown_of_eight_day_forecast(1)
    expect(welcome_page.eight_day_forecast_dropdown_content).to_have_text(
        re.compile('mph')
    )
    expect(welcome_page.eight_day_forecast_dropdown_content).to_have_text(
        re.compile('°F')
    )
