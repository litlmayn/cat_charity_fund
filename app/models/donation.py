from sqlalchemy import Column, String, Integer, ForeignKey

from app.models.base import BaseAbstractModel


class Donation(BaseAbstractModel):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(String)
