from datetime import datetime
from pydantic import BaseModel


class Token(BaseModel):
    expires: datetime
    data: dict