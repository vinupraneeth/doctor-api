# Doctor Management API (FastAPI + MySQL)

## Overview
This project is a RESTful API built using FastAPI to manage doctor records.  
It supports full CRUD operations with proper validation and clean architecture.

---

## Tech Stack
- FastAPI
- SQLAlchemy
- Pydantic
- MySQL
- Uvicorn

---

## Project Structure
```
app/
├── core/           # Database connection  
├── models/         # SQLAlchemy models  
├── schemas/        # Pydantic schemas  
├── routers/        # API endpoints  
├── services/       # Business logic  
├── main.py         # Entry point  
```
---

## Features

- Create doctor
- Get all doctors
- Get doctor by ID
- Update doctor
- Delete doctor

---

## Validation Rules

- Email must be unique  
- Name, specialization, phone are required  
- Experience must be >= 0  

---

## Setup Instructions

1. Clone the repository:
```
   git clone https://github.com/vinupraneeth/doctor-api.git
   cd doctor_api
```

2. Create virtual environment:
```
   python -m venv venv
   venv\Scripts\activate
```

3. Install dependencies:
```
   pip install -r requirements.txt
```

4. Configure database:

Create `.env` file and add:
```
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=doctor_db
```
---


## Run the Application
```
python -m uvicorn app.main:app --reload
```
---


## API Documentation (Swagger)
```
http://127.0.0.1:8000/docs
```
---


## API Endpoints

- POST   /doctors        → Create doctor  
- GET    /doctors        → Get all doctors  
- GET    /doctors/{id}   → Get doctor by ID  
- PUT    /doctors/{id}   → Update doctor  
- DELETE /doctors/{id}   → Delete doctor  

---

## Database

Table: doctors

Fields:
- id (Primary Key)
- name
- email (unique)
- specialization
- phone
- experience
- is_active
- created_at

