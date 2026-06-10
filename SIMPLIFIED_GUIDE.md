# 📊 Simple Data-Driven Testing with Excel

## ✅ Your Simplified Framework

```
Your Excel File → Read Data → Feature Examples → Run Tests
   (maintain it)   (utils)     (hardcoded)      (BDD)
```

---

## 🚀 How to Use

### **1. Your Excel File**
- **Location**: `data/test_data.xlsx`
- **You manage it**: Open in Excel, add/edit rows as needed
- **Sheets**: RegistrationData, LoginData, SearchData, Config

### **2. Feature Files** (Already set up)
```gherkin
Scenario Outline: User registers
    When user enters "<firstName>" as first name
    And user enters "<email>" as email
    ...

Examples: Valid registration data
    | firstName | email          |
    | John      | john@ex.com    |
    | Jane      | jane@ex.com    |
```

### **3. Run Tests**
```bash
pytest tests/step_defs/test_register_steps.py -v
# 4 tests run (one per row in Examples)
```

---

## 📝 Add More Test Data

### Option 1: Edit Feature File (Simplest)
1. Open `tests/features/register.feature`
2. Add new row to Examples
3. Run tests - new scenario runs automatically

### Option 2: Keep Data in Excel
- Edit `data/test_data.xlsx` in Excel
- Copy-paste Examples to feature file from there
- Use our utilities to read Excel when needed

---

## 🔧 Code to Read Excel (When Needed)

```python
from utils.excel_reader import ExcelDataReader

# Read Excel
reader = ExcelDataReader("data/test_data.xlsx")
data = reader.get_sheet_data("RegistrationData")

# Now use data
for row in data:
    print(row)
    # Output: {'firstName': 'John', 'email': 'john@ex.com', ...}

reader.close()
```

---

## ✅ What You Have Now

- ✅ Feature files with Examples (register, login)
- ✅ Step definitions that accept parameters
- ✅ Excel file for data (you maintain it)
- ✅ Utilities to read Excel if needed
- ✅ Config from Excel for URLs

**No code to generate Excel needed!**

---

## 📂 File Structure (Simplified)

```
tests/
├── features/
│   ├── register.feature              ← Examples with data
│   └── login_logout.feature          ← Examples with data
├── step_defs/
│   ├── test_register_steps.py        ← Parameterized steps
│   └── test_login_steps.py           ← Parameterized steps

utils/
├── excel_reader.py                   ← Read Excel
├── config.py                         ← Load config

data/
└── test_data.xlsx                    ← Your test data (you manage)

(No create_test_data.py needed!)
```

---

## 💡 Three Ways to Use Excel

### **1. Examples in Feature File** (Current - Recommended)
```gherkin
Examples:
    | firstName | email       |
    | John      | john@ex.com |
```
✅ Simple, easy to read, no code needed

### **2. Python - Read from Excel**
```python
reader = ExcelDataReader("data/test_data.xlsx")
data = reader.get_sheet_data("RegistrationData")
```
✅ When you need to access data in code

### **3. Config from Excel**
```python
from utils.config import Config
url = Config.get_base_url()  # From Excel
```
✅ For configuration values

---

## ✨ Summary

**Before**: Complex setup with code to generate Excel  
**After**: Simple approach - you manage Excel, we read it  

**Just**:
1. Edit `data/test_data.xlsx` in Excel
2. Copy data to Examples in feature files (or keep separate)
3. Run `pytest tests/step_defs/ -v`
4. Done! ✅

**Status**: Simplified and ready! 🚀
