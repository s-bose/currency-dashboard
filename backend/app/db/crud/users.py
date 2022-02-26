from pydantic import EmailStr
from databases import Database

from app.db.crud.base import BaseCrud



class UsersCrud(BaseCrud):

    QUERY_CREATE_USER = """
        INSERT INTO users (name, email, password)
        VALUES (:name, :email, :password)
        returning id, name, email;
    """

    QUERY_GET_USER = """
        SELECT id, name, email FROM users
        WHERE id=:id;
    """


    # TODO
    # async def create_user(self, ) -> UserDB:
    #     query = await self.db.fetch_one(self.QUERY_CREATE_USER)