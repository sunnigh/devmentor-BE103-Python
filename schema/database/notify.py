from pydantic import BaseModel

class NotifyBase(BaseModel):
    type: str
    data: str
    user_id: int


class NotifyCreate(NotifyBase):
    pass

class NotifyUpdate(NotifyBase):
    type: str | None = None
    data: str | None = None
    user_id: int | None = None


class Notify(NotifyBase):
    id: int

    class Config:
        orm_mode: True