import time

from playwright.sync_api import Page, expect


def test_multipleWindows(playwright):
    browser = playwright.chromium.launch(headless=False)
    context1 = browser.new_context()
    page = context1.new_page()
    page.goto("https://www.hdfc.bank.in/")
    expect(page).to_have_title("Personal Banking & Netbanking Services | HDFC Bank")
    expect(page).to_have_url("https://www.hdfc.bank.in/")

    with page.expect_popup() as personalLoan:
        page.locator("//a[text()='Personal Loan']").click()
        personalLoanPageData = personalLoan.value

    personalLoanPageData.bring_to_front()
    expect(personalLoanPageData).to_have_title("Get Instant Personal Loan Online Starting 9.99% | HDFC Bank")
    expect(personalLoanPageData).to_have_url("https://www.hdfc.bank.in/personal-loan?icid=website_organic_footer_coreproducts:link:personalloan")


    with page.expect_popup() as carLoan:
        page.locator("//a[text()='Car Loan']").click()
        carLoanPageData = carLoan.value

    carLoanPageData.bring_to_front()
    expect(carLoanPageData).to_have_title("Car Loan Online - Apply New Car Loan & Get up to 100% Funding | HDFC Bank")
    expect(carLoanPageData).to_have_url("https://www.hdfc.bank.in/car-loan?icid=website_organic_footer_coreproducts:link:carloan")

    with page.expect_popup() as businessLoan:
        page.locator("//a[text()='Business Loan']").click()
        businessLoanPageData = businessLoan.value

    businessLoanPageData.bring_to_front()
    expect(businessLoanPageData).to_have_title("Apply for Business Loan Online at Lowest Interest Rate | HDFC Bank")
    expect(businessLoanPageData).to_have_url("https://www.hdfc.bank.in/business-loan?icid=website_organic_footer_coreproducts:link:businessloan")

    with page.expect_popup() as goldLoan:
        page.locator("//a[text()='Gold Loan']").click()
        goldLoanPageData = goldLoan.value

    goldLoanPageData.bring_to_front()
    expect(goldLoanPageData).to_have_title("Gold Loan - Apply Loan Against Gold Online in India | HDFC Bank")
    expect(goldLoanPageData).to_have_url("https://www.hdfc.bank.in/gold-loan?icid=website_organic_footer_coreproducts:link:goldloan")

    # to get all pages of a context(window)
    allpages = context1.pages

    # print title of all pages
    for p in allpages:
        print(p.title())

    # to open a new browser window
    context2 = browser.new_context()
    newPage = context2.new_page()
    newPage.goto("https://www.google.com/")
    time.sleep(2)
    newPage.close()


    # close the first context(browser window)
    page.close()
