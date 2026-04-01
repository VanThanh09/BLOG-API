from datetime import datetime

from sqlalchemy.orm import Relationship

from app.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = Relationship('User', backref='comments', lazy=True)

    blog_id = Column(Integer, ForeignKey('blog.id'))
    blog = Relationship('Blog', backref='comments', lazy=True)