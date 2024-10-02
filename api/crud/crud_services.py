from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from .. import models, schemas


def lookup_service_by_name(db: Session, title: str, company_id):
    return db.query(models.Service).filter(
        models.Service.title == title,
        models.Service.company_id == company_id
    ).one_or_none()


def register_new_service(
    db: Session,
    service: schemas.ServiceIn,
    company_id: int
):
    db_service = models.Service(
        title=service.title,
        price=service.price,
        duration=service.duration,
        description=service.description,
        is_enabled=True,
        company_id=company_id
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return(db_service)


def list_services(
    db: Session, 
    company_id: int
):
    return db.query(models.Service).filter(
        models.Service.company_id == company_id
    ).all()


def get_services_by_id(
    db: Session, 
    service_id: int, 
    company_id: int
):
    return db.query(models.Service).filter(
        models.Service.id == service_id,
        models.Service.company_id == company_id
    ).one_or_none()


def update_service(
    db: Session, 
    service_id: int,
    company_id: int,
    service_update: schemas.ServiceIn,
):
    service = db.query(models.Service).filter(
        models.Service.id == service_id,
        models.Service.company_id == company_id
    ).one_or_none()

    if service is None:
        return None
    
    service.title = service_update.title
    service.price = service_update.price
    service.duration = service_update.duration
    service.description = service_update.description

    db.commit()
    db.refresh(service)
    return service


def toggle_activation(
        db: Session,
        company_id: int,
        service_id: int
):
    service = db.query(models.Service).filter(
        models.Service.id == service_id,
        models.Service.company_id == company_id
    ).one_or_none()
    if service is None:
        return None
    if service.is_enabled == False:
        service.is_enabled = True
    else: 
        service.is_enabled = False

    db.commit()
    db.refresh(service)
    return service


def delete_service(
    db: Session,
    service_id: int,
    company_id: int
):
    try:
        service = db.query(models.Service).filter(
            models.Service.id == service_id,
            models.Service.company_id == company_id
        ).one()
        db.delete(service)
        db.commit()
        return{"detail": "Service successfully deleted"}
    except NoResultFound:
        db.rollback()
        return {"detail": "Service not found"}