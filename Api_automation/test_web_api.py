from playwright.sync_api import Playwright
from playwright.sync_api import expect
from Api_automation.utils.apiBase import APIUtils

def test_e2e_web_api(playwright: Playwright):
    #launch the browser
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order - oderid
    api_utils = APIUtils()
    oder_id = api_utils.createoder(playwright)

    #login to the application
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("asifms@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Abcd@1234")
    page.get_by_role("button", name="Login").click()

    #go to my orders
    page.get_by_role("button", name="ORDERS").click()
    product_row = page.locator("tr").filter(has_text=oder_id)
    product_row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    browser.close()
