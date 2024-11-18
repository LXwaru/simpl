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


@router.post("/api/pay_rates/", response_model=schemas.PayRateOut)
def post_pay_rate(
    pay_rate: schemas.PayRateIn,
    db: Session = Depends(utils_db.get_db),
    access_token: str = Cookie(None)
):
    return crud_pay_rates.post_pay_rate(db, pay_rate=pay_rate)