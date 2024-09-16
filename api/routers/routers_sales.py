from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from .. import schemas, utils_db
from ..crud import crud_sales
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/api/{company_id}/sales/')
def create_new_sale():
    pass


@router.get('/api/{company_id}/sales/')
def list_sales():
    pass


@router.get('/api/{company_id}/sale/{sale_id}')
def detail_sale():
    pass


@router.put('/api/{company_id}/sale/{sale_id}')
def edit_sale():
    pass


@router.delete('/api/{company_id}/sale/{sale_id}')
def delete_sale():
    pass