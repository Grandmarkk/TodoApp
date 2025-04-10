import json
from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import HTTPResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database.configurations import init_db, db_session
from database.models import TodoItem
from database.schema import ItemSchema

# Configure fastapi
app = FastAPI()

# Configure static route
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure template
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def startup():
    """
    Initialize the database on startup.
    """
    init_db()
    print("Database initialized.")

@app.get("/", response_class=HTTPResponse)
def index(request: Request):
    """
    Render the index page.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("api/todo")
def getItems(session: Session = Depends(db_session)):
    """
    Get all todo items.
    """
    items = session.query(TodoItem).all()
    return items

@app.post("/api/todo")
def addItem(item: ItemSchema, session: Session = Depends(db_session)):
    """
    Add a new todo item.
    """
    item = TodoItem(task=item.task)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@app.patch("/api/todo/{id}")
def update_item(id: int, item: ItemSchema, session: Session = Depends(db_session)):
    """
    Update an existing todo item.
    """
    todoitem = session.query(TodoItem).get(id)
    if todoitem:
        todoitem.task = item.task
        session.commit()
        session.close()
        response = json.dumps({"msg": "Item has been updated."})
        return Response(content=response, media_type='application/json', status_code=200)
    else:
        response = json.dumps({"msg": "Item not found"})
        return Response(content=response, media_type='application/json', status_code=404)
    
@app.delete("/api/todo/{id}")
def delete_item(id: int, session: Session = Depends(db_session)):
    """
    Delete a todo item.
    """
    todoitem = session.query(TodoItem).get(id)
    if todoitem:
        session.delete(todoitem)
        session.commit()
        response = json.dumps({"msg": "Item has been deleted."})
        return Response(content=response, media_type='application/json', status_code=200)
    else:
        response = json.dumps({"msg": "Item not found"})
        return Response(content=response, media_type='application/json', status_code=404)