from fastapi import APIRouter, Depends
from controllers.helper import get_token_header
from models.todo import Todo, todos
from models.user import users


router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found!"}},
)


@router.get("/")
async def get_todos():
    return {"todos": todos}


@router.post("/")
async def create_todo(todo: Todo):
    if todo.owner not in users:
        users.append({**dict(todo.owner)})
    todos.append({**dict(todo)})
    return {"message": "Todo created successfully!", "message": todos[-1]}


@router.get("/{title}")
async def get_todo(title: str):
    todo = next((x for x in todos if x["title"]==title), "Todo not found!")
    return {"todo": todo}


@router.patch("/{title}")
async def update_todo(title: str, todo: Todo):
    for x in todos:
        if x["title"]==title:
            x.update({'description': todo.description})
            return {"message": "Todo updated successfully!", "todo": x}
    return {"message": "Failed to update, try again!"}


@router.delete("/{title}")
async def delete_todo(title: str):
    todo = next((todos.pop(x) for x,y in enumerate(todos) if y["title"]==title), "Todo not found!")
    return {"message": "Todo deleted successfully!", "todo": todo}
