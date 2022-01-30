from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text

from app.drivers.rdb.base import Base


class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer)
    title = Column(String(128), unique=False, index=True, nullable=False)

    description = Column(Text(1000), nullable=True)

    from_date = Column(DateTime, nullable=False, index=True)
    is_all_day = Column(Boolean, nullable=True)
    to_date = Column(DateTime, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    # color = Column(String(32), nullable=False, index=True)
