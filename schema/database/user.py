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
    pass

class UserUpdate(UserBase):
    pass