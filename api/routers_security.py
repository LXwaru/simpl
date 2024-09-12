from datetime import datetime, timedelta, timezone
from typing import Annotated, Union
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from . import models, utils_sec, utils_db, schemas
from sqlalchemy.orm import Session

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get('/token')
async def get_token(
    token: Annotated[str, Depends(oauth2_scheme)]
    ):
    return {'token': token}


@router.post("/token", response_model=models.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
    db: Session = Depends(utils_db.get_db),
) -> models.Token: 
    user = utils_sec.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        ) 
    access_token_expires = timedelta(minutes=utils_sec.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = utils_sec.create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )
    return models.Token(access_token=access_token, token_type="bearer")



@router.get("/users/me", response_model=schemas.AdminOut)
async def read_users_me(
    current_user: Annotated[models.Admin, Depends(utils_sec.get_current_active_user)]
    ):  
    return current_user