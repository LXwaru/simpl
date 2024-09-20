from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from .. import schemas, utils_db
from ..crud import crud_sale_items
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/api/{company_id}/sale_item/', response_model=schemas.SaleItemOut)
def create_sale_item(
    company_id: int,
    sale_item: schemas.SaleItemIn,
    db: Session = Depends(utils_db.get_db)
):
    return crud_sale_items.create_sale_item(
        db=db, company_id=company_id, sale_item=sale_item
    )