from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def route_read():
    return{"message": "Hello"}

@app.get("/items/{item-id}")
def route_two(item_id: int, q: Optional[str]= None):
    return{"item_id": item_id, "q": q}