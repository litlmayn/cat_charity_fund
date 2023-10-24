from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_name_duplicate, check_charity_project_exists,
    check_update_charity_project, check_charity_project_invested
)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.models.donation import Donation
from app.schemas.charity_project import (
    CharityProjectDB, CharityProjectCreate, CharityProjectUpdate
)
from app.services.investment import investment_process


router = APIRouter()


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session),
):
    return await charity_project_crud.get_multi(session)


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_charity_project(
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзера."""
    await check_name_duplicate(charity_project.name, session)
    charity_project = await charity_project_crud.create(
        charity_project, session
    )
    sources = await charity_project_crud.get_db_objs_for_investment(Donation, session)
    charity_project = await investment_process(charity_project, sources, session)
    return charity_project


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def delete_charity_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """Только для суперюзера."""
    charity_project = await check_charity_project_exists(project_id, session)
    check_charity_project_invested(charity_project)
    charity_project = await charity_project_crud.remove(
        charity_project, session
    )
    return charity_project


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзера."""
    await check_name_duplicate(obj_in.name, session)
    charity_project = await check_charity_project_exists(project_id, session)
    check_update_charity_project(charity_project, obj_in)
    charity_project = await charity_project_crud.update(
        charity_project, obj_in, session
    )
    return charity_project
