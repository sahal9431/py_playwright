from playwright.sync_api import Playwright

class APIUtils:
    def __init__(self):
        self.orders = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}
        self.url = "https://rahulshettyacademy.com"

    def get_token(self, playwright:Playwright):
        api_request = playwright.request.new_context(base_url=self.url)
        response = api_request.post("/api/ecom/auth/login", data = {"userEmail": "asifms@gmail.com", "userPassword": "Abcd@1234"})
        assert response.ok
        print(response.json())
        token = response.json()["token"]
        return token

    def createoder(self, playwright:Playwright):
        token = self.get_token(playwright)
        api_reuest = playwright.request.new_context(base_url=self.url)
        response = api_reuest.post("/api/ecom/order/create-order", data = self.orders, 
                                   headers= {"Authorization": token, "content-type": "application/json"})
        response_body = response.json()
        print(response_body)
        order_id = response_body["orders"][0]
        return order_id
