from uuid import UUID
from pydantic import BaseModel, EmailStr

class Users(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    password: str
