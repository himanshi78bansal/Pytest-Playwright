from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")

    # page.select_option("locator", label="value")
    page.select_option("#Skills", label="AutoCAD")

    # or use page.locator(-----).select_option
    # page.locator("#Skills").select_option(label="AutoCAD")

    # or use page.get_by_role("combobox") (if role=combobox instead of select)
    # page.get_by_role("combobox", name="Skills").click()
    # page.get_by_text("AutoCAD").click()

    page.wait_for_timeout(2000)

