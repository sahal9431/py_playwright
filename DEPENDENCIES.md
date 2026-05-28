# Project Dependencies Documentation

## Overview
This document provides a comprehensive list of all libraries and plugins used in the Playwright Test Automation project, including their versions, purposes, and usage.

---

## Core Dependencies

### 1. **pytest** (v8.3.5)
- **Purpose**: Main testing framework for running automated tests
- **Usage**: Test discovery, execution, and reporting
- **Website**: https://pytest.org
- **Key Features**:
  - Fixture-based testing
  - Parametrized tests
  - Plugin architecture
  - Detailed test reporting

### 2. **pytest-bdd** (v8.1.0)
- **Purpose**: BDD (Behavior-Driven Development) support for pytest
- **Usage**: Writing tests in Gherkin syntax (.feature files)
- **Website**: https://pytest-bdd.readthedocs.io
- **Files**: `tests/features/*.feature`, `tests/step_defs/*.py`
- **Key Features**:
  - Gherkin language support
  - Scenario and step definitions
  - Scenario parametrization

### 3. **playwright** (v1.48.0)
- **Purpose**: Cross-browser automation library
- **Usage**: Browser control, element interaction, page navigation
- **Website**: https://playwright.dev
- **Supported Browsers**: Chromium, Firefox, WebKit
- **Key Features**:
  - Synchronous and asynchronous APIs
  - Network interception
  - Screenshot and video recording
  - Session storage management

### 4. **pytest-playwright** (v0.7.2)
- **Purpose**: Pytest plugin for Playwright integration
- **Usage**: Provides `playwright` fixture for accessing Playwright API
- **Website**: https://github.com/pytest-dev/pytest-playwright
- **Key Features**:
  - Automatic browser lifecycle management
  - Page fixtures
  - Tracing and debugging

---

## Reporting & Logging

### 5. **pytest-html** (v4.2.0)
- **Purpose**: Generate interactive HTML test reports
- **Usage**: Post-execution report generation
- **Website**: https://pytest-html.readthedocs.io
- **Output**: `reports/report.html`
- **Key Features**:
  - Rich HTML reports
  - Self-contained reports
  - Detailed test information
  - Screenshot embedding

### 6. **pytest-metadata** (v3.1.1)
- **Purpose**: Collect and display test metadata
- **Usage**: Environment, platform, and execution information in reports
- **Website**: https://github.com/pytest-dev/pytest-metadata
- **Key Features**:
  - System information capture
  - Custom metadata
  - Report headers

---

## Testing Utilities

### 7. **pytest-xdist** (v3.8.0)
- **Purpose**: Parallel test execution
- **Usage**: Run multiple tests simultaneously
- **Website**: https://pytest-xdist.readthedocs.io
- **Command**: `pytest -n auto tests/`
- **Key Features**:
  - Parallel execution
  - Distributed testing
  - Load balancing
  - `-n` flag for parallelization

### 8. **pytest-base-url** (v2.1.0)
- **Purpose**: Manage base URLs for tests
- **Usage**: Store application URLs for testing
- **Website**: https://github.com/pytest-dev/pytest-base-url
- **Configuration**: Set via `--base-url` option or fixture
- **Key Features**:
  - URL management
  - Base URL fixture
  - Environment-specific URLs

---

## Auto-Installed Dependencies

The following libraries are automatically installed when installing the above packages:

### Supporting Libraries
- **packaging** (>=20.0) - Version handling and comparison
- **pluggy** (>=1.5.0) - Plugin system for pytest
- **tomli** (>=1.0.0) - TOML file parsing for configs
- **attrs** (>=19.3.0) - Class creation utilities
- **greenlet** (>=1.1.2) - Lightweight concurrency for async operations
- **anyio** (>=4.0) - Async compatibility layer

---

## Python Standard Library (No Installation Required)

These are built-in Python modules used throughout the project:

### Module: **os** (pathlib alternative)
- File and OS operations
- Environment variables

### Module: **pathlib** (Modern path handling)
- Cross-platform path handling
- File/directory operations
- Used in: `conftest.py`, page objects

```python
from pathlib import Path
logs_dir = Path.cwd() / "logs"
```

### Module: **datetime**
- Timestamp generation
- Date/time manipulation
- Used in: Screenshot naming, logging

```python
from datetime import datetime
ts = datetime.now().strftime("%Y%m%d-%H%M%S")
```

### Module: **time**
- Sleep/delay operations
- Used in: Test waits, timing

### Module: **random**
- Random data generation
- Used in: `registration_page.py` for unique email/phone generation

```python
random.randint(100, 999)
random.randint(6000000000, 9999999999)
```

### Module: **typing**
- Type hints
- Used in: `base_page.py` for function signatures

```python
from typing import List, Optional
```

---

## Version Matrix

