from sqlalchemy import Column, String

from app.models.base import AbstractModel


class CharityProject(AbstractModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String, nullable=False)
