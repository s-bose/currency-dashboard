from typing import Callable, Type
from databases import Database
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from starlette.requests import Request

from app.models.users import UsersDB

from ..db.crud import BaseCrud, UsersCrud
from ..configs.configs import settings

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_STR}/user/login"
)


def get_db(request: Request) -> Database:
    return request.app.state._db


def get_crud(CrudType: Type[BaseCrud]) -> Callable:
    def _crud(db: Database = Depends(get_db)) -> Type[BaseCrud]:
        return CrudType(db)

    return _crud


def auth_user(
    user_crud: UsersCrud = Depends(get_crud(UsersCrud)),
    token: str = Depends(reusable_oauth2)
) -> UsersDB:

    pass
    # TODO - jwt authentication