from pydantic import BaseModel
from .user import User


class Todo(BaseModel):
    title: str
    description: str
    owner: User

    class Config:
        orm_mode = True


todos = [
    {
        "title": "plumbus",
        "description": "This is a plumbus description",
        "owner": {
            "username": "Dominic", "bio": "This is bout Dominic"
        }
    },
    {
        "title": "gun",
        "description": "This is a portal gun description",
        "owner": {
            "username": "Dominic", "bio": "This is bout Dominic"
        }
    }]
