from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base 
from typing import List 
import models, schema, crud 

Base.metadata.create_all(bind=engine)

app = FastAPI()


# dependency with the DB
def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()


# endpoints
# 1. create an employee
@app.post('/create', response_model=schema.EmployeeOut)
def create_employee(employee: schema.EmployeeCreate, db: Session=Depends(get_db)):
    return crud.create_employee(db, employee)

@app.get('/employees', response_model=List[schema.EmployeeOut])
def get_employees(db: Session= Depends(get_db)):
    return crud.get_employees(db)


@app.get('/employee/{emp_id}', response_model=schema.EmployeeOut)
def get_employee_by_id(emp_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, emp_id)
    if db_employee:
        return db_employee
    raise HTTPException(status_code=404, detail="Employee not found")


@app.put("/update/{emp_id}", response_model=schema.EmployeeUpdate)
def update_employee(emp_id: int, employee: schema.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if db_employee:
        return db_employee
    raise HTTPException(status_code=404,detail="Employee not found" )

@app.delete("/delete/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    db_employee = crud.delete_employee(db, emp_id)
    if db_employee:
        return db_employee
    raise HTTPException(status_code=404, detail="Employee not found")