from pydantic import BaseModel

class UserBase(BaseModel):
    user_name: str
    account: str
    password: str
    is_login: bool
    language: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    user_id: int

    class Config:
        orm_mode: True

class UserUpdate(UserBase):
    user_name: str | None = None
    account: str | None = None
    password: str | None = None
    is_login: bool | None = None
    language: str | None = None

class UserInDB(UserBase):
    hashed_password: str | None = None

class Token(BaseModel):
    access_token: str
    token_type: str
    is_login: bool

class TokenData(BaseModel):
    user_name: str | None = None
