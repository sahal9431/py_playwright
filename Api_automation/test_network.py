from playwright.sync_api import Page

fakePayloadResponse = {"data":[],"message":"No Orders"}
def intercept_response(route):
    route.fulfill(json = fakePayloadResponse)


def test_network(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("asifms@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Abcd@1234")
    page.get_by_role("button", name="Login").click()
    #go to my orders
    page.get_by_role("button", name="ORDERS").click()
    page.locator(".mt-4").text_content() == " You have No Orders to show at this time."
    print("successfully mocked the response")
