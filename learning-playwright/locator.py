from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")

    # CSS Selector -
        # 1. id - #
        # 2. class - .
        # 3. attribute - tagname[attribute="value"]

    # using id - #
    emailInputField = page.wait_for_selector("#username")
    emailInputField.type("student")
    # using attribute - tagname[attribute="value"]
    passInputField = page.wait_for_selector("input[type=password]")
    passInputField.type("Password123")
    # using class - .
    loginButton = page.wait_for_selector(".btn")
    loginButton.click()
    #using xpath
    logoutButton = page.wait_for_selector("//a[normalize-space()='Log out']")
    logoutButton.click()

    page.wait_for_timeout(3000)