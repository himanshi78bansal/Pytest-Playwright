from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/FileUpload.html")

    # file path
    filePath = "./file.txt"
    # upload file
    page.locator("#input-4").set_input_files(filePath)

    # page.wait_for_timeout(5000)