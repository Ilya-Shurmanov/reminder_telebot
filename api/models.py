from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    user_name: str
    is_admin: bool
    telegram_id: str
