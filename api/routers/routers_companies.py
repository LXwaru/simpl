from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from .. import schemas, utils_db
from ..crud import crud_companies
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/api/{admin_id}/companies/', response_model=schemas.CompanyOut)
def create_company(
    admin_id: int,
    company: schemas.CompanyIn,
    db: Session = Depends(utils_db.get_db)
):
    return crud_companies.create_company(db=db, company=company, admin_id=admin_id)

@router.get('/api/{admin_id}/companies/', response_model=schemas.CompanyOut)
def get_company_by_admin(
    admin_id: int,
    db: Session = Depends(utils_db.get_db)
):
    return crud_companies.get_company(db=db, admin_id=admin_id)