# routes/items.py
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status,Query
from sqlalchemy.orm import Session
from database import get_db
from schema.items_schema import Item, ItemResponse  
from CRUD import items_CRUD
from decimal import Decimal
item_router = APIRouter(prefix="/item", tags=["Item"])

@item_router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(
    item: Item, 
    db: Session = Depends(get_db)):

    return items_CRUD.create_item(db, item)

@item_router.get("/{item_id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
def retrieve_item(item_id: int, db: Session = Depends(get_db)):
    db_item = items_CRUD.get_item(db, item_id)
    if db_item != None:
         return db_item
    return HTTPException(status_code=404, detail="Item is not available")
   

@item_router.get("/", response_model=List[ItemResponse], status_code=status.HTTP_200_OK)
def retrieve_item_with_query(
    name: str = Query(None, min_length=1 ,max_length=50),
    price: Decimal = Query(None,gt=0), 
    db: Session = Depends(get_db)):

    db_items = items_CRUD.get_items_by_query(db, item_name=name, item_price=price)
    if db_items:
        return db_items  # FastAPI will automatically serialize the list of ItemModel instances into ItemResponse
    raise HTTPException(status_code=404, detail="Item not found")


    