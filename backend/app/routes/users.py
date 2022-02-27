
from pydantic import EmailStr
from fastapi import APIRouter, Depends

from ..db.crud.users import UsersCrud
from ..dependencies.database import get_crud
from ..models.users import UserCreate

router = APIRouter()

@router.get('/users')
async def get_user(
    email: EmailStr,
    user_crud: UsersCrud = Depends(get_crud(UsersCrud))
):

    user = await user_crud.get_user_by_email(email=email)
    return user


@router.post('/users')
async def add_user(
    user_schema: UserCreate,
    user_crud: UsersCrud = Depends(get_crud(UsersCrud))
):

    new_user = await user_crud.create_user(user_schema)
    return new_user