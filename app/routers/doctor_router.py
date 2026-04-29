from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.schemas.doctor_schema import DoctorResponse, DoctorCreate
from app.services import doctor_service
from app.models.doctors import Doctor

router = APIRouter(prefix="/doctors", tags=["Doctors"])


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET all doctors
@router.get("/", response_model=List[DoctorResponse])
def get_doctors(db: Session = Depends(get_db)):
    return doctor_service.get_all_doctors(db)


# CREATE doctor
@router.post("/", response_model=DoctorResponse)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):

    # Email uniqueness check
    existing = db.query(Doctor).filter(Doctor.email == doctor.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    return doctor_service.create_doctor(db, doctor)


# GET doctor by ID
@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = doctor_service.get_doctor_by_id(db, doctor_id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor


# UPDATE doctor
@router.put("/{doctor_id}", response_model=DoctorResponse)
def update_doctor(doctor_id: int, updated: DoctorCreate, db: Session = Depends(get_db)):
    doctor = doctor_service.get_doctor_by_id(db, doctor_id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    # Prevent duplicate email
    existing = db.query(Doctor).filter(
        Doctor.email == updated.email,
        Doctor.id != doctor_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    return doctor_service.update_doctor(db, doctor, updated)


# DELETE doctor
@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = doctor_service.get_doctor_by_id(db, doctor_id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    doctor_service.delete_doctor(db, doctor)

    return {"message": "Doctor deleted"}