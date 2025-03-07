from playwright.sync_api import expect


# TC 01.05.01 Use the small map | The map is movable with the mouse
def test_map_is_movable(welcome_page):
    welcome_page.visit()

    welcome_page.move_small_map()

    expect(welcome_page.small_map_center).not_to_have_css(
        'transform', 'matrix(1, 0, 0, 1, 0, 0)'
    )
