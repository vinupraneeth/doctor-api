from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from app.core.database import Base

# mapping python classes to MySQL table columns
class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    specialization = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    experience = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP)