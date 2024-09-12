from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from . import models, schemas


def get_employee_by_name_and_company(db: Session, full_name: str, company_id: int):
    return db.query(models.Employee).filter(models.Employee.full_name == full_name and models.Employee.company_id == company_id).first()


def create_employee(db: Session, employee: schemas.EmployeeIn):
    db_employee = models.Employee(full_name=employee.full_name, company_id=employee.company_id)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee