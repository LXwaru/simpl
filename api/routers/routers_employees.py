from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from .. import schemas, utils_db
from ..crud import crud_employees
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/api/{company_id}/employees/", response_model=schemas.EmployeeOut)
def create_employee(
    company_id: int,
    employee: schemas.EmployeeIn,
    db: Session = Depends(utils_db.get_db)
):
    db_employee = crud_employees.get_employee_by_email(db, email=employee.email)
    if db_employee:
        raise HTTPException(status_code=400, detail="employee email already registered")
    return crud_employees.create_employee(db=db, employee=employee, company_id=company_id)