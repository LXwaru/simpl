from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from .. import schemas, utils_db
from ..crud import crud_appointments
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/api/{company_id}/appointments/')
def create_new_appointment(
    company_id: int,
    appointment: schemas.AppointmentIn,
    db: Session = Depends(utils_db.get_db)
):
    appointment = crud_appointments.create_new_appointment(db=db, appointment=appointment, company_id=company_id)
    return appointment


@router.get('/api/{company_id}/appointments/')
def list_appointments():
    pass


@router.get('/api/{company_id}/appointment/{appointment_id}')
def detail_appointment():
    pass


@router.put('/api/{company_id}/appointment/{appointment_id}')
def edit_appointment():
    pass


@router.delete('/api/{company_id}/appointment/{appointment_id}')
def delete_appointment():
    pass