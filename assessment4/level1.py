from playwright.sync_api import Page, expect


def test_dialogTrainer(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    # JS Alert
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Click for JS Alert").click()
    expect(page.get_by_text("You successfully clicked an alert")).to_be_visible()

    # JS Confirm
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_text("Click for JS Confirm").click()
    expect(page.get_by_text("You clicked: Cancel")).to_be_visible()

    # JS Prompt
    def handle_prompt(dialog):
        dialog.accept("Playwright Hero")

    page.once("dialog", handle_prompt)
    page.get_by_text("Click for JS Prompt").click()
    expect(page.get_by_text("You entered: Playwright Hero")).to_be_visible()
