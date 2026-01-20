from playwright.sync_api import Page, expect


def test_mouseNinja(page: Page):
    page.goto("https://demoqa.com/buttons", wait_until="domcontentloaded")

    double_click_btn = page.get_by_text("Double Click Me")
    right_click_btn = page.get_by_text("Right Click Me")
    dynamic_click_btn = page.get_by_text("Click Me", exact=True)


    double_click_btn.dblclick()
    expect(page.get_by_text("You have done a double click")).to_be_visible()

    right_click_btn.click(button="right")
    expect(page.get_by_text("You have done a right click")).to_be_visible()

    dynamic_click_btn.click()
    expect(page.get_by_text("You have done a dynamic click")).to_be_visible()
