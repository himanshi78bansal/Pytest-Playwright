from behave import *
from playwright.sync_api import sync_playwright
from pages.loginPage import LoginPage

@given('user launches the application')
def step_impl(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.page.goto("https://practicetestautomation.com/practice-test-login/")
    context.login = LoginPage(context.page)


@when('user logs in with "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login.login(username, password)


@then('dashboard should be displayed')
def step_impl(context):
    assert context.page.title() == "Logged In Successfully | Practice Test Automation"
    context.browser.close()
