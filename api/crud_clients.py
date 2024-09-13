from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from . import models, schemas


def get_client_by_email(db: Session, email: str):
    return db.query(models.Client).filter(models.Client.email == email).first()


def create_client(
    db: Session, 
    client: schemas.ClientIn,
    company_id: int
):
    db_client = models.Client(
        full_name=client.full_name, 
        email=client.email,
        company_id=company_id)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client