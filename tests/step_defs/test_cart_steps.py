from pages.cart_page import CartPage
from pages.home_page import HomePage
from pytest_bdd import scenarios, given, when, then

scenarios("../features/cart.feature")

@given("user is logged in")
def user_logged_in(browser_instance):
    pass

@when("user adds a product to cart")
def add_product_to_cart(browser_instance):
    home_page = HomePage(browser_instance)
    home_page.add_a_product_to_cart()
    home_page.get_success_message()

@when("user opens the cart")
def open_cart(browser_instance):
    home_page = HomePage(browser_instance)
    home_page.open_cart()
    home_page.open_view_cart()

@then("user removes the product from cart")
def remove_product_from_cart(browser_instance):
    cart_page = CartPage(browser_instance)
    cart_page.remove_product_from_cart()

@then("cart should be empty")
def verify_cart_is_empty(browser_instance):
    cart_page = CartPage(browser_instance)
    cart_page.verify_cart_is_empty()