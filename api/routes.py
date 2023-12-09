from fastapi import APIRouter, HTTPException
from models import User
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


@router.get("/users/")
async def get_users():
    return {"test ok"}
