from tokenize import Token
import jwt
from typing import Callable, Type
from databases import Database
from fastapi import Depends

from fastapi.security import OAuth2PasswordBearer
from starlette import status

from starlette.requests import Request

from app.models.users import UserSchema, UsersDB

from ..db.crud import BaseCrud, UsersCrud
from ..configs.configs import settings


def get_db(request: Request) -> Database:
    return request.app.state._db


def get_crud(CrudType: Type[BaseCrud]) -> Callable:
    def _crud(db: Database = Depends(get_db)) -> Type[BaseCrud]:
        return CrudType(db)

    return _crud


