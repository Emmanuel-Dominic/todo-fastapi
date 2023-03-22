from typing import Annotated
from fastapi import Header


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        return {"error": "Invalid token!"}

async def get_query_token(token: str):
    if token != "emmanuel":
        return {"error": "No token provided!"}
