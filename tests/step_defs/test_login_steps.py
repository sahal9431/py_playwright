from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.account_page import AccountPage


scenarios("../features/login_logout.feature")

@given("user is on login page")
def navigate_to_login_page(browser_instance):
    browser_instance.goto("https://awesomeqa.com/ui/index.php?route=account/login")

@when(parsers.parse("user login in with email {email} and password {password}"))
def enter_invalid_credentials(browser_instance, email, password):
    login_page = LoginPage(browser_instance)
    login_page.login(email, password)

@then("error message should be displayed")
def verify_error_message(browser_instance):
    login_page = LoginPage(browser_instance)
    error_message = login_page.get_error_message()
    assert "Warning" in error_message

@then("user should be navigated to home page")
def verify_home_page(browser_instance):
    login_page = LoginPage(browser_instance)
    assert login_page.home_icon_visible()

@given("user is logged in")
def user_logged_in(browser_instance):
    browser_instance.goto("https://awesomeqa.com/ui/index.php?route=account/login")
    login_page = LoginPage(browser_instance)
    login_page.login("leomessi107@gmail.com", "Worldcup@2022")
    assert login_page.home_icon_visible()

@when("user clicks on Logout")
def user_clicks_on_logout(browser_instance):
    account_page = AccountPage(browser_instance)
    account_page.logout()

@then("user should be logged out succesfully")
def verify_user_logged_out(browser_instance):
    account_page = AccountPage(browser_instance)
    assert account_page.is_logged_out()