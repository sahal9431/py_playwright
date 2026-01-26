
class BasePage:
    def __init__(self, page):
        self.page = page

    def click_element(self, locator):
        self.page.click(locator)
    
    def fill_input(self, locator, text):
        self.page.fill(locator, text)