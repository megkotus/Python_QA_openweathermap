
#TC 01.03.01 Check geolocation | Compare displayed location name with the browser detected location
def test_get_location(welcome_page):
    welcome_page.set_location()
    welcome_page.visit()

    assert welcome_page.location.text_content() == 'San Francisco, US'


