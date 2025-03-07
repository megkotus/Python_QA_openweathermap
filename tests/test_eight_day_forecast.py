from playwright.sync_api import expect

# TC 01.06.01 A detailed day forecast (any day of 8) | Forecast for the selected day is displayed
def test_each_day_of_eight_day_forecast(welcome_page):
    welcome_page.visit()
    for i in range(welcome_page.eight_day_forecast_item.count()):
        day, temp, conditions, _ = (
            welcome_page.eight_day_forecast_item.nth(i)
            .locator('span')
            .all_inner_texts()
        )
        temp1, temp2 = temp.strip('°C').split('/')
        welcome_page.open_dropdown_of_eight_day_forecast(i)

        # Checks header
        expect(
            welcome_page.eight_day_forecast_dropdown_header_selected_day
        ).to_have_text(day)

        # Checks overcast and temperatures in top section
        expect(
            welcome_page.eight_day_forecast_dropdown_top_section
        ).to_contain_text(conditions.capitalize())
        expect(
            welcome_page.eight_day_forecast_dropdown_top_section
        ).to_contain_text(temp1)
        expect(
            welcome_page.eight_day_forecast_dropdown_top_section
        ).to_contain_text(temp2)
        welcome_page.close_eight_day_forecast_dropdown()
