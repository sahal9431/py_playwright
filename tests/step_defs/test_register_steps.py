from pytest_bdd import scenarios, given, when, then
from pages.registration_page import RegistrationPage


scenarios("../features/register.feature")

@given("user is on register page")
def registation_page(browser_instance):
    registration_page = RegistrationPage(browser_instance)
    registration_page.navigate_to_registration_page()
    registration_page.verify_user_on_registration_page()

@when("user enters valid registration details")
def enter_valid_details(browser_instance):
    registration_page = RegistrationPage(browser_instance)
    registration_page.registration_details_filling()

@when("user submits the registration form")
def registration_submisson(browser_instance):
    registration_page = RegistrationPage(browser_instance)
    registration_page.registration_submission()

@then("account should be created successfully")
def succesfull_registration(browser_instance):
    registration_page = RegistrationPage(browser_instance)
    registration_page.verify_succesful_registration()