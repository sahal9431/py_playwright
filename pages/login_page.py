from pages.base_page import BasePage


class LoginPage(BasePage):

    Email_Input = "#input-email"
    Password_Input = "#input-password"
    Error_message = ".alert-danger"
    Home_icon = "//h2[text()='My Account']"

    def login(self, email, password):
        self.send_data(self.Email_Input, email)
        self.send_data(self.Password_Input, password)
        self.click_by_role("button", "Login")
    
    def home_icon_visible(self):
        return self.is_visible(self.Home_icon)
    
    def get_error_message(self):
        return self.get_text(self.Error_message)