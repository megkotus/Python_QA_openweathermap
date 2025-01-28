from playwright.sync_api import expect

#TC 01.09.01 After clicking the "Different weather?" button the pop up window appears
def test_different_weather_pop_up(welcome_page):
    welcome_page.visit()
    welcome_page.open_different_weather_pop_up()
    expect(welcome_page.different_weather_pop_up).to_be_visible()
