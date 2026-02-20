import pytest
from pages.login_page import LoginPage

@pytest.fixture
def browser_instance(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture
def user_logged_in(browser_instance):
    browser_instance.goto("https://awesomeqa.com/ui/index.php?route=account/login")
    login_page = LoginPage(browser_instance)
    login_page.login("leomessi107@gmail.com", "Worldcup@2022")
    assert login_page.home_icon_visible()