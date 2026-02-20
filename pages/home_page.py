class HomePage:
    def __init__(self, page):
        self.page = page
    
    def add_a_product_to_cart(self):
        self.page.get_by_role("button", name="Add to Cart").first.click()

    def get_success_message(self):
        message = self.page.locator(".alert-success").text_content()
        return message
    
    def open_cart(self):
        """Opens the cart dropdown by clicking on the cart total element."""
        self.page.locator("#cart-total").click()
    
    def open_view_cart(self):
        """"Opens the cart page by clicking on the 'View Cart' link in the cart dropdown.
        """
        self.page.get_by_role("link", name="View Cart").click()

    