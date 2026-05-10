class HomePage:
    def __init__(self, page):
        self.page = page
    
    def add_a_product_to_cart(self):
        # ensure we're on the storefront before trying to add a product
        try:
            self.page.goto("https://awesomeqa.com/ui/")
        except Exception:
            pass
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
    
    def search_for_product(self, product_name):
        """Search for a product by name"""
        try:
            self.page.goto("https://awesomeqa.com/ui/")
        except Exception:
            pass
        search_box = self.page.locator("input[name='search']")
        search_box.fill(product_name)
        search_box.press("Enter")
        # Wait for search results to load
        self.page.wait_for_load_state("networkidle")

    