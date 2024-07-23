from sqlalchemy import Column, Integer, String, ForeignKey
from infrastructure.mysql import Base
from sqlalchemy.orm import relationship


class Content(Base):
    __tablename__ = 'contents'

    id = Column(Integer, primary_key=True)
    language = Column(String(255), nullable=False)
    contents_data = Column(String(255), nullable=False)
    event_id = Column(Integer, nullable=False)

    # event = relationship("Event", back_populates="contents")
