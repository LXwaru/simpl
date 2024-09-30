from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException

from .. import models, schemas


def get_employee_by_email(db: Session, email: str):
    return db.query(models.Employee).filter(models.Employee.email == email).first()


def create_employee(
        db: Session, 
        employee: schemas.EmployeeIn,
        company_id: int
):
    db_employee = models.Employee(
        full_name=employee.full_name, 
        email=employee.email,
        company_id=company_id
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def list_employees_by_company(db: Session, company_id: int):
    return db.query(models.Employee).filter(models.Employee.company_id == company_id).all()


def get_employee_details(
    db: Session,
    company_id: int,
    employee_id: int
):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).one_or_none()
    if employee == None:
        raise HTTPException(status_code=404, detail="employee not found")
    if company_id != employee.company_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    return employee


def update_employee_info(
        db: Session,
        company_id: int,
        employee_id: int,
        employee_update: schemas.EmployeeIn
):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).one()
    if company_id != employee.company_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    employee.full_name = employee_update.full_name
    employee.email = employee_update.email
    db.commit()
    db.refresh(employee)
    return employee


def toggle_employee_active_status(
        db: Session,
        company_id: int,
        employee_id: int
):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).one()
    if company_id != employee.company_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    if employee.is_active == False:
        employee.is_active = True
    else:
        employee.is_active = False
    db.commit()
    db.refresh(employee)
    return employee


def delete_employee(
        db: Session,
        company_id: int,
        employee_id: int
):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).one()
    if company_id != employee.company_id:
        raise HTTPException(status_code=403, detail="forbidden")
    db.delete(employee)
    db.commit()
    return {'detail': "employee deleted successfully"}