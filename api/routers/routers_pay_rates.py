from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
    Cookie
)
from .. import schemas, utils_db, utils_sec
from ..crud import crud_pay_rates
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()


@router.post("/api/{company_id}/pay_rates/", response_model=schemas.PayRateOut)
def post_pay_rate(
    company_id: int,
    pay_rate: schemas.PayRateIn,
    db: Session = Depends(utils_db.get_db),
    access_token: str = Cookie(None)
):
    return crud_pay_rates.post_pay_rate(db, pay_rate=pay_rate, company_id=company_id)


@router.get('/api/{company_id}/pay_rates/', response_model=list[schemas.PayRateOut])
def get_pay_rates(
    company_id: int,
    db: Session = Depends(utils_db.get_db),
    access_token: str = Cookie(None)
):
    return crud_pay_rates.get_all_pay_rates(db=db, company_id=company_id)

@router.get('/api/{company_id}/pay_rate/{employee_id}/{service_id}/', response_model=schemas.PayRateOut)
def get_one_rate(
    company_id: int,
    employee_id: int,
    service_id: int,
    db: Session = Depends(utils_db.get_db),
    access_token: str = Cookie(None)
):
    return crud_pay_rates.get_one_rate(db=db, company_id=company_id, employee_id=employee_id, service_id=service_id)