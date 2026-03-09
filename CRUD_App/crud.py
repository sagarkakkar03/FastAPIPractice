from sqlalchemy.orm import Session
import models, schema

def get_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee(db: Session, emp_id):
    return (
        db
        .query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )

def create_employee(db: Session, employee: schema.EmployeeCreate):
    db_empoyee = models.Employee (
            name=employee.name, 
            email=employee.email
            )
    db.add(db_empoyee)
    db.commit()
    db.refresh(db_empoyee)    
    return db_empoyee

def update_employee(db: Session, emp_id: int, employee: schema.EmployeeUpdate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db_employee.name = employee.name 
        db_employee.email = employee.email 
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, emp_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    
    if db_employee:
        db.delete(db.employee)
        db.commit()
        
    return db_employee