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

    class Config:
        orm_mode: True


class EventSubscribe(BaseModel):
    user_id: int

    class Config:
        orm_mode: True
