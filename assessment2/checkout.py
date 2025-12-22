import time

from playwright.sync_api import Page, expect

def test_checkoutPage(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("checkbox").click()
    page.get_by_role("button").click()

    phone1 = "iphone X"
    phone2 = "Samsung Note 8"

    iphone = page.locator("app-card").filter(has_text=phone1)
    iphone.get_by_role("button").click()
    samsung = page.locator("app-card").filter(has_text=phone2)
    samsung.get_by_role("button").click()
    page.get_by_text(" Checkout ( 2 )").click()

    expect(page.locator(".media-body")).to_have_count(2)
    expect(page.locator(".media-heading").nth(0)).to_have_text(phone1)
    expect(page.locator(".media-heading").nth(2)).to_have_text(phone2)

    page.get_by_text("Checkout").click()

    country = "India"
    page.locator("#country").type(country)
    page.wait_for_selector(".suggestions", state="visible")
    page.locator(".suggestions").click()
    page.locator("//label[@for='checkbox2']").click()
    page.locator("//input[@value='Purchase']").click()

    # expect(page.locator(".alert")).to_contain_text("Thank you! Your order will be delivered in next few weeks :-).")




