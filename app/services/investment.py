from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession


def close_charity_prorject(db_obj):
    db_obj.fully_invested = True
    db_obj.close_date = datetime.utcnow()


async def investment_process(
    target,
    sources,
    session: AsyncSession,
):
    while sources and target.full_amount > target.invested_amount:
        source = sources.pop()
        needed_money = source.full_amount - source.invested_amount
        if target.full_amount > needed_money:
            target.invested_amount += needed_money
        else:
            target.invested_amount = target.full_amount
            close_charity_prorject(target)
            source.invested_amount += target.full_amount
            if source.invested_amount == source.full_amount:
                close_charity_prorject(source)
        session.add(source)
    session.add(target)
    await session.commit()
    await session.refresh(target)
    return target
