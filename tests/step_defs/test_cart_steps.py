from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../features/cart.feature")

@given("user is logged in")
def user_logged_in(browser_instance):
    # perform explicit login so the scenario has a logged-in user
    browser_instance.goto("https://awesomeqa.com/ui/index.php?route=account/login")
    login_page = LoginPage(browser_instance)
    login_page.login("leomessi107@gmail.com", "Worldcup@2022")
    assert login_page.home_icon_visible()

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

@when(parsers.parse('user updates quantity to {quantity}'))
def update_product_quantity(browser_instance, quantity):
    cart_page = CartPage(browser_instance)
    cart_page.update_product_quantity(quantity)

@then("cart total should update correctly")
def verify_cart_total_updated(browser_instance):
    cart_page = CartPage(browser_instance)
    cart_page.get_cart_total()
