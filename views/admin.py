from fastapi import APIRouter, Depends
from controllers.helper import get_token_header, get_query_token
from models.user import users

router = APIRouter(
    tags=["admin"],
    dependencies=[Depends(get_token_header), Depends(get_query_token)],
    responses={404: {"description": "Not found!"}}
    )


@router.get("/users")
async def get_users():
    return {"users": users}
