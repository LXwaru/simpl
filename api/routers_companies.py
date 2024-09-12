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


@router.post('/api/{admin_id}/companies/', response_model=schemas.CompanyOut)
def create_company(
    admin_id: int,
    company: schemas.CompanyIn,
    db: Session = Depends(utils_db.get_db)
):
    return crud_companies.create_company(db=db, company=company, admin_id=admin_id)