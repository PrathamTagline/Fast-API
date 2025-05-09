from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import status
app = FastAPI()

items_db = {}  # This will act as our fake database

@app.get("/")
def root():
    return {"message" : "hello fastapi"}     

class Items(BaseModel):
    name : str
    discription : str
    price : int
    is_offer : bool

class ItemsResponse(BaseModel):
    name :str
    discription : str




@app.get("/items/{item_id}", response_model=ItemsResponse, status_code=status.HTTP_200_OK)
def read_item(item_id: int):
    item = items_db.get(item_id)
    if item:
        return item
    return {"error": "Item not found"}, status.HTTP_404_NOT_FOUND



@app.post("/items/{item_id}", response_model=ItemsResponse, status_code=status.HTTP_201_CREATED)
def create_item(item_id: int, item: Items):
    items_db[item_id] = item
    return item

@app.put("/items/{item_id}", response_model=ItemsResponse)
def update_item(item_id: int, item: Items):
    if item_id in items_db:
        items_db[item_id] = item
        return item
    return {"error": "Item not found"}, status.HTTP_404_NOT_FOUND



@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id in items_db:
        del items_db[item_id]
        return
    return {"error": "Item not found"}, status.HTTP_404_NOT_FOUND
