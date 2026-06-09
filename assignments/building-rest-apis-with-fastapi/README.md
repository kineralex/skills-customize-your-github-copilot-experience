# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by creating routes, handling request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Set up a basic FastAPI application and add a simple endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance
- Add a `GET /` route that returns a JSON message such as `"Welcome to the Task API"`
- Start the app locally with `uvicorn` so it can be opened in a browser or tested with curl

### 🛠️ Implement CRUD Endpoints

#### Description
Build endpoints for managing a collection of tasks stored in memory.

#### Requirements
Completed program should:

- Add a `GET /tasks` endpoint that returns the list of tasks
- Add a `POST /tasks` endpoint that creates a new task
- Add a `GET /tasks/{task_id}` endpoint that returns a single task
- Add a `PUT /tasks/{task_id}` endpoint that updates an existing task
- Add a `DELETE /tasks/{task_id}` endpoint that removes a task
- Return appropriate status codes, including `404` for missing tasks

### 🛠️ Add Validation with Pydantic Models

#### Description
Improve the API by using Pydantic models for request and response validation.

#### Requirements
Completed program should:

- Define a `TaskCreate` model for incoming task data
- Define a `Task` model for response data
- Ensure task titles are required and non-empty
- Use response models so the API returns consistent JSON structures
