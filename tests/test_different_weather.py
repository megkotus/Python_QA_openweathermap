from playwright.sync_api import expect

#TC 01.09.01 After clicking the "Different weather?" button the pop up window appears
def test_different_weather_pop_up(welcome_page):
    welcome_page.visit()
    welcome_page.open_different_weather_pop_up()
    expect(welcome_page.different_weather_pop_up).to_be_visible()

def test_different_weather_send_button_is_clickable(welcome_page):
    welcome_page.visit()
    welcome_page.open_different_weather_pop_up()
    welcome_page.choose_different_weather_first_option()
    welcome_page.different_weather_click_send_button()