from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import Relationship

from app.db.database import Base


class BlogImage(Base):
    __tablename__ = 'blogimage'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(Text, nullable=False)

    blog_id = Column(Integer, ForeignKey('blog.id'), nullable=False)
    blog = Relationship('Blog', backref='images', lazy=True)