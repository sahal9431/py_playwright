from pages.base_page import BasePage


class AccountPage(BasePage):

    def logout(self):
        """Logout from the account"""
        self.click("a[title='My Account']")
        self.click("#top-links a[href*='route=account/logout']")

    def is_logged_out(self):
        """Check if user is logged out"""
        return self.is_visible("//h1[text()='Account Logout']")