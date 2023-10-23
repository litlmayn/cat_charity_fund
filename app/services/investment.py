from datetime import datetime
from typing import Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.charity_project import CharityProject
from app.models.donation import Donation


def close_charity_prorject(db_obj):
    db_obj.fully_invested = True
    db_obj.close_date = datetime.utcnow()


async def investment_process(
    obj_in: Union[CharityProject, Donation],
    db_obj: Union[CharityProject, Donation],
    session: AsyncSession,
):
    db_objs = await session.execute(
        select(db_obj)
        .where(db_obj.fully_invested == 0)
        .order_by(db_obj.id.desc())
    )
    db_objs = db_objs.scalars().all()
    while db_objs and obj_in.full_amount > obj_in.invested_amount:
        db_obj = db_objs.pop()
        needed_money = db_obj.full_amount - db_obj.invested_amount
        if obj_in.full_amount > needed_money:
            obj_in.invested_amount += needed_money
        else:
            obj_in.invested_amount = obj_in.full_amount
            close_charity_prorject(obj_in)
            db_obj.invested_amount += obj_in.full_amount
            if db_obj.invested_amount == db_obj.full_amount:
                close_charity_prorject(db_obj)
        session.add(db_obj)
    session.add(obj_in)
    await session.commit()
    await session.refresh(obj_in)
    return obj_in
