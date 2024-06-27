from sqlalchemy import Boolean, Column, Integer, String
from infrastructure.mysql import Base

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    account = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_login = Column(Boolean, default=False)
    language = Column(String(255), nullable=False)