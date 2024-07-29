from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.mysql import Base

class Notify(Base):
    __tablename__ = "notification_methods"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(255), nullable=False)
    data = Column(String(255), nullable=False)
    user_id = Column(Integer, nullable=False)


    # user = relationship("user", back_populates="notification_methods")