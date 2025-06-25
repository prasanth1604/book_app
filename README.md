# 📚 FastAPI Book API with JWT Authentication

This is a simple FastAPI-based backend application that allows users to:

- ✅ Create a book
- 🔍 View all books or filter by author/publisher
- ❌ Delete a book by ID

All APIs are protected via **JWT-based authentication**.

---

## 🚀 Features

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- JWT Authentication with expiry validation
- SQLite database via SQLAlchemy ORM
- Clean and modular codebase

---

## 🏗 Tech Stack

- **FastAPI** - Web framework
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Lightweight DB for local development
- **JWT** - Authentication using JSON Web Tokens
- **Pydantic** - Data validation

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-book-api.git
cd fastapi-book-api
```

### 2. Create and Activate Virtual Environment
```
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run the Server
```
uvicorn main:app --reload
```
The API will be available at:
📍 http://127.0.0.1:8000


### 5. API Endpoints
🔸 Create a Book
POST /books/
Request Body:
```
{
  "name": "Atomic Habits",
  "description": "A book on habits",
  "pages": 300,
  "author": "James Clear",
  "publisher": "Penguin"
}
```
🔸 Get All Books (Optional Filters)
GET /books/
Supports query params:

author

publisher

Example:
```
GET /books/?author=James%20Clear
```
Delete a Book
```
DELETE /books/{book_id}
```
