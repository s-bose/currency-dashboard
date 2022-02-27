from typing import Callable, Type
from databases import Database
from fastapi import Depends
from starlette.requests import Request
from app.db.crud.base import BaseCrud


def get_database(request: Request) -> Database:
    return request.app.state._db


def get_repository(Repo_type: Type[BaseCrud]) -> Callable:
    def get_repo(db: Database = Depends(get_database)) -> Type[BaseCrud]:
        return Repo_type(db)

    return get_repo