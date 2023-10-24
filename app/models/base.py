from datetime import datetime

from sqlalchemy import (
    Column, Boolean, DateTime, Integer, CheckConstraint
)

from app.core.db import Base


class AbstractModel(Base):
    __abstract__ = True
    __table_args__ = (
        CheckConstraint("full_amount>0", "full_amount>invested_amount"),
    )

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False, )
    create_date = Column(DateTime, default=datetime.utcnow)
    close_date = Column(DateTime)
