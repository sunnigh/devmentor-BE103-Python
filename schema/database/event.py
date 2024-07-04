from pydantic import BaseModel
from datetime import date


class EventBase(BaseModel):
    date: date

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    date: date

class Event(EventBase):
    id: int
    # users: List[int] = []
    # notification_methods: List[int] = []
    # contents: List[int] = []

    class Config:
        orm_mode: True