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
import jwt
from .. import models, utils_sec, utils_db, schemas
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
    response: Response,
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

    response.set_cookie(
        key='access_token',
        value=access_token,
        httponly=True,
        secure=True,
        samesite='Lax',
        max_age=1800
    )
    return models.Token(access_token=access_token, token_type='bearer')


@router.get("/users/me", response_model=schemas.AdminOut)
async def read_users_me(
    request: Request,
    db: Session = Depends(utils_db.get_db),
    ):  
    access_token = request.cookies.get('access_token')
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='no access token found in cookies'
        )
    
    try:
        payload = jwt.decode(access_token, utils_sec. SECRET_KEY, algorithms=[utils_sec.ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="invalid token payload"
            )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='token has expired'
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='invalid token'
        )
    current_user = utils_sec.get_user(db, username)
    if current_user is None:
        raise HTTPException(
            status=status.HTTP_401_UNAUTHORIZED,
            detail='user not found'
        )
    return current_user