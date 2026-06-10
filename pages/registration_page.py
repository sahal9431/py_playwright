from pages.base_page import BasePage
from utils.config import Config
import time
import random


class RegistrationPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        self.generated_email = None
        self.generated_phone = None

    def navigate_to_registration_page(self):
        """Navigate to the registration page"""
        self.navigate_to(Config.get_base_url() + "index.php?route=account/login")
        self.click_by_role('link', 'Continue')

    def verify_user_on_registration_page(self):
        """Verify user is on the registration page"""
        self.assert_element_visible("//h1[text()='Register Account']")

    def registration_details_filling(self, first_name=None, last_name=None, email=None, 
                                    phone=None, password=None, confirm_password=None, 
                                    newsletter=False, use_generated_email=True):
        """
        Fill registration form with provided data or generated credentials
        
        Args:
            first_name: First name (if None, uses default)
            last_name: Last name (if None, uses default)
            email: Email address (if None, generates unique email)
            phone: Phone number (if None, generates random)
            password: Password (if None, uses default)
            confirm_password: Confirm password (if None, uses default)
            newsletter: Newsletter checkbox (if True, checks it)
            use_generated_email: If True, generates unique email despite provided email
        """
        # Use provided data or defaults
        first_name = first_name or "Asif"
        last_name = last_name or "M S"
        password = password or "Asif@1234"
        confirm_password = confirm_password or password
        
        # Generate unique email if requested
        if use_generated_email or email is None:
            ts = int(time.time())
            rnd = random.randint(100, 999)
            email = f"asifms{ts}{rnd}@example.com"
        
        self.generated_email = email
        
        # Generate phone if not provided
        if phone is None:
            phone = str(random.randint(6000000000, 9999999999))
        
        self.generated_phone = phone

        self.send_data_by_placeholder("First Name", first_name)
        self.send_data_by_placeholder("Last Name", last_name)
        self.send_data_by_placeholder("E-Mail", email)
        self.send_data_by_placeholder("Telephone", phone)
        self.send_data("#input-password", password)
        self.send_data("#input-confirm", confirm_password)
        
        if newsletter:
            self.check_checkbox("input[name='newsletter'][value='1']")
        
        self.check_checkbox("//input[@name = 'agree']")

    def registration_submission(self):
        """Submit the registration form"""
        self.click_by_role('button', 'Continue')

    def verify_succesful_registration(self):
        """Verify successful registration with timeout"""
        self.assert_element_visible("//h1[text()='Your Account Has Been Created!']")
