from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from . import schemas, crud_employees, utils_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/api/employees/", response_model=schemas.EmployeeOut)
def create_employee(
    employee: schemas.EmployeeIn,
    db: Session = Depends(utils_db.get_db)
):
    db_employee = crud_employees.get_employee_by_name_and_company(db, full_name=employee.full_name, company_id=employee.company_id)
    if db_employee:
        raise HTTPException(status_code=400, detail="employee name already registered")
    return crud_employees.create_employee(db=db, employee=employee)