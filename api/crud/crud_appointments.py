from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException
from datetime import datetime, timezone

from .. import models, schemas


def create_new_appointment(
        company_id: int,
        appointment: schemas.AppointmentIn,
        db: Session
):
    # credit = db.query(models.Credit).filter(
    #     models.Credit.id == appointment.credit_id
    # ).one_or_none()
    
    db_appointment = models.Appointment(
        client_id=appointment.client_id,
        employee_id=appointment.employee_id,
        service_id=appointment.service_id,
        # credit_id=appointment.credit_id,
        start_time=appointment.start_time,
        company_id=company_id,
        # credit=credit
    )
    client = db.query(models.Client).filter(
        models.Client.id == appointment.client_id
    ).one_or_none()
    if client is None:
        raise HTTPException(status_code=404, detail='client not found')


    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def list_appointments(
        company_id: int,
        db: Session
):
    appointments = db.query(models.Appointment).filter(
        models.Appointment.company_id == company_id
    ).all() 
    if len(appointments) == 0:
        return None
    return appointments


def get_appointment_details(
        company_id: int,
        appointment_id: int,
        db: Session
):
    appointment = db.query(models.Appointment).filter(
        models.Appointment.company_id == company_id,
        models.Appointment.id == appointment_id
    ).one_or_none()

    if appointment is None:
        return None
    
    return appointment


def edit_appointment(
        company_id: int,
        appointment_id: int,
        updated_appointment: schemas.AppointmentIn,
        db: Session
):
    appointment = db.query(models.Appointment).filter(
        models.Appointment.company_id == company_id,
        models.Appointment.id == appointment_id
    ).one_or_none()
    if appointment is None:
        return None
    appointment.client_id = updated_appointment.client_id
    appointment.service_id = updated_appointment.service_id
    appointment.employee_id = updated_appointment.employee_id
    appointment.start_time = updated_appointment.start_time

    db.commit()
    db.refresh(appointment)
    return appointment


def toggle_confirm_appointment(
    company_id: int,
    appointment_id: int,
    db: Session
):
    appointment = db.query(models.Appointment).filter(
    models.Appointment.company_id == company_id,
    models.Appointment.id == appointment_id
    ).one_or_none()
    if appointment is None:
        return None
    if appointment.is_confirmed == False:
        appointment.is_confirmed = True
    else:
        appointment.is_confirmed = False

    db.commit()
    db.refresh(appointment)
    return appointment


def checkout_appointment(
    company_id: int,
    appointment_id: int,
    db: Session
):
    appointment = db.query(models.Appointment).filter(
    models.Appointment.company_id == company_id,
    models.Appointment.id == appointment_id
    ).one_or_none()
    if appointment is None:
        return None
    if appointment.credit is None:
        return None
    appointment.is_complete = True

    credit = db.query(models.Credit).filter(
        models.Credit.id == appointment.credit_id
    ).one_or_none()
    if credit is None:
        raise HTTPException(status_code=401, detail='no credit on file')
    
    credit.is_redeemed = True
    credit.completed_on = datetime.now()
    
    db.commit()
    db.refresh(appointment)
    return appointment


def delete_appointment(
    company_id: int,
    appointment_id: int,
    db: Session
):
    appointment = db.query(models.Appointment).filter(
    models.Appointment.company_id == company_id,
    models.Appointment.id == appointment_id
    ).one_or_none()

    if appointment is None: 
        return None
    
    if appointment.credit is not None:
        raise HTTPException(status_code=401, detail='appointment has a credit, delete the credit first')

    db.delete(appointment)
    db.commit()
    return {'detail': 'appointment successfully deleted'}


def apply_credit(
    company_id: int,
    appointment_id: int,
    credit_id: int,
    db: Session
):
    appointment = db.query(models.Appointment).filter(
        models.Appointment.company_id == company_id,
        models.Appointment.id == appointment_id
        ).one_or_none()
    
    if appointment is None: 
        return None
    
    db_credit = db.query(models.Credit).filter(
        models.Appointment.company_id == company_id,
        models.Credit.id == credit_id).one_or_none()
    if db_credit is None:
        return None
    appointment.credit = db_credit
    db_credit.is_attached = True
    db.commit()
    db.refresh(appointment)
    return appointment

def remove_credit(
    company_id: int,
    appointment_id: int,
    credit_id: int,
    db: Session
):
    appointment = db.query(models.Appointment).filter(
        models.Appointment.company_id == company_id,
        models.Appointment.id == appointment_id
    ).one_or_none()

    if appointment is None:
        return None
    
    credit = appointment.credit

    if credit is None:
        return None
    
    credit.is_attached = False
    appointment.credit = None

    db.commit()
    db.refresh(appointment)
    return appointment


    