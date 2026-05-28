from playwright.sync_api import APIRequestContext, Playwright
from typing import Dict, Any, Optional


class BaseAPI:
    """
    Base API class for all API endpoints.
    Provides common functionality for API interactions.
    """

    def __init__(self, base_url: str = "https://rahulshettyacademy.com"):
        """
        Initialize Base API with base URL.
        
        Args:
            base_url (str): The base URL for API endpoints
        """
        self.base_url = base_url
        self.request_context: Optional[APIRequestContext] = None
        self.token: Optional[str] = None

    def set_request_context(self, request_context: APIRequestContext) -> None:
        """
        Set the Playwright API request context.
        
        Args:
            request_context (APIRequestContext): The request context
        """
        self.request_context = request_context

    def set_token(self, token: str) -> None:
        """
        Set authentication token for subsequent requests.
        
        Args:
            token (str): Authentication token
        """
        self.token = token

    def get_headers(self, include_auth: bool = True) -> Dict[str, str]:
        """
        Get request headers with optional authentication.
        
        Args:
            include_auth (bool): Whether to include authorization header
            
        Returns:
            Dict: Headers dictionary
        """
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        if include_auth and self.token:
            headers["Authorization"] = self.token
        
        return headers

    def post(
        self,
        endpoint: str,
        data: Dict[str, Any] = None,
        headers: Dict[str, str] = None,
        include_auth: bool = True
    ) -> Any:
        """
        Make a POST request.
        
        Args:
            endpoint (str): API endpoint path
            data (Dict): Request body data
            headers (Dict): Custom headers
            include_auth (bool): Include authorization header
            
        Returns:
            Response object
        """
        if not self.request_context:
            raise RuntimeError("Request context not set. Use set_request_context() first.")
        
        if headers is None:
            headers = self.get_headers(include_auth)
        
        response = self.request_context.post(endpoint, data=data, headers=headers)
        return response

    def get(
        self,
        endpoint: str,
        headers: Dict[str, str] = None,
        include_auth: bool = True
    ) -> Any:
        """
        Make a GET request.
        
        Args:
            endpoint (str): API endpoint path
            headers (Dict): Custom headers
            include_auth (bool): Include authorization header
            
        Returns:
            Response object
        """
        if not self.request_context:
            raise RuntimeError("Request context not set. Use set_request_context() first.")
        
        if headers is None:
            headers = self.get_headers(include_auth)
        
        response = self.request_context.get(endpoint, headers=headers)
        return response

    def put(
        self,
        endpoint: str,
        data: Dict[str, Any] = None,
        headers: Dict[str, str] = None,
        include_auth: bool = True
    ) -> Any:
        """
        Make a PUT request.
        
        Args:
            endpoint (str): API endpoint path
            data (Dict): Request body data
            headers (Dict): Custom headers
            include_auth (bool): Include authorization header
            
        Returns:
            Response object
        """
        if not self.request_context:
            raise RuntimeError("Request context not set. Use set_request_context() first.")
        
        if headers is None:
            headers = self.get_headers(include_auth)
        
        response = self.request_context.put(endpoint, data=data, headers=headers)
        return response

    def delete(
        self,
        endpoint: str,
        headers: Dict[str, str] = None,
        include_auth: bool = True
    ) -> Any:
        """
        Make a DELETE request.
        
        Args:
            endpoint (str): API endpoint path
            headers (Dict): Custom headers
            include_auth (bool): Include authorization header
            
        Returns:
            Response object
        """
        if not self.request_context:
            raise RuntimeError("Request context not set. Use set_request_context() first.")
        
        if headers is None:
            headers = self.get_headers(include_auth)
        
        response = self.request_context.delete(endpoint, headers=headers)
        return response

    def create_request_context(self, playwright: Playwright) -> APIRequestContext:
        """
        Create a new API request context.
        
        Args:
            playwright (Playwright): Playwright instance
            
        Returns:
            APIRequestContext: The created request context
        """
        self.request_context = playwright.request.new_context(base_url=self.base_url)
        return self.request_context

    def verify_response_ok(self, response: Any) -> None:
        """
        Verify that API response is successful.
        
        Args:
            response: API response object
            
        Raises:
            AssertionError: If response is not OK
        """
        assert response.ok, f"API request failed with status {response.status}: {response.text()}"

    def get_response_json(self, response: Any) -> Dict[str, Any]:
        """
        Get JSON response body.
        
        Args:
            response: API response object
            
        Returns:
            Dict: Response JSON
        """
        return response.json()
