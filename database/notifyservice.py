from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.mysql import Base


class NotifyService(Base):
    __tablename__ = 'notify_services'

    notify_service_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.event_id', ondelete='CASCADE'), nullable=False)
    notification_method_id = Column(Integer,
                                    ForeignKey('notification_methods.notificationmethod_id', ondelete='CASCADE'),
                                    nullable=False)

    event = relationship("Event", back_populates="notify_services")
    notification_method = relationship("NotificationMethod", back_populates="notify_services")
