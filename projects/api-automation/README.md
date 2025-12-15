# API Automation Testing (Python)

## 📌 Project Overview
This project demonstrates API automation testing using **Python**, **Pytest**, and **Flask**.  
It covers real-world API testing scenarios including:

- REST API testing (GET, POST, DELETE)
- Working with public APIs (NASA API)
- Testing custom Flask applications
- Request validation and response assertions
- Test structure and reusability

The project is organized as a production-like automation framework.

---

## 🧪 Technologies Used
- Python 3
- Pytest
- Requests
- Flask
- REST API
- JSON
- Git

---

## 📂 Project Structure

projects/api-automation/
├── app.py                   # Flask CRUD API (demo app)
├── cars_app.py              # Cars search API app
├── clients/
│   └── nasa_client.py       # Client for NASA Mars Rover API
├── tests/
│   ├── conftest.py          # Pytest fixtures
│   ├── test_nasa_api.py     # Tests for NASA public API
│   ├── test_crud_api.py     # Tests for CRUD endpoints
│   ├── test_flask_crud_api.py # CRUD tests (renamed from test_app.py)
│   └── test_cars_search.py  # Tests for Cars search API
├── requirements.txt
└── README.md



---

## 🔍 Tested APIs

### 1️⃣ NASA Mars Rover Photos API
- Sends GET requests to the public NASA API
- Validates response status codes
- Checks response structure and required fields
- Demonstrates work with external APIs

### 2️⃣ Flask CRUD API
- Custom Flask application
- Covers:
  - POST (create resource)
  - GET (retrieve resource)
  - DELETE (remove resource)
- Validates request/response data and HTTP status codes

### 3️⃣ Cars Search API
- API with query parameters
- Authorization handling
- Data-driven tests
- Validation of filtered results

---

## ▶️ How to Run the Tests

### 1️⃣ Create virtual environment

python -m venv venv
source venv/bin/activate  # macOS / Linux
# venv\Scripts\activate   # Windows

### 2️⃣ Install dependencies

pip install -r requirements.txt
### 3️⃣ Run tests

pytest