from playwright.sync_api import expect

#TC 01.01.01 The "Search city" field is available
def test_search_city_field_is_available(welcome_page):
    welcome_page.visit()
    expect(welcome_page.search_city_input).to_be_visible()
    expect(welcome_page.search_city_input).to_be_enabled()