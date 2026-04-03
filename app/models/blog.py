from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import Relationship

from app.db.database import Base


class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=True)
    content = Column(Text, nullable=False)
    is_published = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    author = Relationship('User', backref='blogs', lazy=True)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
