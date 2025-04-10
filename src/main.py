from fastapi import FastAPI, Response, HTTPException, Header, Cookie, Form
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Union

# configure fastapi
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def awsome_api():
    """
    A simple API that returns a message.
    """
    return Response("Hello!")

@app.get("/Redirect")
def items():
    return RedirectResponse(url="/items/")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if item_id > 10:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "q": q}

@app.post("/login/")
def longin_usr(usr_id: str = Form(), password: str = Form()):
    return {"usr_id": usr_id, "password": password}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}