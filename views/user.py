from fastapi import APIRouter, Depends
from controllers.helper import get_query_token
from models.user import User, users

router = APIRouter(
    dependencies=[Depends(get_query_token)],
    responses={404: {"description": "Not found!"}}
    )


@router.get("/users/{username}", tags=["users"])
async def get_user(username: str):
    user = next((x for x in users if x["username"]==username), "User not found!")
    return {"user": user}


@router.post("/users", tags=["users"])
async def create_user(user: User):
    users.append({**dict(user)})
    return {"message": "User created successfully!", "message": users[-1]}


@router.patch("/users/{username}", tags=["users"])
async def update_user(username: str, user: User):
    for x in users:
        if x["username"]==username:
            x.update({"bio": user.bio})
            return {"message": "User updated successfully!", "user": x}
    return {"message": "Failed to update, try again!"}

@router.delete("/users/{username}", tags=["users"])
async def delete_user(username: str):
    user = next((users.pop(x) for x,y in enumerate(users) if y["username"]==username), "User not found!")
    return {"message": "User deleted successfully!", "user": user}
