from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from . import models, schemas


def create_company(
        db: Session,
        company: schemas.CompanyIn,
        admin_id: int
):
    db_company = models.Company(**company.model_dump(), admin_id=admin_id)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company