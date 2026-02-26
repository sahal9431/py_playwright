import pytest
import os
from pathlib import Path
from datetime import datetime
from pages.login_page import LoginPage


@pytest.fixture
def browser_instance(playwright, request):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page   # <-- test runs here
    # teardown starts here
    if request.node.rep_call.failed:
        screenshots_dir = Path.cwd() / "screenshots"
        screenshots_dir.mkdir(exist_ok=True)
        name = request.node.nodeid.replace("::", "_").replace("/", "_")
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        path = screenshots_dir / f"{name}-{ts}.png"
        page.screenshot(path=str(path), full_page=True)
        print(f"\nScreenshot saved: {path}")
    page.close()
    context.close()
    browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture
def user_logged_in(browser_instance):
    # perform explicit login so the scenario has a logged-in user
    browser_instance.goto("https://awesomeqa.com/ui/index.php?route=account/login")
    login_page = LoginPage(browser_instance)
    login_page.login("leomessi107@gmail.com", "Worldcup@2022")
    assert login_page.home_icon_visible()
    return browser_instance