from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from .. import models, schemas


def create_company(
        db: Session,
        admin_id: int,
        company: schemas.CompanyIn
):
        db_company = models.Company(
                name=company.name,
                description=company.description,
                admin_id=admin_id
        )
        db.add(db_company)
        db.commit()
        db.refresh(db_company)
        return db_company


def get_company(
        db: Session,
        admin_id
):
        return db.query(models.Company).filter(models.Company.admin_id == admin_id).one()


def get_all_companies(db: Session):
        return db.query(models.Company).all()

def edit_info(
        db: Session,
        admin_id: int,
        company: schemas.CompanyIn
):
        db_company = db.query(models.Company).filter(models.Company.admin_id == admin_id).one()
        db_company.name = company.name
        db_company.description = company.description
        db.commit()
        db.refresh(db_company)
        return db_company