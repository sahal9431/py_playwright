from pytest_bdd import scenarios, given, when, then, parsers
from pages.registration_page import RegistrationPage


scenarios("../features/register.feature")

@given("user is on register page")
def registration_page(browser_instance):
    registration_page = RegistrationPage(browser_instance)
    registration_page.navigate_to_registration_page()
    registration_page.verify_user_on_registration_page()

@when(parsers.parse('user enters "{user_input}" as first name'))
def enter_first_name(browser_instance, user_input):
    registration_page = RegistrationPage(browser_instance)
    registration_page.send_data_by_placeholder("First Name", user_input)

@when(parsers.parse('user enters "{user_input}" as last name'))
def enter_last_name(browser_instance, user_input):
    registration_page = RegistrationPage(browser_instance)
    registration_page.send_data_by_placeholder("Last Name", user_input)

@when(parsers.parse('user enters "{user_input}" as email'))
def enter_email(browser_instance, user_input):
    registration_page = RegistrationPage(browser_instance)
    registration_page.send_data_by_placeholder("E-Mail", user_input)

@when(parsers.parse('user enters "{user_input}" as telephone'))
def enter_telephone(browser_instance, user_input):
    registration_page = RegistrationPage(browser_instance)
    registration_page.send_data_by_placeholder("Telephone", user_input)

@when(parsers.parse('user enters "{user_input}" as password'))
def enter_password(browser_instance, user_input):
    registration_page = RegistrationPage(browser_instance)
    registration_page.send_data("#input-password", user_input)

@when(parsers.parse('user enters "{user_input}" as confirm password'))
def enter_confirm_password(browser_instance, user_input):
    registration_page = RegistrationPage(browser_instance)
    registration_page.send_data("#input-confirm", user_input)

@when(parsers.parse('user selects newsletter "{newsletter}"'))
def select_newsletter(browser_instance, newsletter):
    registration_page = RegistrationPage(browser_instance)
    if newsletter.lower() == "yes":
        registration_page.check_checkbox("input[name='newsletter'][value='1']")

@when("user agrees to terms and conditions")
def agree_to_terms(browser_instance):
    registration_page = RegistrationPage(browser_instance)
    registration_page.check_checkbox("//input[@name = 'agree']")

@when("user submits the registration form")
def registration_submission(browser_instance):
    registration_page = RegistrationPage(browser_instance)
    registration_page.registration_submission()

@then("account should be created successfully")
def successful_registration(browser_instance):
    registration_page = RegistrationPage(browser_instance)
    registration_page.verify_succesful_registration()