from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Relationship

from app.db.database import Base


class Follow(Base):
    __tablename__ = 'follow'

    id = Column(Integer, primary_key=True, autoincrement=True)
    follower_id = Column(Integer, ForeignKey('user.id')) # người đi follow
    following_id = Column(Integer, ForeignKey('user.id')) # người được follow

    following = Relationship('User', backref='following', lazy=True, foreign_keys=[follower_id]) # list user mình follow
    follower = Relationship('User', backref='my_follower', lazy=True, foreign_keys=[following_id]) # list user follow mình