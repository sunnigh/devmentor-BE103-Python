from sqlalchemy import Column, Integer, ForeignKey
from infrastructure.mysql import Base


class NotifyService(Base):
    __tablename__ = 'notify_services'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    event_id = Column(Integer, nullable=False)
    notification_method_id = Column(Integer, nullable=False)
