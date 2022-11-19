from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .schemas import *
#from .routers import post, user, auth, vote

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

get_db()

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

@app.get('/database')
async def database(db: Session = Depends(get_db)):
    return {"S": "success"}


@app.get('/attendance')
async def attendings(db: Session = Depends(get_db)):
    results = db.query(models.Attendance).all()
    return {"Data": results}


@app.get('/employees')
async def employees(db: Session = Depends(get_db)):
    results = db.query(models.Employees).all()
    return {"Data": results}

@app.post('/addemplyoee', status_code=status.HTTP_201_CREATED)
async def addemplyoee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = models.Employees(**employee.dict())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return {"Data": new_employee}

@app.post('/addattendance/{id}', status_code=status.HTTP_201_CREATED)
async def add_attendance(id: int, info: AttendanceCreate, db: Session = Depends(get_db)):
    new_attendance = models.Attendance(**info.dict(), employee_id=id)
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return {"Data": info}


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
