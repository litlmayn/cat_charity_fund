from sqlalchemy import Column, String, Integer, ForeignKey

from app.models.base import IvestmentModel


class Donation(IvestmentModel):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(String)
