from sqlalchemy import Column, Integer, Date
from infrastructure.mysql import Base


class SendLog(Base):
    __tablename__ = 'send_log'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    event_id = Column(Integer, nullable=False)
    event_content = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    notification_method = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
