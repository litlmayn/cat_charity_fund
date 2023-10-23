from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models import CharityProject
from app.schemas.charity_project import CharityProjectUpdate


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
):
    project_id = await charity_project_crud.get_project_id_by_name(project_name, session)
    if project_id:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!',
        )


async def check_charity_project_exists(
        project_id: int,
        session: AsyncSession
):
    charity_project = await charity_project_crud.get(project_id, session)
    if charity_project is None:
        raise HTTPException(
            status_code=404,
            detail='Проект для инвестирования не найден!'
        )
    return charity_project


async def check_update_charity_project(
        charity_project: CharityProject,
        charity_project_update: CharityProjectUpdate
):
    if charity_project.fully_invested:
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!',
        )

    if (charity_project_update.full_amount and
            charity_project.invested_amount > charity_project_update.full_amount):
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!'
        )


async def check_charity_project_invested(charity_project: CharityProject):
    if charity_project.invested_amount > 0:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!'
        )