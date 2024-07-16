from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.mysql import Base


class NotificationMethod(Base):
    __tablename__ = 'notification_methods'

    notificationmethod_id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)
    data = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    event_id = Column(Integer, ForeignKey('events.event_id', ondelete='CASCADE'), nullable=False)

    user = relationship("User", back_populates="notification_methods")
    event = relationship("Event", back_populates="notification_methods")
