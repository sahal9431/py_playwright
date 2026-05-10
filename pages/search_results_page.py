class SearchResultsPage:
    def __init__(self, page):
        self.page = page
    
    def get_search_results(self):
        """Get all product titles from search results"""
        products = self.page.locator("h4 a")
        product_titles = []
        count = products.count()
        for i in range(count):
            title = products.nth(i).text_content()
            product_titles.append(title)
        return product_titles
    
    def select_first_product(self):
        """Click on the first product in search results"""
        first_product = self.page.locator("h4 a").first
        first_product.click()
        self.page.wait_for_load_state("networkidle")
    
    def is_product_details_displayed(self):
        """Verify if product details page is displayed"""
        # Check for product title and price elements on the details page
        product_title = self.page.locator("h1, .heading-title").is_visible(timeout=5000)
        price_element = self.page.locator("[id*='price'], [class*='price']").is_visible(timeout=5000)
        add_to_cart = self.page.locator("button", has_text="Add to Cart").is_visible(timeout=5000)
        return product_title or price_element or add_to_cart
    
    def add_to_cart_from_details(self):
        """Add product to cart from product details page"""
        add_to_cart_btn = self.page.locator("button", has_text="Add to Cart")
        add_to_cart_btn.click()
        self.page.wait_for_load_state("networkidle")
    
    def get_success_message(self):
        """Get the success message after adding to cart"""
        message = self.page.locator(".alert-success").text_content()
        return message
