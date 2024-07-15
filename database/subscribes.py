from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.mysql import Base


class Subscribe(Base):
    __tablename__ = "subscribes"

    subscribe_id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.event_id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)

    event = relationship("Event", back_populates="subscriptions")
    user = relationship("User", back_populates="subscriptions")
