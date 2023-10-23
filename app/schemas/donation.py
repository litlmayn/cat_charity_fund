from datetime import datetime
from typing import Optional
from pydantic import BaseModel, PositiveInt

from app.schemas.base import BaseAbstractSchema


class DonationCreate(BaseModel):
    comment: Optional[str]
    full_amount: PositiveInt


class DonationDB(DonationCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationGetAll(BaseAbstractSchema, DonationDB):
    user_id: int
