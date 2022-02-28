
from http.client import HTTPException
from pydantic import EmailStr
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status


from ..db.crud.users import UsersCrud
from ..dependencies.database import get_crud
from ..dependencies.auth import get_current_user

from ..models.users import UserCreate, UserSchema

router = APIRouter(prefix='/users')

@router.get('/', response_model=UserSchema)
async def get_user(
    user: UserSchema = Depends(get_current_user)
):
    return user


@router.post('/register', response_model=UserSchema)
async def user_register(
    user_schema: UserCreate,
    crud: UsersCrud = Depends(get_crud(UsersCrud))
) -> UserSchema:

    new_user = await crud.create_user(user_schema)
    return new_user


@router.post('/login')
async def user_login(
    *, 
    form: OAuth2PasswordRequestForm = Depends(),
    crud: UsersCrud = Depends(get_crud(UsersCrud)) 
):
    if await crud.get_user_by_email(email=form.username) is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='email not found'
        )

    if user := await crud.auth_user(
        email=form.username,
        password=form.password
    )
