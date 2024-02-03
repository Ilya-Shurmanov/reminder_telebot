from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    user_id: int
    user_name: Optional[str]
    is_admin: bool
    telegram_id: Optional[str]
