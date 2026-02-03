from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")

    name = "Himanshi Bansal"

    def handle_alert(dialog):
        print("Dialog type:", dialog.type)
        print("Alert text:", dialog.message)

        if dialog.type == "alert":
            dialog.accept()
        elif dialog.type == "confirm":
            dialog.dismiss()
        elif dialog.type == "prompt":
            dialog.accept(name)


    page.on("dialog", handle_alert)

    # simple alert message
    page.locator("//a[@href = '#OKTab']").click()
    page.locator("//div[@id='OKTab']/button").click()

    # confirmation alert
    page.locator("//a[@href = '#CancelTab']").click()
    page.locator("//div[@id='CancelTab']/button").click()
    expect(page.locator("#demo")).to_have_text("You Pressed Cancel")

    # prompt alert
    page.locator("//a[@href = '#Textbox']").click()
    page.locator("//div[@id='Textbox']/button").click()
    expect(page.locator("#demo1")).to_have_text(f"Hello {name} How are you today")

    browser.close()

