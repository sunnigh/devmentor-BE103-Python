from pydantic import BaseModel

class NotifyBase(BaseModel):
    user_id: int
    type: str
    data: str

class Notify(NotifyBase):
    id: int

    class Config:
        orm_mode: True
class NotifyCreate(NotifyBase):
    pass

class NotifyUpdate(NotifyBase):
    type: str | None = None
    data: str | None = None