from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from .. import models, schemas


def lookup_service_by_name(db: Session, title: str):
    return db.query(models.Service).filter(
        models.Service.title == title
    ).first()


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


def get_services(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Service).offset(skip).limit(limit).all()


def get_services_by_id(db: Session, service_id: int):
    return db.query(models.Service).filter(models.Service.id == service_id).first()


def delete_service(
        db: Session,
        service_id: int
):
    try:
        service = db.query(models.Service).filter(models.Service.id == service_id).one()
        db.delete(service)
        db.commit()
        return{"detail": "Service successfully deleted"}
    except NoResultFound:
        db.rollback()
        return {"detail": "Service not found"}