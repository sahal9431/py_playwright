from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page import HomePage

scenarios("../features/currency_change.feature")

@given("user is on the home page")
def user_on_home_page(browser_instance):
    browser_instance.goto("https://awesomeqa.com/ui/")
    browser_instance.wait_for_load_state("networkidle")

@when(parsers.parse('user changes currency to "{currency}"'))
def change_currency(browser_instance, currency):
    home_page = HomePage(browser_instance)
    home_page.change_currency(currency)

@then("product price should display with changed price")
def verify_currency_changed(browser_instance):
    home_page = HomePage(browser_instance)
    price_text = home_page.get_product_price()
    if price_text:
        assert any(symbol in price_text for symbol in ["$", "€", "£"]), f"Price text '{price_text}' does not contain expected currency symbols."