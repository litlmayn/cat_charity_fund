from sqlalchemy import Column, String

from app.models.base import IvestmentModel


class CharityProject(IvestmentModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String, nullable=False)
