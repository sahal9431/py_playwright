import pytest
import os
from pathlib import Path
from datetime import datetime
from pages.login_page import LoginPage
from utils.excel_reader import ExcelDataReader
import allure
from playwright.sync_api import Page


@pytest.fixture
def excel_data():
    """Fixture to provide Excel data reader"""
    data_file = Path(__file__).parent / "data" / "test_data.xlsx"
    reader = ExcelDataReader(str(data_file))
    yield reader
    reader.close()


@pytest.fixture
def registration_data(excel_data):
    """Get all registration test data from Excel"""
    return excel_data.get_sheet_data("RegistrationData")


@pytest.fixture
def login_data(excel_data):
    """Get all login test data from Excel"""
    return excel_data.get_sheet_data("LoginData")


@pytest.fixture
def search_data(excel_data):
    """Get all search test data from Excel"""
    return excel_data.get_sheet_data("SearchData")

@pytest.fixture
def browser_instance(playwright, request):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page   # <-- test runs here
    # teardown starts here
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshots_dir = Path.cwd() / "screenshots"
        screenshots_dir.mkdir(exist_ok=True)
        name = request.node.nodeid.replace("::", "_").replace("/", "_")
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        path = screenshots_dir / f"{name}-{ts}.png"
        try:
            if not page.is_closed():
                page.screenshot(path=str(path), full_page=True)
                print(f"\nScreenshot saved: {path}")
                # Attach screenshot to Allure report
                with open(path, 'rb') as f:
                    allure.attach(f.read(), name="failure_screenshot", 
                                attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"\nFailed to capture screenshot: {e}")

    page.close()
    context.close()
    browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    
    # Add test result to Allure
    if rep.when == "call":
        if rep.failed:
            allure.dynamic.title(item.name)
            allure.dynamic.description(f"Test failed with error: {rep.longreprtext}")
        elif rep.passed:
            allure.dynamic.title(item.name)

@pytest.fixture
def user_logged_in(browser_instance):
    # perform explicit login so the scenario has a logged-in user
    browser_instance.goto("https://awesomeqa.com/ui/index.php?route=account/login")
    login_page = LoginPage(browser_instance)
    login_page.login("leomessi107@gmail.com", "Worldcup@2022")
    assert login_page.home_icon_visible()
    return browser_instance