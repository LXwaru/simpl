from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from .. import schemas, utils_db, utils_sec
from ..crud import crud_employees
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/api/employees/{company_id}/", response_model=schemas.EmployeeOut)
def create_employee(
    company_id: int,
    employee: schemas.EmployeeIn,
    db: Session = Depends(utils_db.get_db),
    current_user: str = Depends(utils_sec.get_current_active_user)
):
    db_employee = crud_employees.get_employee_by_email(db, email=employee.email)
    if db_employee:
        raise HTTPException(status_code=400, detail="employee email already registered")
    return crud_employees.create_employee(db=db, employee=employee, company_id=company_id)


@router.get("/api/employees/{company_id}", response_model=list[schemas.EmployeeOut])
def list_employees_by_company(
    company_id: int,
    db: Session = Depends(utils_db.get_db),
    current_user: str = Depends(utils_sec.get_current_active_user)
):
    employee_list = crud_employees.list_employees_by_company(db=db, company_id=company_id)
    if employee_list is None:
        raise HTTPException(status_code=404, detail=f"company with id number {company_id} has no employees")
    return employee_list


@router.get("/api/employee/{company_id}/{employee_id}", response_model=schemas.EmployeeOut)
def get_employee_details(
    company_id: int,
    employee_id: int,
    db: Session = Depends(utils_db.get_db),
    current_user: str = Depends(utils_sec.get_current_active_user)
):
    return crud_employees.get_employee_details(
        company_id=company_id,
        employee_id=employee_id,
        db=db
    )


@router.put("/api/employee_info/{company_id}/{employee_id}/", response_model=schemas.EmployeeOut)
def update_employee_info(
    company_id: int,
    employee_id: int,
    employee_update: schemas.EmployeeIn,
    db: Session = Depends(utils_db.get_db),
    current_user: str = Depends(utils_sec.get_current_active_user)
):
    return crud_employees.update_employee_info(
        db=db, 
        company_id=company_id, 
        employee_id=employee_id, 
        employee_update=employee_update
    )


@router.put("/api/employee_status/{company_id}/{employee_id}/", response_model=schemas.EmployeeOut)
def toggle_employee_active_status(
    company_id: int,
    employee_id: int,
    db: Session = Depends(utils_db.get_db),
    current_user: str = Depends(utils_sec.get_current_active_user)
):
    return crud_employees.toggle_employee_active_status(
        db=db, 
        company_id=company_id, 
        employee_id=employee_id,
    )


@router.delete("/api/employee/{company_id}/")
def delete_employee(
    company_id: int,
    employee_id: int,
    db: Session = Depends(utils_db.get_db),
    current_user: str = Depends(utils_sec.get_current_active_user)
):
    return crud_employees.delete_employee(db=db, employee_id=employee_id, company_id=company_id)