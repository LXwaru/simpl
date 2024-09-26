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
    db_appointment = models.Appointment(
        client_id=appointment.client_id,
        employee_id=appointment.employee_id,
        service_id=appointment.service_id,
        start_time=appointment.start_time,
        company_id=company_id,
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment