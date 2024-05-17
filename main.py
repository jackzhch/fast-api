from typing import Union
from fastapi import FastAPI
from models import Todo
from pytube import YouTube
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

todos = []

# Get all todos 
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get single todo 
@app.get("/todo/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo not found"}

# Create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been added"}

# Delete a todo
@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo has been deleted"}
    return {"message": "Todo not found"}

# Update a todo
@app.put("/todo/{todo_id}")
async def update_todo(todo_id: int, todo: Todo):
    for t in todos:
        if t.id == todo_id:
            t.id = todo.id
            t.item = todo.item
            return {"message": "Todo has been updated"}
    return {"message": "Todo not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8088)
    # yt = YouTube('http://youtube.com/watch?v=SSnsmqIj1MI')
    # stream = yt.streams.first()
    
    # data={
    #     "uid": "1234",
    #     "url": "http://youtube.com/watch?v=SSnsmqIj1MI",
    #     "title": yt.title,
    #     "author": yt.author,
    #     "length": yt.length,
    #     "description": yt.description,
    #     "rating": yt.rating,
    #     "views": yt.views,
    #     "keywords": yt.keywords,
    # }
    # print(json.dumps(data, indent=4, sort_keys=True))
