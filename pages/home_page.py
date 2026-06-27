from pages.base_page import BasePage
from utils.config import Config


class HomePage(BasePage):
    
    def add_a_product_to_cart(self):
        """Add first available product to cart"""
        try:
            self.navigate_to(Config.get_base_url())
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
            self.navigate_to(Config.get_base_url())
        except Exception:
            pass
        self.send_data("input[name='search']", product_name)
        self.send_keys("input[name='search']", "Enter")
        self.wait_for_page_load("networkidle")

    def change_currency(self, currency):
        """Change the currency on the home page"""
        currency_map = {"EUR": "€ Euro",
        "GBP": "£ Pound Sterling",
        "USD": "$ US Dollar"}
        display_currency = currency_map.get(currency, currency)
        self.click("//span[text()='Currency']")
        self.page.get_by_text(display_currency).click()

    def get_product_price(self):
        """Get the price of the all product displayed on the home page"""
        product_prices = self.get_elements(".product-thumb .price")
        for price in product_prices:
            price_text = price.text_content()
            if price_text:
                return price_text.strip()
        return None
