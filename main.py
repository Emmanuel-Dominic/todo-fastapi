from fastapi import FastAPI
from views.admin import router as admin_router
from views.todo import router as todo_router
from views.user import router as user_router

app = FastAPI()

app.include_router(admin_router)
app.include_router(user_router)
app.include_router(todo_router)


@app.get("/")
async def home():
    return {"message": "Welcome to the home page!"}
