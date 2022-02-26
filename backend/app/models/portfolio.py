from uuid import UUID
from pydantic import BaseModel

class Portfolio(BaseModel):
    id: UUID
    user_id: UUID
    currency_id: UUID
    holdings: int