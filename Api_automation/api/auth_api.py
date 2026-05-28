from Api_automation.api.base_api import BaseAPI
from typing import Dict, Any


class AuthAPI(BaseAPI):
    """
    Authentication API module.
    Handles all authentication and login-related API calls.
    """

    AUTH_LOGIN_ENDPOINT = "/api/ecom/auth/login"

    def __init__(self, base_url: str = "https://rahulshettyacademy.com"):
        """
        Initialize AuthAPI with base URL.
        
        Args:
            base_url (str): The base URL for API endpoints
        """
        super().__init__(base_url)

    def login(self, email: str, password: str) -> Dict[str, Any]:
        """
        Login user and retrieve authentication token.
        
        Args:
            email (str): User email
            password (str): User password
            
        Returns:
            Dict: Login response containing token and user details
            
        Raises:
            AssertionError: If login fails
        """
        login_payload = {
            "userEmail": email,
            "userPassword": password
        }

        response = self.post(
            self.AUTH_LOGIN_ENDPOINT,
            data=login_payload,
            include_auth=False
        )

        self.verify_response_ok(response)
        response_body = self.get_response_json(response)
        
        # Store token for future requests
        if "token" in response_body:
            self.set_token(response_body["token"])
        
        return response_body

    def get_token(self, email: str, password: str) -> str:
        """
        Get authentication token for a user.
        
        Args:
            email (str): User email
            password (str): User password
            
        Returns:
            str: Authentication token
        """
        response = self.login(email, password)
        return response.get("token")

    def verify_login_response(self, response: Dict[str, Any]) -> bool:
        """
        Verify login response contains expected fields.
        
        Args:
            response (Dict): Login response
            
        Returns:
            bool: True if response is valid, False otherwise
        """
        required_fields = ["token", "userId", "message"]
        return all(field in response for field in required_fields)

    def get_user_details_from_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract user details from login response.
        
        Args:
            response (Dict): Login response
            
        Returns:
            Dict: User details (userId, firstName, lastName, email, etc.)
        """
        user_details = {
            "userId": response.get("userId"),
            "firstName": response.get("firstName"),
            "lastName": response.get("lastName"),
            "email": response.get("email")
        }
        return user_details
