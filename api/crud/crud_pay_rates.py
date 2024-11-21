from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException

from .. import models, schemas

def post_pay_rate(
        db: Session,
        company_id: int,
        pay_rate: schemas.PayRateIn,
):
    db_pay_rate = models.PayRate(
        company_id = company_id,
        employee_id = pay_rate.employee_id,
        service_id = pay_rate.service_id,
        rate_per_service = pay_rate.rate_per_service
    )
    db.add(db_pay_rate)
    db.commit()
    db.refresh(db_pay_rate)
    return db_pay_rate


def get_all_pay_rates(
        db: Session,
        company_id: int
):
    pay_rates = db.query(models.PayRate).filter(models.PayRate.company_id == company_id).all()
    return pay_rates


def get_one_rate(
        db: Session,
        company_id: int,
        employee_id: int,
        service_id: int 
):
    pay_rate = db.query(models.PayRate).filter(
        models.PayRate.company_id == company_id,
        models.PayRate.employee_id == employee_id,
        models.PayRate.service_id == service_id
    ).first()
    return pay_rate


#  
#     if not db_check:
#         db_pay_rate = models.PayRate(
#             employee_id = pay_rate.employee_id,
#             service_id = pay_rate.service_id,
#             rate_per_service = pay_rate.rate_per_service
#         )
#         db.add(db_pay_rate)
#         db.commit()
#         db.refresh(db_pay_rate)
#         return db_pay_rate
#     else:
#         return edit_pay_rate
    

# def edit_pay_rate(
#         db: Session,
#         pay_rate: schemas.PayRateIn
# ):
#     db_pay_rate = db.query(models.PayRate).filter(
#         models.PayRate.employee_id == pay_rate.employee_id,
#         models.PayRate.service_id == pay_rate.service_id,
#     )
#     db_pay_rate(
#         employee_id = pay_rate.employee_id,
#         service_id = pay_rate.service_id,
#         rate_per_service = pay_rate.rate_per_service
#     )
#     db.commit()
#     db.refresh(db_pay_rate)
#     return db_pay_rate
