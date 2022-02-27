from typing import Optional

from uuid import UUID
from pydantic import BaseModel, EmailStr, validator

class Users(BaseModel):
    id: UUID
    name: Optional[str] = None
    email: EmailStr
    password: str

    @validator('name', always=True)
    def name_validator(cls, v, values):
        if not v:
            v = values['email'].split('@')[0]
        return v

    
class UserCreate(BaseModel):
    name: Optional[str] = None
    email: EmailStr

    @validator('name', always=True)
    def name_validator(cls, v, values):
        if not v:
            v = values['email'].split('@')[0]
        return v

    
class UsersDB(BaseModel):
    id: UUID
    name: str
    email: EmailStr