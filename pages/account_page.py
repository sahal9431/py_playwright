
class AccountPage:
    def __init__(self, page):
        self.page = page

    def logout(self):
        self.page.locator("a[title='My Account']").click()
        self.page.locator("#top-links a[href*='route=account/logout']").click()

    def is_logged_out(self):
        return self.page.get_by_role("heading", name="Account Logout").is_visible()