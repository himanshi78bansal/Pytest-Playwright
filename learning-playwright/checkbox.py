from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")

    # using page.get_by_role (not working here)
    # checkbox = page.get_by_role("checkbox", name="Cricket")
    # checkbox.check()

    # using page.get_by_text
    # checkbox = page.get_by_text("Cricket")
    # checkbox.click()

    # using query_selector
    checkbox = page.query_selector("//input[@value='Cricket']")
    checkbox.check()

    if checkbox.is_checked():
        print("Checkbox is checked")
    else:
        print("Checkbox is not checked")

    page.wait_for_timeout(2000)