from uuid import UUID
from pydantic import EmailStr
from databases import Database

from .base import BaseCrud
from ...models.users import UserCreate, UsersDB


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

    QUERY_GET_USER_BY_EMAIL = """
        SELECT id, name, email FROM users
        WHERE email=:email;
    """

    QUERY_DELETE_USER = """
        DELETE FROM users WHERE id=:id;
    """


    async def create_user(self, new_user: UserCreate) -> UsersDB:
        values = new_user.dict()
        response = await self.db.fetch_one(self.QUERY_CREATE_USER, values=values)

        return UsersDB(**response)

    
    async def get_user_by_email(self, email: EmailStr) -> UsersDB:
        response = await self.db.fetch_one(self.QUERY_GET_USER_BY_EMAIL,
                                           value={'email': email})

        return UsersDB(**response)

    
    async def get_user_by_id(self, id: UUID) -> UsersDB:
        response = await self.db.fetch_one(self.QUERY_GET_USER, value={'id': id})

        return UsersDB(**response)

    
    # async def delete_user(self, id: UUID) -> UsersDB:
    #     response = await self.db.fetch_one(self.QUERY_DELETE_USER, value={'id': id})

    #     return 