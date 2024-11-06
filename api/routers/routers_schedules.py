from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
    Cookie
)
from .. import schemas, utils_db, utils_sec
from ..crud import crud_employees
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()


@router.post("/api/{company_id}/{employee_id}/schedules/", response_model=schemas.ScheduleOut)
def add_schedule():
    pass


@router.get("/api/{company_id}/{employee_id}/schedules/", response_model=schemas.ScheduleOut)
def list_schedule():
    pass


@router.get("/api/{company_id}/{employee_id}/schedule/{schedule_id}/", response_model=schemas.ScheduleOut)
def get_schedule_detail():
    pass


@router.put("/api/{company_id}/{employee_id}/update_schedule/{schedule_id}/", response_model=schemas.ScheduleOut)
def update_schedule():
    pass


@router.put("/api/{company_id}/{employee_id}/reservation/{schedule_id}/", response_model=schemas.ScheduleOut)
def toggle_reserve():
    pass


@router.delete("/api/{company_id}/{employee_id}/schedule/{schedule_id}/")
def delete_schedule():
    pass