class CartPage:
    def __init__(self, page):
        self.page = page
    
    def remove_product_from_cart(self):
        """Removes a product from the cart by clicking on the remove button."""
        self.page.locator(".fa-times-circle").click()
    
    def verify_cart_is_empty(self):
        """Verifies that the cart is empty by checking for the presence of the empty cart message."""
        locator = self.page.locator("//p[text()='Your shopping cart is empty!']")
        # If multiple matches exist, return the first one's text
        try:
            return locator.first.text_content()
        except Exception:
            return locator.text_content()