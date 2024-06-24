from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.mysql import Base

class Notify(Base):
    __tablename__ = "notification_methods"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    type = Column(String(255), nullable=False)
    data = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="notification_methods")