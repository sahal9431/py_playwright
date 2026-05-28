from pages.base_page import BasePage


class CartPage(BasePage):
    
    def remove_product_from_cart(self):
        """Remove a product from the cart by clicking the remove button"""
        self.click(".fa-times-circle")
    
    def verify_cart_is_empty(self):
        """Verify that the cart is empty by checking for the empty cart message"""
        locator = "//p[text()='Your shopping cart is empty!']"
        try:
            return self.page.locator(locator).first.text_content()
        except Exception:
            return self.get_text(locator)
        
    def update_product_quantity(self, quantity):
        """Update the quantity of a product in the cart"""
        self.send_data("input[name^='quantity']", quantity)
        self.click("button[data-original-title='Update']")

    def parse_money(self, text: str):
        """Helper method to parse a money string and return a float value"""
        if not text:
            return None
        match = text.replace("$", "").replace(",", "").strip()
        try:
            return float(match)
        except ValueError:
            raise ValueError(f"Could not parse money value from text: {text}")

    def get_cart_total(self):
        """Retrieve and verify cart total amount based on product quantities"""
        rows = self.page.locator("#content form table tbody tr")
        rows.first.wait_for(state="visible")
        print(f"Found {rows.count()} rows in the cart table.")
        for i in range(rows.count()):
            row = rows.nth(i)
            unit_price = self.parse_money(row.locator("td").nth(4).inner_text())
            total = self.parse_money(row.locator("td").nth(5).inner_text())
            quantity = int(row.locator("input[type='text']").input_value())
            assert round(unit_price * quantity, 2) == round(total, 2), f"Expected total: {unit_price} * {quantity} = {round(unit_price * quantity, 2)}, but got: {total}"