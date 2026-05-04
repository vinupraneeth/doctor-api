from app.repositories import doctor_repository
from sqlalchemy.orm import Session
from app.repositories import doctor_repository


def get_all_doctors(db: Session):
    return doctor_repository.get_all_doctors(db)


def get_doctor_by_id(db: Session, doctor_id: int):
    return doctor_repository.get_doctor_by_id(db, doctor_id)


def create_doctor(db: Session, data):
    return doctor_repository.create_doctor(db, data)


def update_doctor(db: Session, doctor, data):
    return doctor_repository.update_doctor(db, doctor, data)


def delete_doctor(db: Session, doctor):
    return doctor_repository.delete_doctor(db, doctor)


def get_doctor_by_email(db: Session, email: str):
    return doctor_repository.get_doctor_by_email(db, email)