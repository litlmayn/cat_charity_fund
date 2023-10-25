from datetime import datetime
from typing import Union

from app.models.charity_project import CharityProject
from app.models.donation import Donation


def investment_process(
    target: Union[CharityProject, Donation],
    sources: list[Union[CharityProject, Donation]],
) -> list[Union[CharityProject, Donation]]:
    redact_sources = []
    for source in sources:
        needed_money = target.full_amount - target.invested_amount
        donation_money = source.full_amount - source.invested_amount
        if needed_money == 0:
            break
        if needed_money > donation_money:
            needed_money = donation_money
        for object in [source, target]:
            object.invested_amount += needed_money
            if object.invested_amount == object.full_amount:
                object.fully_invested = True
                object.close_date = datetime.utcnow()
        redact_sources.append(source)
    return redact_sources
