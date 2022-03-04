from typing import Callable, Type
from databases import Database
from fastapi import Depends


from starlette.requests import Request


from ..db.crud import BaseCrud


def get_db(request: Request) -> Database:
    return request.app.state._db


def get_crud(CrudType: Type[BaseCrud]) -> Callable:
    def _crud(db: Database = Depends(get_db)) -> Type[BaseCrud]:
        return CrudType(db)

    return _crud


