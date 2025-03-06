from playwright.sync_api import expect

# TC 01.07.01 Check date and time | Compare displayed time with the current time at the displayed location
def test_date_and_time(welcome_page):
    welcome_page.visit()
    expect(welcome_page.date_and_time).to_have_text(
        welcome_page.get_date_and_time_at_showed_location()
    )
