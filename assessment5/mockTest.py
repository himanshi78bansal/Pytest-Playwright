from playwright.sync_api import Playwright, expect

from CreateOrderAPI import ApiUtils

fakeOrderResponse = {"data":[],"message":"No Orders"}

def response_intercept(route):
    route.fulfill(json= fakeOrderResponse)

def test_createOrder(playwright: Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", response_intercept)

    page.locator("#userEmail").fill("Shubhamlambha.1996@gmail.com")
    page.locator("#userPassword").fill("Shubh123")
    page.locator("#login").click()
    print("Logged in")

    page.get_by_role('button', name='ORDERS').click()

    page.get_by_role('button', name='HELP').click()


    expect(page.locator("//div[@class='mt-4 ng-star-inserted']")).to_have_text("You have No Orders to show at this time. Please Visit Back Us")
