from sqlalchemy import Column, String, Integer, ForeignKey

from app.models.base import AbstractModel


class Donation(AbstractModel):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(String)
