from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks = [
    Task(id=1, title="Write assignment", completed=False)
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}


@app.get("/tasks")
def list_tasks():
    return tasks


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    new_task = Task(id=len(tasks) + 1, title=task.title, completed=task.completed)
    tasks.append(new_task)
    return new_task


# TODO: Implement GET /tasks/{task_id}
# TODO: Implement PUT /tasks/{task_id}
# TODO: Implement DELETE /tasks/{task_id}
