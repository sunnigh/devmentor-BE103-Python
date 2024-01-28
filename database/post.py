from sqlalchemy import Boolean, Column, Integer, String

from infrastructure.mysql import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    content = Column(String)
    is_active = Column(Boolean, default=True)


