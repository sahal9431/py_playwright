import pytest
from pathlib import Path
from datetime import datetime
from pages.login_page import LoginPage
import allure
from playwright.sync_api import Page
from utils.config import Config

@pytest.fixture 
def browser_instance(playwright, request): 
    browser = playwright.chromium.launch( headless=Config.get_headless() ) 
    context = browser.new_context() 
    page = context.new_page() 
    page.set_default_timeout(Config.get_timeout()) 
    yield page 
    # Capture screenshot only on failure 
    if ( hasattr(request.node, "rep_call") and request.node.rep_call.failed ): 
        test_name = (request.node.name.split("[")[0].replace("test_", ""))
        attach_screenshot(page, test_name)
    # Cleanup 
    context.close() 
    browser.close()

def attach_screenshot(page: Page, test_name: str): 
    """ Capture screenshot and attach to Allure report """ 
    screenshots_dir = Path.cwd() / "screenshots" 
    screenshots_dir.mkdir(exist_ok=True) 
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S") 
    screenshot_path = screenshots_dir / f"{test_name}-{timestamp}.png" 
    try: 
        if not page.is_closed():
            page.screenshot(path=str(screenshot_path), full_page=True)
            with open(screenshot_path, "rb") as file: allure.attach( file.read(), name="failure_screenshot", attachment_type=allure.attachment_type.PNG )
            print(f"\nScreenshot saved: {screenshot_path}")
    except Exception as e: 
        print(f"\nFailed to capture screenshot: {e}")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
     outcome = yield 
     report = outcome.get_result() 
     setattr(item, f"rep_{report.when}", report) 
     if report.when == "call": 
        allure.dynamic.title(item.name)
        if report.failed: 
            allure.dynamic.description( f"Test failed:\n{report.longreprtext}" )

@pytest.fixture
def user_logged_in(browser_instance):
    browser_instance.goto( f"{Config.get_base_url()}index.php?route=account/login" )
    login_page = LoginPage(browser_instance)
    login_page.login( "leomessi107@gmail.com", "Worldcup@2022" )
    assert login_page.home_icon_visible()
    return browser_instance