from sqlalchemy import Column, String

from app.models.base import BaseAbstractModel


class CharityProject(BaseAbstractModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String, nullable=False)
