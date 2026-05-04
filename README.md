# Doctor Management API (FastAPI + MySQL)

## Overview

This project is a RESTful API built using FastAPI to manage doctor records.
It supports full CRUD operations with validation and a clean architecture structure.

---

## Tech Stack

* FastAPI
* SQLAlchemy
* Pydantic
* MySQL
* Uvicorn

---

## Project Structure

```bash
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

* Create doctor
* Get all doctors
* Get doctor by ID
* Update doctor
* Delete doctor

---

## Validation Rules

* Email must be unique
* Name, specialization, phone are required
* Experience must be >= 0

---

## Prerequisites

Make sure the following are installed:

* Python (3.8 or above)
* MySQL Server
* Git
* pip

Downloads:

* Python: https://www.python.org/downloads/
* MySQL: https://dev.mysql.com/downloads/
* Git: https://git-scm.com/downloads

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/vinupraneeth/doctor-api.git
cd doctor_api
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure database

Create a `.env` file and add:

```bash
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=doctor_db
```

---

## Database Setup

Run the following in MySQL:

```sql
CREATE DATABASE doctor_db;
```

---

## Run the Application

```bash
python -m uvicorn app.main:app --reload
```

---

## API Documentation (Swagger)

```bash
http://127.0.0.1:8000/docs
```

---

## API Endpoints

* POST   /doctors        → Create doctor
* GET    /doctors        → Get all doctors
* GET    /doctors/{id}   → Get doctor by ID
* PUT    /doctors/{id}   → Update doctor
* DELETE /doctors/{id}   → Delete doctor

---

## Database

Table: doctors

Fields:

* id (Primary Key)
* name
* email (unique)
* specialization
* phone
* experience
* is_active
* created_at
