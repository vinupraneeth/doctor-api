from sqlalchemy.orm import Session
from app.models.doctors import Doctor


def get_all_doctors(db: Session):
    return db.query(Doctor).all()


def get_doctor_by_id(db: Session, doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()


def create_doctor(db: Session, data):
    new_doctor = Doctor(**data.dict())
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor


def update_doctor(db: Session, doctor, data):
    for key, value in data.dict().items():
        setattr(doctor, key, value)

    db.commit()
    db.refresh(doctor)
    return doctor


def delete_doctor(db: Session, doctor):
    db.delete(doctor)
    db.commit()