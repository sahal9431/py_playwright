from pytest_bdd import scenarios, given, when, then, parsers
from pages.registration_page import RegistrationPage


scenarios("../features/register.feature")

@given("user is on register page")
def registration_page(browser_instance):
    registration_page = RegistrationPage(browser_instance)
    registration_page.navigate_to_registration_page()
    registration_page.verify_user_on_registration_page()

@when( parsers.parse( 'user registers with "{first_name}" "{last_name}" and "{newsletter}"' ) )
def user_registration( browser_instance, first_name, last_name, newsletter ): 
    registration_page = RegistrationPage(browser_instance) 
    registration_page.registration_details_filling( first_name=first_name, last_name=last_name, 
                                                   newsletter=newsletter.lower() == "yes" )
    registration_page.registration_submission()

@then("account should be created successfully")
def successful_registration(browser_instance):
    registration_page = RegistrationPage(browser_instance)
    registration_page.verify_succesful_registration()