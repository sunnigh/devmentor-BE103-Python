from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
import repository.user
from infrastructure.mysql import get_db
from schema.database.user import UserCreate, UserUpdate, User, RegisterUserRequest, DuplicateCheckRequest
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from service.user import login_for_access_token, get_current_user, register_user

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


# 取得特定
# [GET] /v1/users/{id}
@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return repository.user.get(db, user_id)


# 更新特定
# [PUT] /v1/users/{id}

@router.put("/{user_id}")
def update_user(user_id: int,
                user_update: UserUpdate,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    return repository.user.update(db, user_id, user_update, current_user)


# 刪除特定
# [DELETE] /v1/users/{id}
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return repository.user.delete(db, user_id)


################################################################################
@router.post("/token")
async def log_in_with_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Session = Depends(get_db)
):
    return login_for_access_token(db, form_data.username, form_data.password)


@router.post("/register")
async def register(request: RegisterUserRequest, db: Session = Depends(get_db)):
    return register_user(request, db)


@router.post("/check-duplicate")
async def check_duplicate(request: DuplicateCheckRequest, db: Session = Depends(get_db)):
    repository.user.get_by_account(db, request.account)
    repository.user.get_by_password(db, request.password)
    return {"message": "No duplicates found"}
