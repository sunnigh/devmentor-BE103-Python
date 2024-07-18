from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.mysql import Base


class Subscribe(Base):
    __tablename__ = "subscribes"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    # event = relationship("Event", back_populates="subscriptions")
    # user = relationship("User", back_populates="subscriptions")
