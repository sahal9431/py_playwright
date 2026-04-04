from playwright.sync_api import Page

def intercept_response(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4d4cob9f6fbO")


def test_network_mock_response(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("asifms@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Abcd@1234")
    page.get_by_role("button", name="Login").click()
    #go to my orders
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    print("sucessfully mocked the response")
