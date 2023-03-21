from pydantic import BaseModel


class User(BaseModel):
    username: str
    bio: str


users = [
    {"username": "Emmanuel", "bio": "This is bout Emmanuel"},
    {"username": "fakecurrentuser", "bio": "This is bout fakecurrentuser"},
    {"username": "Dominic", "bio": "This is bout Dominic"}
]
