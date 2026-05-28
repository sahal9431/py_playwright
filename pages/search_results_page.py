from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    
    def get_search_results(self):
        """Get all product titles from search results"""
        return self.get_all_text_contents("h4 a")
    
    def select_first_product(self):
        """Click on the first product in search results"""
        self.click_nth_element("h4 a", 0)
        self.wait_for_page_load("networkidle")
    
    def is_product_details_displayed(self):
        """Verify if product details page is displayed"""
        product_title = self.is_visible("h1, .heading-title", timeout=5000)
        price_element = self.is_visible("[id*='price'], [class*='price']", timeout=5000)
        add_to_cart = self.is_visible("button:has-text('Add to Cart')", timeout=5000)
        return product_title or price_element or add_to_cart
    
    def add_to_cart_from_details(self):
        """Add product to cart from product details page"""
        self.click("button:has-text('Add to Cart')")
        self.wait_for_page_load("networkidle")
    
    def get_success_message(self):
        """Get the success message after adding to cart"""
        return self.get_text(".alert-success")
