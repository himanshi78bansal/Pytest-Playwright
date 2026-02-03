from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practice.expandtesting.com/dynamic-table")

    # using column and row
    # headers = page.locator("th")
    # CPUCol = None
    # for i in range(headers.count()):
    #     if page.locator("th").nth(i).inner_text() == "CPU":
    #         CPUCol = i
    #         break
    # row = page.locator("tr", has_text = "Chrome")
    # val = row.locator("td").nth(CPUCol).inner_text()

    # playwright methods
    headers = page.locator("th").all_inner_texts()
    CPUCol = headers.index("CPU")
    row = page.locator("tr").filter(has_text = "Chrome")
    val = row.locator("td").nth(CPUCol).inner_text()

    # dynamic xpath
    # val = page.locator("//table//tr[td[contains(text(),'Chrome')]]/td[count(//th[contains(text(),'CPU')]/preceding-sibling::th)+1]").inner_text()

    page.wait_for_timeout(2000)

    print(val)

