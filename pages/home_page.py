from pages.base_page import BasePage


class HomePage(BasePage):
    
    def add_a_product_to_cart(self):
        """Add first available product to cart"""
        try:
            self.navigate_to("https://awesomeqa.com/ui/")
        except Exception:
            pass
        self.click_nth_element("button:has-text('Add to Cart')", 0)

    def get_success_message(self):
        """Get success message after adding to cart"""
        return self.get_text(".alert-success")
    
    def open_cart(self):
        """Open the cart dropdown by clicking on the cart total element"""
        self.click("#cart-total")
    
    def open_view_cart(self):
        """Open the cart page by clicking on the 'View Cart' link in the cart dropdown"""
        self.click_by_role("link", "View Cart")
    
    def search_for_product(self, product_name):
        """Search for a product by name"""
        try:
            self.navigate_to("https://awesomeqa.com/ui/")
        except Exception:
            pass
        self.send_data("input[name='search']", product_name)
        self.send_keys("input[name='search']", "Enter")
        self.wait_for_page_load("networkidle")

    