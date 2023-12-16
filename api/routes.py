from fastapi import APIRouter, HTTPException

from api.models import User
from api.db_tools.data_getter import get_user
router = APIRouter()


# Example endpoint to handle POST requests
@router.post("/user/add/")
async def create_item(user: User):
    # process the item data, e.g., save it to a database
    return {"item_name": user.name, "item_description": user.description}

# Example endpoint to handle GET requests
# @router.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}


@router.get("/users/{user_id}")
async def get_users(user_id: int):
    user = await get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user.user_id, "user_name": user.user_name}
