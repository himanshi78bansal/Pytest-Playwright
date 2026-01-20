from playwright.sync_api import Playwright, expect

from CreateOrderAPI import ApiUtils


def test_createOrder(playwright: Playwright):
    apiUtils = ApiUtils()
    orderId = apiUtils.createOrder(playwright)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    page.locator("#userEmail").fill("Shubhamlambha.1996@gmail.com")
    page.locator("#userPassword").fill("Shubh123")
    page.locator("#login").click()
    print("Logged in")

    page.get_by_role('button', name='ORDERS').click()

    row = page.locator('tr').filter(has_text=orderId)
    expect(row).to_be_visible()
    page.wait_for_timeout(2000)
