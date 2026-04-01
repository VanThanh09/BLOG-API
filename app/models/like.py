from sqlalchemy.orm import Relationship

from app.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Like(Base):
    __tablename__ = 'like'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    blog_id = Column(Integer, ForeignKey('blog.id'), nullable=False)

    user = Relationship('User', backref='likes', lazy=True)
    blog = Relationship('blog', backref='likes', lazy=True)