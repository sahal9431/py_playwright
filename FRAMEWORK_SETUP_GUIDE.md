# API Automation Framework Setup Guide

## ✅ Framework Created Successfully!

Your `Api_automation` folder has been transformed into a professional test automation framework with the following structure:

### 📂 Directory Structure

```
Api_automation/
├── config/
│   ├── __init__.py
│   └── settings.py           # API & test configuration
├── fixtures/
│   ├── __init__.py
│   └── api_fixtures.py       # Pytest fixtures
├── models/
│   ├── __init__.py
│   └── api_models.py         # Data models (LoginRequest, Order, etc.)
├── services/
│   ├── __init__.py
│   └── api_client.py         # API services (AuthService, OrderService, etc.)
├── tests/
│   ├── __init__.py
│   └── test_example.py       # Example test cases
├── utils/
│   ├── __init__.py
│   ├── apiBase.py            # Original base API class
│   └── helpers.py            # Utility helpers & validators
├── api/                      # Original API endpoint files
│   ├── auth_api.py
│   ├── base_api.py
│   └── order_api.py
├── conftest.py               # Pytest configuration & fixtures
├── pytest.ini                # Pytest settings
├── .env.example              # Environment variables template
└── README.md                 # Complete documentation
```

### 🎯 Key Features

1. **Config Management** (`config/settings.py`)
   - Centralized configuration
   - Environment-based settings
   - Easy to modify base URLs, timeouts, credentials

2. **Data Models** (`models/api_models.py`)
   - Type-safe request/response models
   - LoginRequest, LoginResponse, Order, OrderResponse
   - Easy serialization/deserialization

3. **API Services** (`services/api_client.py`)
   - Base APIClient class with HTTP methods (GET, POST, PUT, DELETE)
   - AuthService for login operations
   - OrderService for order operations
   - ProductService for product operations
   - Built-in error handling and logging

4. **Test Fixtures** (`fixtures/api_fixtures.py`)
   - API context fixture
   - Logging configuration
   - Test data fixtures

5. **Utilities** (`utils/helpers.py`)
   - ResponseValidator for API response validation
   - TestDataBuilder for creating test payloads
   - Custom Logger for better logging

6. **Example Tests** (`tests/test_example.py`)
   - Login test example
   - Get orders test example
   - Response validation example
   - Test data builder example

### 🚀 Quick Start

#### 1. Install Dependencies
```bash
pip install -r requirements.txt
pip install pytest-asyncio python-dotenv
```

#### 2. Setup Environment
```bash
cp Api_automation/.env.example Api_automation/.env
```

Edit `.env` with your API credentials:
```env
API_BASE_URL=https://your-api-url.com
TEST_EMAIL=your-email@example.com
TEST_PASSWORD=your-password
```

#### 3. Run Tests
```bash
# Run all tests
pytest Api_automation/

# Run with verbose output
pytest Api_automation/ -v

# Run specific marker
pytest Api_automation/ -m smoke

# Generate HTML report
pytest Api_automation/ --html=reports/report.html --self-contained-html
```

### 📝 Example Test Usage

```python
import pytest
from Api_automation.services.api_client import AuthService

@pytest.mark.asyncio
@pytest.mark.smoke
async def test_login(api_context, test_data):
    auth_service = AuthService(api_context)
    
    credentials = test_data["valid_credentials"]
    response = await auth_service.login(
        credentials["email"],
        credentials["password"]
    )
    
    assert response.token is not None
```

### 🧩 Available Test Markers

- `@pytest.mark.smoke` - Smoke tests (quick validation)
- `@pytest.mark.regression` - Regression tests
- `@pytest.mark.integration` - Integration tests

### 🛠️ Creating New API Services

1. Create service class in `services/api_client.py`:
```python
class YourService(APIClient):
    async def your_method(self):
        response = await self.get("/your/endpoint")
        return response
```

2. Create models in `models/api_models.py`

3. Write tests in `tests/`

### 📚 Important Files

- **conftest.py** - Main pytest configuration and shared fixtures
- **.env.example** - Copy this to `.env` and fill in your values
- **README.md** - Full documentation with examples
- **pytest.ini** - Pytest settings and test discovery rules

### ✨ Framework Advantages

✅ **Organized Structure** - Clear separation of concerns
✅ **Reusable Services** - DRY principle with service classes
✅ **Type Safety** - Data models with type hints
✅ **Easy Configuration** - Centralized settings
✅ **Fixtures** - Shared test setup and teardown
✅ **Logging** - Built-in logging to files and console
✅ **Scalable** - Easy to add new tests and services
✅ **Best Practices** - Follows pytest and automation testing best practices

### 🎓 Next Steps

1. Review `Api_automation/README.md` for detailed documentation
2. Look at example tests in `Api_automation/tests/test_example.py`
3. Modify `Api_automation/config/settings.py` with your API endpoints
4. Create `.env` file with your test credentials
5. Run example tests to validate setup
6. Start writing your test cases!

---

**Happy Testing! 🎉**
