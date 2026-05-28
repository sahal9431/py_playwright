from Api_automation.api.base_api import BaseAPI
from Api_automation.api.auth_api import AuthAPI
from typing import Dict, List, Any, Optional


class OrderAPI(BaseAPI):
    """
    Order API module.
    Handles all order-related API calls including creation, retrieval, and updates.
    """

    CREATE_ORDER_ENDPOINT = "/api/ecom/order/create-order"
    GET_ORDERS_ENDPOINT = "/api/ecom/order/get-orders-for-customer/"
    GET_ORDER_DETAILS_ENDPOINT = "/api/ecom/order/get-orders-details"

    def __init__(self, base_url: str = "https://rahulshettyacademy.com"):
        """
        Initialize OrderAPI with base URL.
        
        Args:
            base_url (str): The base URL for API endpoints
        """
        super().__init__(base_url)
        self.auth_api = AuthAPI(base_url)

    def create_order(
        self,
        order_data: Dict[str, Any],
        token: Optional[str] = None
    ) -> str:
        """
        Create a new order.
        
        Args:
            order_data (Dict): Order details containing products and country
            token (str, optional): Authentication token
            
        Returns:
            str: Created order ID
            
        Raises:
            AssertionError: If order creation fails
        """
        if token:
            self.set_token(token)

        headers = self.get_headers(include_auth=True)
        headers["Content-Type"] = "application/json"

        response = self.post(
            self.CREATE_ORDER_ENDPOINT,
            data=order_data,
            headers=headers
        )

        self.verify_response_ok(response)
        response_body = self.get_response_json(response)
        
        # Extract order ID from response
        order_id = response_body.get("orders", [None])[0]
        return order_id

    def get_all_orders(self, customer_id: str, token: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retrieve all orders for a customer.
        
        Args:
            customer_id (str): Customer ID
            token (str, optional): Authentication token
            
        Returns:
            List: List of orders
            
        Raises:
            AssertionError: If request fails
        """
        if token:
            self.set_token(token)

        endpoint = f"{self.GET_ORDERS_ENDPOINT}{customer_id}"
        response = self.get(endpoint, include_auth=True)

        self.verify_response_ok(response)
        response_body = self.get_response_json(response)
        
        return response_body.get("data", [])

    def get_order_details(self, order_id: str, token: Optional[str] = None) -> Dict[str, Any]:
        """
        Get detailed information about a specific order.
        
        Args:
            order_id (str): Order ID
            token (str, optional): Authentication token
            
        Returns:
            Dict: Order details
            
        Raises:
            AssertionError: If request fails
        """
        if token:
            self.set_token(token)

        # Build query parameter endpoint
        endpoint = f"{self.GET_ORDER_DETAILS_ENDPOINT}?id={order_id}"
        response = self.get(endpoint, include_auth=True)

        self.verify_response_ok(response)
        response_body = self.get_response_json(response)
        
        return response_body

    def create_sample_order(self, token: str) -> str:
        """
        Create a sample order for testing.
        
        Args:
            token (str): Authentication token
            
        Returns:
            str: Created order ID
        """
        sample_order = {
            "orders": [
                {
                    "country": "India",
                    "productOrderedId": "6960eae1c941646b7a8b3ed3"
                }
            ]
        }

        return self.create_order(sample_order, token)

    def verify_order_response(self, order: Dict[str, Any]) -> bool:
        """
        Verify order response contains expected fields.
        
        Args:
            order (Dict): Order data
            
        Returns:
            bool: True if order is valid, False otherwise
        """
        required_fields = ["_id", "orderNumber"]
        return all(field in order for field in required_fields)

    def get_order_count(self, orders: List[Dict[str, Any]]) -> int:
        """
        Get count of orders.
        
        Args:
            orders (List): List of orders
            
        Returns:
            int: Number of orders
        """
        return len(orders)
