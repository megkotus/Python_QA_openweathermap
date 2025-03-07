from playwright.sync_api import expect

# TC 01.03.01 Check geolocation | Compare displayed location name with the browser detected location
def test_get_location(welcome_page):
    location = 'San Francisco, US'
    coordinates = {'latitude': 37.7749, 'longitude': -122.4194}
    param, val = ['transform', 'matrix(128, 0, 0, 128, 10482.2, 25331)']

    welcome_page.set_location(coordinates)
    welcome_page.visit()

    assert welcome_page.location.text_content() == location
    expect(welcome_page.small_map_location).to_have_css(param, val)
