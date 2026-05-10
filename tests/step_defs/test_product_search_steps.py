from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../features/product_search.feature")

@given("user is on the home page")
def user_on_home_page(browser_instance):
    browser_instance.goto("https://awesomeqa.com/ui/")
    browser_instance.wait_for_load_state("networkidle")

@when(parsers.parse('user searches for "{product_name}"'))
def search_product(browser_instance, product_name):
    home_page = HomePage(browser_instance)
    home_page.search_for_product(product_name)

@then(parsers.parse('search results should display products containing "{keyword}"'))
def verify_search_results(browser_instance, keyword):
    search_results = SearchResultsPage(browser_instance)
    results = search_results.get_search_results()
    assert len(results) > 0, "No search results found"
    # Verify at least one result contains the keyword
    matching_results = [r for r in results if keyword.lower() in r.lower()]
    assert len(matching_results) > 0, f"No products containing '{keyword}' found in results"

@when("user selects the first product from search results")
def select_first_product(browser_instance):
    search_results = SearchResultsPage(browser_instance)
    search_results.select_first_product()

@then("product details page should be displayed")
def verify_product_details_page(browser_instance):
    search_results = SearchResultsPage(browser_instance)
    assert search_results.is_product_details_displayed(), "Product details page is not displayed"

@then("user can add product to cart from details page")
def add_product_from_details(browser_instance):
    search_results = SearchResultsPage(browser_instance)
    search_results.add_to_cart_from_details()
    message = search_results.get_success_message()
    assert message is not None, "Success message not displayed"
    assert "Success" in message or "added" in message.lower(), "Product was not added to cart"
