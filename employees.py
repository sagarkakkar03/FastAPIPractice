from fastapi import FastAPI, HTTPException
from models import Employee
from typing import List

employees_db: List[Employee] = []

app = FastAPI()

#  get all employee
@app.get('/employee', response_model=List[Employee])
def get_employee():
    return employees_db

#  get specific employee

@app.post('/employee/{emp_id}', response_model=Employee)
def add_employee(emp_id):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            return employees_db[index]
    raise HTTPException(status_code=404, detail='Employee Not Found')
