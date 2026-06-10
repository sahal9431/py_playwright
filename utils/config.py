"""
Configuration module - Reads config from Excel and environment
"""
import os
from pathlib import Path
from utils.excel_reader import ExcelDataReader


class Config:
    """Configuration management from Excel and environment variables"""
    
    # Default values
    BASE_URL = "https://awesomeqa.com/ui/"
    BROWSER = "chromium"
    HEADLESS = False
    TIMEOUT = 30000
    
    _excel_config = None
    
    @classmethod
    def load_from_excel(cls, excel_path=None):
        """Load configuration from Excel file"""
        if excel_path is None:
            excel_path = Path(__file__).parent.parent / "data" / "test_data.xlsx"
        
        try:
            reader = ExcelDataReader(excel_path)
            config_data = reader.get_sheet_data("Config")
            
            # Convert list of dicts to dict
            for item in config_data:
                key = item.get("Key")
                value = item.get("Value")
                if key == "baseURL":
                    cls.BASE_URL = value
                elif key == "browser":
                    cls.BROWSER = value
                elif key == "headless":
                    cls.HEADLESS = value.lower() == "true" if isinstance(value, str) else value
                elif key == "timeout":
                    cls.TIMEOUT = int(value) if value else 30000
            
            reader.close()
            print(f"✅ Config loaded from Excel: {excel_path}")
        except Exception as e:
            print(f"⚠️ Warning: Could not load Excel config: {e}")
            print(f"   Using default values")
    
    @classmethod
    def get_base_url(cls):
        """Get base URL from environment or config"""
        return os.getenv("BASE_URL", cls.BASE_URL)
    
    @classmethod
    def get_browser(cls):
        """Get browser type"""
        return os.getenv("BROWSER", cls.BROWSER)
    
    @classmethod
    def get_headless(cls):
        """Get headless mode"""
        return os.getenv("HEADLESS", str(cls.HEADLESS)).lower() == "true"
    
    @classmethod
    def get_timeout(cls):
        """Get timeout in milliseconds"""
        return int(os.getenv("TIMEOUT", cls.TIMEOUT))


# Load config on module import
Config.load_from_excel()
