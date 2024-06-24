from pydantic import BaseModel

class NotifyBase(BaseModel):
    user_id: int
    type: str
    data: str
    is_active: bool

class NotifyCreate(NotifyBase):
    pass

class NotifyUpdate(NotifyBase):
    pass