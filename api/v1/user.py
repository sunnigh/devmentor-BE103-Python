from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import repository.user
from infrastructure.mysql import get_db
from infrastructure.token import create_access_token
from schema.database.user import UserCreate, UserUpdate,Token,UserBase
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  #相對URL

router = APIRouter(
    tags=["user"],
    prefix="/users"
)

# 取得全部
# [GET] /v1/users
@router.get("/")
def list_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = repository.user.lists(db, skip=skip, limit=limit)
    return users

# 新增
# [POST] /v1/users
# @router.post("/")   等同@router.post("/register")
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     return repository.user.create(db=db, user=user)

# 取得特定
# [GET] /v1/users/{id}
@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return repository.user.get(db, user_id)

# 更新特定
# [PUT] /v1/users/{id}
@router.put("/{user_id}")
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    return repository.user.update(db, user_id, user_update)

# 刪除特定
# [DELETE] /v1/users/{id}
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return repository.user.delete(db, user_id)
################################################################################
@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = repository.user.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=infrastructure.token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@router.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return repository.user.create(db, user)
