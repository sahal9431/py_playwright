import os


class Config:
    """Configuration module Reads configuration from environment variables"""
    
    BASE_URL = "https://awesomeqa.com/ui/"
    BROWSER = "chromium"
    HEADLESS = True
    TIMEOUT = 30000
    
    @classmethod
    def get_base_url(cls):
        return os.getenv("BASE_URL", cls.BASE_URL)
    
    @classmethod
    def get_browser(cls):
        """Get browser type"""
        return os.getenv("BROWSER", cls.BROWSER)
    
    @classmethod
    def get_headless(cls):
        """Get headless mode"""
        # Always headless in CI (Jenkins sets CI=true automatically)
        if os.getenv("CI", "false").lower() == "true":
            return True
        return os.getenv("HEADLESS", str(cls.HEADLESS)).lower() == "true"
    
    @classmethod
    def get_timeout(cls):
        """Get timeout in milliseconds"""
        return int(os.getenv("TIMEOUT", cls.TIMEOUT))

