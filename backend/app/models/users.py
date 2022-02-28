from typing import Optional

from uuid import UUID
from pydantic import BaseModel, EmailStr, SecretStr, validator

class Users(BaseModel):     # base class
    id: UUID
    name: str
    email: EmailStr
    password: SecretStr

    
class UserCreate(BaseModel):
    name: Optional[str] = None
    email: EmailStr
    password: SecretStr

    @validator('name', always=True)
    def name_validator(cls, v, values):
        if not v:
            v = values['email'].split('@')[0]
        return v

    
class UserSchema(BaseModel):
    id: UUID
    name: str
    email: EmailStr

