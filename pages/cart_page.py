class CartPage:
    def __init__(self, page):
        self.page = page
    
    def remove_product_from_cart(self):
        """Removes a product from the cart by clicking on the remove button."""
        self.page.locator(".fa-times-circle").click()
    
    def verify_cart_is_empty(self):
        """Verifies that the cart is empty by checking for the presence of the empty cart message."""
        empty_cart_message = self.page.locator("//p[text()='Your shopping cart is empty!']").text_content()
        return empty_cart_message