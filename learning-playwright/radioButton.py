from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")

    # using page.get_by_role
    radioButton = page.get_by_role("radio", name="FeMale")
    radioButton.check()

    # using query_selector
    # radioButton = page.query_selector("//input[@value='FeMale']")
    # radioButton.check()

    if radioButton.is_checked():
        print("Radio Button is checked")
    else:
        print("Radio Button is not checked")


    page.wait_for_timeout(2000)