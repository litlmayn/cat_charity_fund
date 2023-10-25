from datetime import datetime

from app.models.base import IvestmentModel


def investment_process(
    target: IvestmentModel,
    sources: list[IvestmentModel],
) -> list[IvestmentModel]:
    redact_sources = []
    for source in sources:
        money = min(
            target.full_amount - target.invested_amount,
            source.full_amount - source.invested_amount
        )
        if money == 0:
            break
        for object in [source, target]:
            object.invested_amount += money
            if object.invested_amount == object.full_amount:
                object.fully_invested = True
                object.close_date = datetime.utcnow()
        redact_sources.append(source)
    return redact_sources
