from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class DoctorBase(BaseModel):
    name: str
    email: EmailStr
    specialization: str
    phone: str
    experience: int = Field(..., ge=0)
    is_active: Optional[bool] = True


class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True