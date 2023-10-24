from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models.charity_project import CharityProject
from app.models.user import User
from app.schemas.donation import (
    DonationGetAll, DonationCreate, DonationDB
)
from app.services.investment import investment_process


router = APIRouter()


@router.get(
    '/',
    response_model=list[DonationGetAll],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзера."""
    return await donation_crud.get_multi(session)


@router.post(
    '/',
    response_model_exclude_none=True,
    response_model=DonationDB,
)
async def create_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    new_donation = await donation_crud.create(donation, session)
    sources = await donation_crud.get_db_objs_for_investment(CharityProject, session)
    new_donation = await investment_process(new_donation, sources, session)
    return new_donation


@router.get(
    '/my',
    response_model=list[DonationDB],
)
async def get_user_donation(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    return await donation_crud.get_by_user(
        session=session, user=user
    )
