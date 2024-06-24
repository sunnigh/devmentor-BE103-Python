from sqlalchemy import Column, Integer, Date
from sqlalchemy.orm import relationship
from infrastructure.mysql import Base

class Event(Base):
    __tablename__ = "Event"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)

    # users = relationship("User", secondary="event_subscribe_user", back_populates="event")
    # notification_methods = relationship("EventNotificationMethod", back_populates="event")
    # contents = relationship("ContentEvent", back_populates="event")