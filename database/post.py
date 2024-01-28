from sqlalchemy import Boolean, Column, Integer, String

from infrastructure.mysql import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), index=True)
    content = Column(String(255))
    is_active = Column(Boolean, default=True)


