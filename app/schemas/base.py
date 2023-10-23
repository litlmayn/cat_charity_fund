from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt


class BaseAbstractSchema(BaseModel):
    full_amount: PositiveInt
    invested_amount: int = 0
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]
