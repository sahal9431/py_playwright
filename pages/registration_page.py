from playwright.sync_api import expect


class RegistrationPage:
    def __init__(self, page):
        self.page = page
    
    def navigate_to_registration_page(self):
        self.page.goto("https://awesomeqa.com/ui/index.php?route=account/login")
        self.page.get_by_role('link', name='Continue').click()
    
    def verify_user_on_registration_page(self):
        expect(self.page.locator("//h1[text()='Register Account']")).to_be_visible()

    def registration_details_filling(self):
        self.page.get_by_placeholder("First Name").fill("Asif")
        self.page.get_by_placeholder("Last Name").fill("M S")
        self.page.get_by_placeholder("E-Mail").fill("asifms123466@gmail.com")
        self.page.get_by_placeholder("Telephone").fill("1234567891")
        self.page.locator("#input-password").fill("Asif@1234")
        self.page.locator("#input-confirm").fill("Asif@1234")
        self.page.check("input[name='newsletter'][value='1']")
        self.page.check("//input[@name = 'agree']")

    def registration_submission(self):
        self.page.get_by_role('button', name='Continue').click()
    
    def verify_succesful_registration(self):
        expect(self.page.locator("//h1[text()='Your Account Has Been Created!']")).to_be_visible()