| Library | Version | Purpose | Status |
|---------|---------|---------|--------|
| pytest | 8.3.5 | Testing Framework | ✅ Active |
| pytest-bdd | 8.1.0 | BDD Support | ✅ Active |
| playwright | 1.48.0 | Browser Automation | ✅ Active |
| pytest-playwright | 0.7.2 | Pytest Integration | ✅ Active |
| pytest-html | 4.2.0 | HTML Reports | ✅ Active |
| pytest-metadata | 3.1.1 | Test Metadata | ✅ Active |
| pytest-xdist | 3.8.0 | Parallel Execution | ✅ Active |
| pytest-base-url | 2.1.0 | URL Management | ✅ Active |

---

## Installation

### Basic Installation
```bash
# Install all dependencies from requirements.txt
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### Installation by Category

**Minimal (Core only):**
```bash
pip install pytest playwright pytest-bdd
```

**Standard (With reporting):**
```bash
pip install -r requirements.txt
```

**Advanced (With optional tools):**
```bash
pip install -r requirements.txt
pip install pytest-cov pytest-benchmark
```

---

## Optional Dependencies (Not Included)

For additional capabilities, consider installing:

### For Code Coverage
```bash
pip install pytest-cov
pytest --cov=pages --cov-report=html
```

### For Performance Testing
```bash
pip install pytest-benchmark
```

### For API Testing
```bash
pip install requests requests-mock
```

### For Debugging
```bash
pip install pytest-debug-on-error
```

### For Allure Reports
```bash
pip install allure-pytest
```

---

## Project Structure & Dependencies

```
Playwright_Project/
├── conftest.py              # Uses: pytest, playwright, pathlib, datetime
├── pytest.ini               # Pytest configuration
├── requirements.txt         # This file
│
├── pages/                   # Page Objects
│   ├── base_page.py         # Uses: playwright, typing, List, Optional
│   ├── login_page.py        # Uses: BasePage (custom)
│   ├── home_page.py         # Uses: BasePage
│   ├── cart_page.py         # Uses: BasePage
│   └── registration_page.py # Uses: BasePage, time, random
│
├── tests/
│   ├── features/            # Feature files (Gherkin syntax)
│   │   ├── login_logout.feature
│   │   ├── cart.feature
│   │   ├── product_search.feature
│   │   └── register.feature
│   │
│   └── step_defs/           # Step definitions
│       ├── test_login_steps.py      # Uses: pytest-bdd, pages
│       ├── test_cart_steps.py       # Uses: pytest-bdd, pages
│       ├── test_product_search_steps.py  # Uses: pytest-bdd, pages
│       └── test_register_steps.py   # Uses: pytest-bdd, pages
│
├── Api_automation/          # API Tests
│   ├── test_network.py      # Uses: playwright, Page
│   ├── test_network_mock_response.py
│   ├── test_network_session_storage.py
│   ├── test_web_api.py      # Uses: playwright, expect, APIUtils
│   └── utils/
│       └── apiBase.py       # Uses: playwright.Playwright
│
├── reports/                 # Generated Reports
│   ├── junit.xml           # JUnit format (pytest-generated)
│   └── report.html         # HTML report (pytest-html)
│
└── logs/                    # Log files
    └── pytest.log          # Detailed logs
```

---

## Quick Commands

### Running Tests
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/step_defs/test_login_steps.py

# Run tests matching pattern
pytest -k "login" tests/

# Run in parallel (requires pytest-xdist)
pytest -n auto tests/

# Run with HTML report
pytest --html=report.html --self-contained-html
```

### Generating Reports
```bash
# Generate JUnit XML (for CI/CD)
pytest --junit-xml=reports/junit.xml

# Generate HTML report
pytest --html=reports/report.html --self-contained-html

# Generate with screenshots and videos
playwright install chromium
pytest --screenshot=only-on-failure --video=retain-on-failure
```

### Debugging
```bash
# Show print statements and logs
pytest -s

# Show local variables on failure
pytest -l

# Stop on first failure
pytest -x

# Show top 10 slowest tests
pytest --durations=10
```

---

## Compatibility

- **Python**: 3.8+
- **OS**: Windows, macOS, Linux
- **Browsers**: Chromium, Firefox, WebKit (via Playwright)
- **CI/CD**: Jenkins, GitHub Actions, GitLab CI, Azure Pipelines

---

## Troubleshooting

### Issue: Playwright not found
```bash
# Install browsers for Playwright
playwright install

# Or install specific browser
playwright install chromium
```

### Issue: pytest not recognized
```bash
# Reinstall pytest and plugins
pip install --upgrade -r requirements.txt
```

### Issue: Tests not discovering
```bash
# Check pytest configuration
pytest --collect-only

# Verify PYTHONPATH
echo $PYTHONPATH
```

---

## Update & Maintenance

### Check for updates
```bash
pip list --outdated
```

### Update all packages
```bash
pip install --upgrade -r requirements.txt
```

### Generate updated requirements
```bash
pip freeze > requirements-frozen.txt
```

---

## Support & Resources

- **Pytest Documentation**: https://docs.pytest.org
- **Playwright Documentation**: https://playwright.dev
- **pytest-bdd Documentation**: https://pytest-bdd.readthedocs.io
- **GitHub Issues**: Check individual project repositories

---

**Last Updated**: May 23, 2026
**Project**: Playwright Test Automation (py_playwright)
**Repository**: https://github.com/sahal9431/py_playwright
