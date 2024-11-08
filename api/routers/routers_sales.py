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
from ..crud import crud_sales
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()


@router.post('/api/{company_id}/sales/', response_model=schemas.SaleOut)
def create_new_sale(
    company_id: int,
    sale: schemas.SaleIn,
    db: Session = Depends(utils_db.get_db),
    access_token: str = Cookie(None)
):
    return crud_sales.create_sale(
        db=db,
        company_id=company_id,
        sale=sale
    )


@router.get('/api/{company_id}/sales/', response_model=list[schemas.SaleOut])
def list_sales(
    company_id: int,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    sale = crud_sales.list_sales(
        db=db, company_id=company_id
    )
    if sale is None:
        raise HTTPException(status_code=404, detail='no sales found')
    return sale


@router.get('/api/{company_id}/sale/{sale_id}', response_model=schemas.SaleOut)
def get_sale(
    company_id: int,
    sale_id: int,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    sale = crud_sales.get_sale(
        db=db,
        company_id=company_id,
        sale_id=sale_id
    )
    if sale is None:
        raise HTTPException(status_code=404, detail='sale not found')
    return sale


@router.delete('/api/{company_id}/sale/{sale_id}')
def delete_sale(
    company_id: int,
    sale_id: int,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    return crud_sales.delete_sale(db=db, company_id=company_id, sale_id=sale_id)
