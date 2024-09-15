from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from .. import schemas, utils_db
from ..crud import crud_services
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/api/{company_id}/services', response_model=schemas.ServiceOut)
def create_service(
    company_id: int,
    service: schemas.ServiceIn,
    db: Session = Depends(utils_db.get_db)
):
    db_service = crud_services.lookup_service_by_name(db, title=service.title)
    if db_service:
        raise HTTPException(status_code=400, detail="service already registered")
    return crud_services.register_new_service(db=db, service=service, company_id=company_id)


@router.get('/api/{company_id}/services')
def list_services():
    pass


@router.get('/api/{company_id}/service/{service_id}')
def get_one_service():
    pass


@router.put('/api/{company_id}/service/{service_id}')
def update_service():
    pass

@router.delete('/api/{company_id}/service/{service_id}')
def delete_service():
    pass