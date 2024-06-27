from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    account: str
    password: str
    is_login: bool
    language: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    # events: List[int] = []
    # notification_methods: List[int] = []

    class Config:
        orm_mode: True

class UserUpdate(UserBase):
    username: str | None = None
    account: str | None = None
    password: str | None = None
    is_login: bool | None = None
    language: str | None = None

class UserInDB(UserBase):
    hashed_password: str | None = None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
