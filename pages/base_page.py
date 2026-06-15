from playwright.sync_api import expect, Page
from typing import List, Optional


class BasePage:
    """
    Base page class that provides common actions for all page objects.
    All page classes should inherit from this class to reuse common methods.
    """

    def __init__(self, page: Page):
        """
        Initialize the BasePage with a Playwright page object.
        
        Args:
            page (Page): Playwright page object
        """
        self.page = page

    # ============ Navigation Methods ============
    def navigate_to(self, url):
        """
        Navigate to a specific URL.
        
        """
        self.page.goto(url)

    def go_back(self) -> None:
        """Go back to the previous page."""
        self.page.go_back()

    def go_forward(self) -> None:
        """Go forward to the next page."""
        self.page.go_forward()

    def reload_page(self) -> None:
        """Reload the current page."""
        self.page.reload()

    # ============ Click Methods ============
    def click(self, locator: str):
        """
        Click on an element.
        """
        self.page.locator(locator).click()

    def click_by_role(self, role, name):
        """
        Click on an element by role and name.
        """
        self.page.get_by_role(role, name=name).click()

    def click_by_text(self, text: str) -> None:
        """
        Click on an element that contains specific text.
        
        Args:
            text (str): Text content to search for
        """
        self.page.get_by_text(text).click()

    def click_nth_element(self, locator: str, index: int):
        """
        Click on the nth occurrence of an element.
        """
        self.page.locator(locator).nth(index).click()

    def double_click(self, locator: str) -> None:
        """
        Double-click on an element.
        
        Args:
            locator (str): CSS selector or XPath of the element
        """
        self.page.locator(locator).dbl_click()

    def right_click(self, locator: str) -> None:
        """
        Right-click on an element.
        
        Args:
            locator (str): CSS selector or XPath of the element
        """
        self.page.locator(locator).click(button="right")

    # ============ Input Methods ============
    def send_data(self, locator, text):
        """
        Fill an input field with text.
        """
        self.page.locator(locator).fill(text)

    def send_data_by_placeholder(self, placeholder, text):
        """
        Fill an input field by placeholder attribute.
        
        """
        self.page.get_by_placeholder(placeholder).fill(text)

    def send_keys(self, locator, key_sequence):
        """
        Press specific keys on an element.
        
        Args:
            locator (str): CSS selector or XPath of the element
            key_sequence (str): Key sequence to press (e.g., 'Enter', 'Tab', 'Control+A')
        """
        self.page.locator(locator).press(key_sequence)

    def type_text(self, locator: str, text: str, delay: int = 0) -> None:
        """
        Type text character by character (slower than fill).
        
        Args:
            locator (str): CSS selector or XPath of the input field
            text (str): Text to type
            delay (int): Delay between key presses in milliseconds
        """
        self.page.locator(locator).type(text, delay=delay)

    def clear_input(self, locator: str) -> None:
        """
        Clear an input field.
        
        Args:
            locator (str): CSS selector or XPath of the input field
        """
        self.page.locator(locator).clear()

    # ============ Checkbox & Radio Methods ============
    def check_checkbox(self, locator):
        """
        Check a checkbox.
        """
        self.page.locator(locator).check()

    def uncheck_checkbox(self, locator):
        """
        Uncheck a checkbox.
        """
        self.page.locator(locator).uncheck()

    def is_checkbox_checked(self, locator: str) -> bool:
        """
        Check if a checkbox is checked.
        
        Args:
            locator (str): CSS selector or XPath of the checkbox
            
        Returns:
            bool: True if checked, False otherwise
        """
        return self.page.locator(locator).is_checked()

    def select_radio_button(self, locator: str) -> None:
        """
        Select a radio button.
        
        Args:
            locator (str): CSS selector or XPath of the radio button
        """
        self.page.locator(locator).check()

    # ============ Dropdown/Select Methods ============
    def select_by_value(self, locator: str, value: str) -> None:
        """
        Select an option from a dropdown by value.
        
        Args:
            locator (str): CSS selector or XPath of the select element
            value (str): Value of the option to select
        """
        self.page.locator(locator).select_option(value)

    def select_by_label(self, locator: str, label: str) -> None:
        """
        Select an option from a dropdown by label.
        
        Args:
            locator (str): CSS selector or XPath of the select element
            label (str): Label text of the option to select
        """
        self.page.locator(locator).select_option(label=label)

    def get_selected_value(self, locator: str) -> str:
        """
        Get the currently selected value from a dropdown.
        
        Args:
            locator (str): CSS selector or XPath of the select element
            
        Returns:
            str: The selected value
        """
        return self.page.locator(locator).input_value()

    # ============ Visibility Methods ============
    def is_visible(self, locator):
        """
        Check if an element is visible.
        """
        try:
            self.page.wait_for_load_state("networkidle")
            return self.page.locator(locator).is_visible()
        except Exception:
            return False

    def is_hidden(self, locator: str) -> bool:
        """
        Check if an element is hidden.
        
        Args:
            locator (str): CSS selector or XPath of the element
            
        Returns:
            bool: True if hidden, False otherwise
        """
        return self.page.locator(locator).is_hidden()

    def is_element_present(self, locator: str) -> bool:
        """
        Check if an element is present on the page.
        
        Args:
            locator (str): CSS selector or XPath of the element
            
        Returns:
            bool: True if present, False otherwise
        """
        try:
            return self.page.locator(locator).count() > 0
        except Exception:
            return False

    def wait_for_element_visible(self, locator: str, timeout: int = 5000) -> None:
        """
        Wait for an element to be visible.
        
        Args:
            locator (str): CSS selector or XPath of the element
            timeout (int): Timeout in milliseconds
        """
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)

    def wait_for_element_hidden(self, locator: str, timeout: int = 5000) -> None:
        """
        Wait for an element to be hidden.
        
        Args:
            locator (str): CSS selector or XPath of the element
            timeout (int): Timeout in milliseconds
        """
        self.page.locator(locator).wait_for(state="hidden", timeout=timeout)

    # ============ Text Methods ============
    def get_text(self, locator):
        """
        Get text content from an element.
        """
        return self.page.locator(locator).text_content()

    def get_inner_text(self, locator: str) -> str:
        """
        Get inner text content from an element.
        
        Args:
            locator (str): CSS selector or XPath of the element
            
        Returns:
            str: Inner text content of the element
        """
        return self.page.locator(locator).inner_text()

    def get_attribute(self, locator: str, attribute_name: str) -> Optional[str]:
        """
        Get the value of an attribute from an element.
        
        Args:
            locator (str): CSS selector or XPath of the element
            attribute_name (str): Name of the attribute
            
        Returns:
            str: Value of the attribute
        """
        return self.page.locator(locator).get_attribute(attribute_name)

    def get_input_value(self, locator: str) -> str:
        """
        Get the value of an input field.
        
        Args:
            locator (str): CSS selector or XPath of the input field
            
        Returns:
            str: Value of the input field
        """
        return self.page.locator(locator).input_value()

    # ============ Element Count Methods ============
    def get_element_count(self, locator: str) -> int:
        """
        Get the count of elements matching the locator.
        
        Args:
            locator (str): CSS selector or XPath of the element
            
        Returns:
            int: Number of elements matching the locator
        """
        return self.page.locator(locator).count()

    def get_all_text_contents(self, locator: str):
        """
        Get text content from all matching elements.
        """
        elements = self.page.locator(locator)
        count = elements.count()
        contents = []
        for i in range(count):
            contents.append(elements.nth(i).text_content())
        return contents

    # ============ Wait Methods ============
    def wait_for_page_load(self, state):
        """
        Wait for the page to load.
        """
        self.page.wait_for_load_state(state)

    def wait_for_url(self, url: str, timeout: int = 5000):
        """
        Wait for the page URL to match a specific pattern.
        
        Args:
            url (str): URL or URL pattern to wait for
            timeout (int): Timeout in milliseconds
        """
        self.page.wait_for_url(url, timeout=timeout)

    def wait_for_function(self, script: str, timeout: int = 5000) -> None:
        """
        Wait for a JavaScript function to return true.
        
        Args:
            script (str): JavaScript code that returns a boolean
            timeout (int): Timeout in milliseconds
        """
        self.page.wait_for_function(script, timeout=timeout)

    # ============ JavaScript Execution Methods ============
    def execute_script(self, script: str, arg: Optional[object] = None) -> object:
        """
        Execute JavaScript on the page.
        
        Args:
            script (str): JavaScript code to execute
            arg (object): Optional argument to pass to the script
            
        Returns:
            object: Result of the JavaScript execution
        """
        return self.page.evaluate(script, arg)

    def scroll_to_element(self, locator: str) -> None:
        """
        Scroll to an element.
        
        Args:
            locator (str): CSS selector or XPath of the element
        """
        self.page.locator(locator).scroll_into_view_if_needed()

    def scroll_to_top(self) -> None:
        """Scroll to the top of the page."""
        self.page.evaluate("window.scrollTo(0, 0)")

    def scroll_to_bottom(self) -> None:
        """Scroll to the bottom of the page."""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # ============ Screenshot Methods ============
    def take_screenshot(self, filename: str = None) -> bytes:
        """
        Take a screenshot of the page.
        
        Args:
            filename (str): Optional filename to save the screenshot
            
        Returns:
            bytes: Screenshot data if filename is not provided
        """
        if filename:
            return self.page.screenshot(path=filename)
        else:
            return self.page.screenshot()

    # ============ Assertion Methods ============
    def assert_element_visible(self, locator):
        """
        Assert that an element is visible.
        """
        expect(self.page.locator(locator)).is_visible()

    def assert_element_hidden(self, locator):
        """
        Assert that an element is hidden.
        
        Args:
            locator (str): CSS selector or XPath of the element
            timeout (int): Timeout in milliseconds
        """
        expect(self.page.locator(locator)).to_be_hidden()

    def assert_text_present(self, locator: str, text: str, timeout: int = 5000) -> None:
        """
        Assert that an element contains specific text.
        
        Args:
            locator (str): CSS selector or XPath of the element
            text (str): Text to verify
            timeout (int): Timeout in milliseconds
        """
        expect(self.page.locator(locator)).to_contain_text(text, timeout=timeout)

    def assert_element_enabled(self, locator: str) -> None:
        """
        Assert that an element is enabled.
        
        Args:
            locator (str): CSS selector or XPath of the element
        """
        expect(self.page.locator(locator)).to_be_enabled()

    def assert_element_disabled(self, locator: str) -> None:
        """
        Assert that an element is disabled.
        
        Args:
            locator (str): CSS selector or XPath of the element
        """
        expect(self.page.locator(locator)).to_be_disabled()

    def assert_url(self, url: str) -> None:
        """
        Assert that the current URL matches the expected URL.
        
        Args:
            url (str): Expected URL
        """
        expect(self.page).to_have_url(url)

    def assert_title(self, title: str) -> None:
        """
        Assert that the page title matches the expected title.
        
        Args:
            title (str): Expected page title
        """
        expect(self.page).to_have_title(title)

    # ============ Utility Methods ============
    def get_page_title(self) -> str:
        """
        Get the current page title.
        
        Returns:
            str: Page title
        """
        return self.page.title()

    def get_page_url(self) -> str:
        """
        Get the current page URL.
        
        Returns:
            str: Current page URL
        """
        return self.page.url

    def switch_to_iframe(self, locator: str):
        """
        Switch to an iframe.
        
        Args:
            locator (str): CSS selector or XPath of the iframe
            
        Returns:
            Page: Iframe page object
        """
        return self.page.locator(locator).content_frame

    def switch_to_parent_page(self) -> Page:
        """
        Switch back to parent page from iframe.
        
        Returns:
            Page: Parent page object
        """
        return self.page.main_frame.parent_frame

    def get_current_page(self) -> Page:
        """
        Get the current page object.
        
        Returns:
            Page: Current page object
        """
        return self.page
