from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from . import models, schemas


def create_company(
        db: Session,
        company: schemas.CompanyIn
):
    db_company = models.Company(**company.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def list_companies(
        db: Session
):
    return db.query(models.Company).all()