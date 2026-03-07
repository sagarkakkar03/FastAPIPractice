from fastapi import FastAPI, HTTPException
from models import Employee
from typing import List

employees_db: List[Employee] = []

app = FastAPI()

@app.get('/employees', response_model=List[Employee])
def get_employee():
    return employees_db

@app.get('/employees/{emp_id}', response_model=Employee)
def get_employee_by_id(emp_id:int):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            return employees_db[index]
    raise HTTPException(status_code=404, detail='Employee Not Found')

@app.post('/add_employee', response_model=Employee)
def add_employee(new_emp: Employee):
    for employee in employees_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee already in the database")
    employees_db.append(new_emp)
    return new_emp

@app.put('/update_employee/{emp_id}', response_model=Employee)
def update_employee(emp_id:str, updated_emp: Employee):
    for index, employee in enumerate(employees_db):
        if emp_id == employee.id:
            employees_db[index] = updated_emp
            return updated_emp
    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete('/delete_employee/{emp_id}')
def delete_employee(emp_id:str):
    for index, employee in enumerate(employees_db):
        if emp_id == employee.id:
            del employees_db[index]
            return {'message': 'Employee deleted successfully'}
    raise HTTPException(status_code=404, detail="Employee not found")