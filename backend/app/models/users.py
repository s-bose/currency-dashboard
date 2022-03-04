from typing import Optional

from uuid import UUID
from pydantic import BaseModel, EmailStr, SecretStr, validator

class Users(BaseModel):     # base class
    id: UUID
    name: str
    email: EmailStr
    password: SecretStr

    
class UserCreate(BaseModel):
    email: EmailStr
    password: SecretStr
    name: Optional[str] = None


    @validator('name', always=True)
    def name_validator(cls, v, values):
        if not v:
            v = values['email'].split('@')[0]
        return v

    
class UserSchema(BaseModel):
    id: UUID
    name: str
    email: EmailStr

