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
from ..crud import crud_appointments
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()


@router.post('/api/{company_id}/appointments/', response_model=schemas.AppointmentOut)
def create_new_appointment(
    company_id: int,
    appointment: schemas.AppointmentIn,
    db: Session = Depends(utils_db.get_db),
    access_token: str = Cookie(None)
):
    appointment = crud_appointments.create_new_appointment(
        db=db, 
        appointment=appointment, 
        company_id=company_id
    )
    return appointment


@router.get('/api/{company_id}/appointments/', response_model=list[schemas.AppointmentOut])
def list_appointments(
    company_id: int,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    appointments = crud_appointments.list_appointments(
        db=db, company_id=company_id
    )
    if appointments is None:
        raise HTTPException(status_code=404, detail='no appointments found')
    return appointments


@router.get('/api/{company_id}/appointment/{appointment_id}/', response_model=schemas.AppointmentOut)
def detail_appointment(
    company_id: int,
    appointment_id: int,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    appointment = crud_appointments.get_appointment_details(
        db=db,
        company_id=company_id,
        appointment_id=appointment_id
    )
    if appointment is None:
        raise HTTPException(status_code=404, detail='appointment not found')
    return appointment


@router.put('/api/{company_id}/appointment_edit/{appointment_id}/', response_model=schemas.AppointmentOut)
def edit_entire_appointment(
    company_id: int,
    appointment_id: int,
    updated_appointment: schemas.AppointmentIn,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    appointment = crud_appointments.edit_appointment(
        db=db, 
        company_id=company_id, 
        appointment_id=appointment_id,
        updated_appointment=updated_appointment
    )
    if appointment is None:
        raise HTTPException(status_code=404, detail='appointment not found')
    return appointment


@router.put('/api/{company_id}/appointment_confirm/{appointment_id}/', response_model=schemas.AppointmentOut)
def toggle_confirm_appointment(
    company_id: int,
    appointment_id: int,
    db: Session = Depends(utils_db.get_db),
    access_token: str = Cookie(None)
):
    appointment = crud_appointments.toggle_confirm_appointment(
        db=db,
        company_id=company_id,
        appointment_id=appointment_id
    )
    if appointment is None:
        raise HTTPException(status_code=404, detail='appointment not found')
    return appointment


@router.put('/api/{company_id}/apply_credit/{appointment_id}/{credit_id}/', response_model=schemas.AppointmentOut)
def apply_credit(
    company_id: int,
    appointment_id: int,
    credit_id: int,
    db: Session = Depends(utils_db.get_db),
    access_token: str = Cookie(None)
):
    appointment = crud_appointments.apply_credit(db=db, company_id=company_id, appointment_id=appointment_id, credit_id=credit_id)
    return appointment


@router.put('/api/{company_id}/appointment_checkout/{appointment_id}/', response_model=schemas.AppointmentOut)
def checkout_appointment(
    company_id: int,
    appointment_id: int,
    db: Session = Depends(utils_db.get_db),
    access_token: str = Cookie(None)
):
    appointment = crud_appointments.checkout_appointment(
        db=db,
        company_id=company_id,
        appointment_id=appointment_id
    )
    if appointment is None:
        raise HTTPException(status_code=404, detail='appointment not found')
    return appointment


    


@router.delete('/api/{company_id}/appointment/{appointment_id}/')
def delete_appointment(
    company_id: int,
    appointment_id: int,
    db: Session = Depends(utils_db.get_db),
    access_token: str = Cookie(None)
):
    appointment = crud_appointments.delete_appointment(
        db=db, 
        company_id=company_id, 
        appointment_id=appointment_id
    )
    if appointment is None:
        raise HTTPException(status_code=404, detail='appointment not found')
    
    return appointment