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
        
    def update_product_quantity(self, quantity):
        """Updates the quantity of a product in the cart by filling the quantity input and clicking the update button."""
        self.page.locator("input[name^='quantity']").fill(quantity)
        self.page.locator("button[data-original-title='Update']").click()

    def parse_money(self, text: str):
        """Helper method to parse a money string and return a float value."""
        if not text:
            return None
        match = text.replace("$", "").replace(",", "").strip()
        try:
            return float(match)
        except ValueError:
                raise ValueError(f"Could not parse money value from text: {text}")

    def get_cart_total(self):
        """Retrieves the cart total amount from the cart page. 
        and verifies that the total is updated correctly based on the new quantity."""
        rows = self.page.locator("#content form table tbody tr")
        rows.first.wait_for(state = "visible")
        print(f"Found {rows.count()} rows in the cart table.")
        for i in range(rows.count()):
            row = rows.nth(i)
            unit_price = self.parse_money(row.locator("td").nth(4).inner_text())
            total = self.parse_money(row.locator("td").nth(5).inner_text())
            quantity = int(row.locator("input[type='text']").input_value())
            assert round(unit_price * quantity, 2) == round(total, 2), f"Expected total: {unit_price} * {quantity} = {round(unit_price * quantity, 2)}, but got: {total}"