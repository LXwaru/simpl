from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

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