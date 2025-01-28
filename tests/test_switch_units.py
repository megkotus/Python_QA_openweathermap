from playwright.sync_api import expect

#TC 01.02.01 See the forecast in C/F | The unit toggle button is working
def test_units_toggle_button(welcome_page):
    welcome_page.visit()
    welcome_page.switch_to_imperial_units()
    expect(welcome_page.units_toggle_css).to_have_css('left', '96px')
    welcome_page.switch_to_metric_units()
    expect(welcome_page.units_toggle_css).to_have_css('left', '2.66667px')

