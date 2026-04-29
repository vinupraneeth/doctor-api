from fastapi import FastAPI
from app.core.database import engine, Base
import app.models.doctors
from app.routers import doctor_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(doctor_router.router)

@app.get("/")
def root():
    return {"message": "API is working"}