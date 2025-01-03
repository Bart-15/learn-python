from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
	id: int
	todo: str
	is_complete: bool = False

todos = []

@app.get("/")
def read_root():
	return {"message": "Sample Simple Fast API"}

@app.post("/todos")
def create_todo(payload: Todo):
	todos.append(payload)
	return JSONResponse(
		content={"message": "Todo item created successfully", "status": "success"},
		status_code=201  # HTTP 201 Created status
	)

@app.get("/todos")
def list_todos(limit: int = 10, response_model=list[Todo]):
	return todos[0:limit]

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo_by_id(todo_id: int):

	if(todo_id < len(todos)):
		for todo in todos:
			if todo.id == todo_id:
				return todo
	else:
		raise HTTPException(status_code=404, detail=f"Item {todo_id} not found")


@app.delete("/todos/{todo_id}")
def delete_todo_by_id(todo_id: int):
	for todo in todos:
		if todo.id == todo_id:
			todos.remove(todo)

		return JSONResponse(
			content={"message": f"Todo item with ID {todo_id} deleted successfully", "status": "success"},
			status_code=200  # HTTP 200 OK status
    	)

	raise HTTPException(status_code=404, detail=f"Todo with ID {todo_id} not found")
