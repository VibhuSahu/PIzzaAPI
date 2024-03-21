from typing import Union
from fastapi import FastAPI
import sys

from auth_routes import auth_router
from order_routes import order_router





app = FastAPI()


app.include_router(auth_router)
app.include_router(order_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q} 