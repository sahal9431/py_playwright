from pages.base_page import BasePage
import time
import random


class RegistrationPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        self.generated_email = None
        self.generated_phone = None

    def navigate_to_registration_page(self):
        """Navigate to the registration page"""
        self.navigate_to("https://awesomeqa.com/ui/index.php?route=account/login")
        self.click_by_role('link', 'Continue')

    def verify_user_on_registration_page(self):
        """Verify user is on the registration page"""
        self.assert_element_visible("//h1[text()='Register Account']")

    def registration_details_filling(self):
        """Fill registration form with generated unique credentials"""
        ts = int(time.time())
        rnd = random.randint(100, 999)
        email = f"asifms{ts}{rnd}@example.com"
        phone = str(random.randint(6000000000, 9999999999))
        self.generated_email = email
        self.generated_phone = phone

        self.send_data_by_placeholder("First Name", "Asif")
        self.send_data_by_placeholder("Last Name", "M S")
        self.send_data_by_placeholder("E-Mail", email)
        self.send_data_by_placeholder("Telephone", phone)
        self.send_data("#input-password", "Asif@1234")
        self.send_data("#input-confirm", "Asif@1234")
        self.check_checkbox("input[name='newsletter'][value='1']")
        self.check_checkbox("//input[@name = 'agree']")

    def registration_submission(self):
        """Submit the registration form"""
        self.click_by_role('button', 'Continue')

    def verify_succesful_registration(self):
        """Verify successful registration with timeout"""
        self.assert_element_visible("//h1[text()='Your Account Has Been Created!']", timeout=10000)
