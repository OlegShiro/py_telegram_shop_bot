from datetime import datetime, timezone

from sqlalchemy import Column, Integer, DateTime

from database.session import base


class User(base):
    __tablename__ = "users"

    uid = Column(Integer, autoincrement=True, primary_key=True)
    registered_at = Column(DateTime, default=datetime.now(timezone.utc))
