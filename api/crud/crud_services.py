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