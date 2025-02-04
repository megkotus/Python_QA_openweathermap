from playwright.sync_api import expect

from data.data_generator import DataGenerator

#TC 01.01.01 The "Search city" field is available
def test_search_city_field_is_available(welcome_page):
    welcome_page.visit()
    expect(welcome_page.search_city_input).to_be_visible()
    expect(welcome_page.search_city_input).to_be_enabled()

#TC 01.01.02 The right location is displayed after searching via the form
def test_right_location_is_displayed_after_searching(welcome_page):
    gen_location = DataGenerator()
    welcome_page.visit()
    welcome_page.fill_search_city_input(gen_location.valid_country)
    print(gen_location.valid_country)
    welcome_page.click_search_city_button()
    welcome_page.dropdown_search_list.first.click()
    expect(welcome_page.location_header).to_contain_text(gen_location.valid_country)
