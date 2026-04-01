from sqlalchemy.orm import Relationship

from app.db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text


class Notification(Base):
    __tablename__ = 'notification'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    type = Column(String(32), nullable=False, default='BLOG')
    target_id = Column(Integer, default=0)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = Relationship('User', backref='notifications', lazy=True)
