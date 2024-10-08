from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from .. import schemas, utils_db, utils_sec
from ..crud import crud_services
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/api/{company_id}/services', response_model=schemas.ServiceOut)
def create_service(
    company_id: int,
    service: schemas.ServiceIn,
    db: Session = Depends(utils_db.get_db),
    current_user: str = Depends(utils_sec.get_current_active_user)
):
    db_service = crud_services.lookup_service_by_name(
        db, 
        title=service.title, 
        company_id=company_id
    )
    if db_service is not None:
        raise HTTPException(status_code=400, detail="service already registered")
    return crud_services.register_new_service(
        db=db, 
        service=service, 
        company_id=company_id,
        
    )


@router.get('/api/{company_id}/services')
def list_services(
    company_id: int,
    db: Session = Depends(utils_db.get_db),
    current_user: str = Depends(utils_sec.get_current_active_user)
):
    services = crud_services.list_services(db=db, company_id=company_id)
    return services


@router.get('/api/{company_id}/service/{service_id}')
def get_one_service(
    company_id: int,
    service_id: int,
    db: Session = Depends(utils_db.get_db),
    current_user: str = Depends(utils_sec.get_current_active_user)
):
    service = crud_services.get_services_by_id(
        db=db, 
        service_id=service_id, 
        company_id=company_id
    )
    if service is None:
        raise HTTPException(status_code=404, detail='service not found')
    return service


@router.put('/api/{company_id}/service/{service_id}')
def update_service(
    company_id: int,
    service_id: int,
    service_update: schemas.ServiceIn,
    db: Session = Depends(utils_db.get_db),
    current_user: str = Depends(utils_sec.get_current_active_user)
):
    service = crud_services.update_service(
        db=db, 
        company_id=company_id, 
        service_id=service_id,
        service_update=service_update
    )
    if service is None:
        raise HTTPException(status_code=404, detail='service not found')
    return service


@router.put('/api/{company_id}/service_activation_toggle/{service_id}')
def toggle_service_status(
    company_id: int,
    service_id: int,
    db: Session = Depends(utils_db.get_db),
    current_user: str = Depends(utils_sec.get_current_active_user)
):
    service = crud_services.toggle_activation(
        db=db, 
        company_id=company_id, 
        service_id=service_id
    )
    if service is None:
        raise HTTPException(status_code=404, detail='service not found')
    return service


@router.delete('/api/{company_id}/service/{service_id}')
def delete_service(
    company_id: int,
    service_id: int,
    db: Session = Depends(utils_db.get_db),
    current_user: str = Depends(utils_sec.get_current_active_user)
):
    return crud_services.delete_service(db, service_id, company_id=company_id)