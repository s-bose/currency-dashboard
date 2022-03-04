from uuid import UUID
from pydantic import EmailStr

from .base import BaseCrud
from ...models.users import Users, UserCreate
from ...core import security

class UsersCrud(BaseCrud):

    QUERY_CREATE_USER = """
        INSERT INTO users (name, email, password)
        VALUES (:name, :email, :password)
        returning id, name, email, password;
    """

    QUERY_GET_USER = """
        SELECT * FROM users WHERE id=:id;
    """

    QUERY_GET_USER_BY_EMAIL = """
        SELECT * FROM users WHERE email=:email;
    """

    QUERY_DELETE_USER = """
        DELETE FROM users WHERE id=:id;
    """


    async def create_user(self, new_user: UserCreate) -> Users:
        values = new_user.dict()
        values['password'] = security.gen_hash(password=values['password'])

        response = await self.db.fetch_one(self.QUERY_CREATE_USER, values=values)

        return Users(**response)

    
    async def get_user_by_email(self, email: EmailStr) -> Users:
        response = await self.db.fetch_one(self.QUERY_GET_USER_BY_EMAIL,
                                           values={'email': email})

        return Users(**response)

    
    async def get_user_by_id(self, id: UUID) -> Users:
        response = await self.db.fetch_one(self.QUERY_GET_USER, values={'id': id})

        return Users(**response)



    async def auth_user(
        self,
        email: EmailStr,
        password: str
    ) -> Users:

        user: Users = await self.get_user_by_email(email=email)
        if not security.verify_password(
                                plain_pwd=password,
                                hash_pwd=user.password.get_secret_value()): 
            
            return None
        
        return user

    # async def delete_user(self, id: UUID) -> UsersDB:
    #     response = await self.db.fetch_one(self.QUERY_DELETE_USER, value={'id': id})

    #     return 