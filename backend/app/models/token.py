from datetime import timedelta
from uuid import UUID
from pydantic import BaseModel


class Token(BaseModel):
    exp: timedelta
    id: UUID