from playwright.sync_api import Page, expect

def test_frameBreaker(page: Page):
    page.goto("https://the-internet.herokuapp.com/iframe")

    frame = page.frame_locator("#mce_0_ifr")

    editor = frame.locator("body")

    editor.click()
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")

    page.keyboard.type("I rule the frames")

    expect(editor).to_have_text("I rule the frames")

