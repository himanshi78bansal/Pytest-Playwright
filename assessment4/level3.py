from playwright.sync_api import Page, expect

def test_keyboardWizard(page: Page):
    page.goto("https://www.selenium.dev/selenium/web/web-form.html")

    page.get_by_label("Text input").click()
    page.keyboard.type("johndoe@gmail.com")
    expect(page.locator("#my-text-id")).to_have_value("johndoe@gmail.com")

    page.keyboard.press("Tab")
    page.keyboard.type("Password")

    page.keyboard.press("Tab")
    page.keyboard.type("Hello World!!!")

    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")

    for i in range(8):
        page.keyboard.press("Tab")

    page.keyboard.press("Enter")

    expect(page.get_by_text("Received!")).to_be_visible()





