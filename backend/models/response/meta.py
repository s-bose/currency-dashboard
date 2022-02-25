from typing import List
from pydantic import BaseModel


class Meta(BaseModel):
    started_at: str
    available_endpoints: List[str]