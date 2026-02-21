class LoginPage:

    Email_Input = "#input-email"
    Password_Input = "#input-password"
    Error_message = ".alert-danger"
    Home_icon = ".img-responsive"
    
    def __init__(self, page):
        self.page = page

    def login(self, email, password):
        self.page.fill(self.Email_Input, email)
        self.page.fill(self.Password_Input, password)
        self.page.get_by_role("button", name="Login").click()
    
    def home_icon_visible(self):
        return self.page.is_visible(self.Home_icon)
    
    def get_error_message(self):
        return self.page.locator(self.Error_message).text_content()