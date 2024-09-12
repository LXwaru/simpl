from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from . import schemas, crud_companies, utils_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/api/companies/', response_model=schemas.CompanyOut)
def create_company(
    company: schemas.CompanyIn,
    db: Session = Depends(utils_db.get_db)
):
    return crud_companies.create_company(db=db, company=company)

@router.get('/api/companies/', response_model=list[schemas.CompanyOut])
def get_all_companies(
    db: Session = Depends(utils_db.get_db)
):
    return crud_companies.list_companies(db=db)