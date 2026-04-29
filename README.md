Doctor API (FastAPI + MySQL)

Features
- CRUD operations for doctors
- Email uniqueness validation
- Input validation using Pydantic
- MySQL database integration

Tech Stack
- FastAPI
- SQLAlchemy
- Pydantic
- MySQL

Run Project
1. Install dependencies:
   pip install -r requirements.txt

2. Run server:
   python -m uvicorn app.main:app --reload

3. Open Swagger:
   http://127.0.0.1:8000/docs