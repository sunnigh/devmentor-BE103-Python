from sqlalchemy import Column, Integer, Date
from sqlalchemy.orm import relationship
from infrastructure.mysql import Base


class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, index=True)
    event_date = Column(Date, nullable=False)

    subscriptions = relationship("Subscribe", back_populates="event")
    # notification_methods = relationship("EventNotificationMethod", back_populates="event")
    contents = relationship("Content", back_populates="event")
