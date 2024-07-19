from sqlalchemy import Boolean, Column, Integer, String
from infrastructure.mysql import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(255), nullable=False)
    account = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_login = Column(Boolean, nullable=False,default=False)
    language = Column(String(255), nullable=False)

    # subscriptions = relationship("Subscribe", back_populates="user")