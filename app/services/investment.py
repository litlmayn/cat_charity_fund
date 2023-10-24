from datetime import datetime


def investment_process(
    target,
    sources,
):
    for source in sources:
        needed_money = target.full_amount - target.invested_amount
        if needed_money == 0:
            break
        for object in [source, target]:
            object.invested_amount += needed_money
            if object.invested_amount == object.full_amount:
                object.fully_invested = True
                object.close_date = datetime.utcnow()
    return target
