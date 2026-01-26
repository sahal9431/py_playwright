import pytest


@pytest.fixture
def browser_instance(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
