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
from ..crud import crud_companies
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()


@router.post('/api/companies/{admin_id}/', response_model=schemas.CompanyOut)
def create_company(
    admin_id: int,
    company: schemas.CompanyIn,
    db: Session = Depends(utils_db.get_db),
    access_token: str = Cookie(None)
):
    return crud_companies.create_company(db=db, company=company, admin_id=admin_id)


@router.get('/api/companies', response_model=list[schemas.CompanyOut])
def get_all_companies(
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    companies = crud_companies.get_all_companies(db=db)
    return companies


@router.get('/api/company/{admin_id}/', response_model=schemas.CompanyOut)
def get_company_by_admin(
    admin_id: int,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    company = crud_companies.get_company(db=db, admin_id=admin_id)
    if company is None:
        raise HTTPException(status_code=404, detail='company not found')
    return company


@router.put('/api/company/{admin_id}/', response_model=schemas.CompanyOut)
def edit_info(
    admin_id: int,
    company: schemas.CompanyIn,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    return crud_companies.edit_info(db=db, admin_id=admin_id, company=company)


@router.delete('/api/company/{company_id}/')
def delete_company(
    admin_id: int,
    company_id: int,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    return crud_companies.delete_company(db=db, admin_id=admin_id, company_id=company_id)


