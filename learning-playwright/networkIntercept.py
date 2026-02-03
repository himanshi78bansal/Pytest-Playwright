from playwright.sync_api import Playwright, expect
from CreateOrderAPI import ApiUtils

def test_networklIntercept(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    apiUtils = ApiUtils()
    token = apiUtils.getToken(playwright)

    page.add_init_script(f"""localStorage.setItem('token', '{token}')""")

    page.goto("https://rahulshettyacademy.com/client")
    page.wait_for_timeout(3000)
    page.get_by_role('button', name='ORDERS').click()
    expect(page.get_by_text("Your Orders")).to_be_visible()