from playwright.sync_api import Page, expect

# Task 3
def test_example_domain_page(page: Page):
    # Step 1 & 2: Open browser and navigate
    page.goto("https://example.com/")

    # Step 3: Verify title
    expect(page).to_have_title("Example Domain")

    # Step 4: Verify text presence
    expect(page.locator("h1")).to_have_text("Example Domain")

    # Task 4: Text Verification
    (expect(page.locator("//p[text()='This domain is for use in documentation examples without needing permission. Avoid use in operations.']")).
     to_contain_text("This domain is for use in documentation examples without needing permission. Avoid use in operations."))

    # Task 5: Negative Scenario (Incorrect Title)
    expect(page).not_to_have_title("Wrong Title")
