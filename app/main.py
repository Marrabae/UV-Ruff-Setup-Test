from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Todo API")

class Todo(BaseModel):
    id: int
    task: str
    done: bool = False

# dummy storage
todos: list[Todo] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Todo API"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def create_todo(todo: Todo):
    for t in todos:
        if t.id == todo.id:
            raise HTTPException(status_code=400, detail="Todo ID already exists")
    todos.append(todo)
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t.id != todo_id]
    return {"message": f"Todo {todo_id} deleted"}
