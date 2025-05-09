from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, ItemModel, Base, engine
from pydantic import BaseModel,Field

# Create FastAPI app
app = FastAPI()

class Item(BaseModel):
    name: str = Field(max_length=50 ,)
    description: str = Field(max_length=200)
    price: float = Field(max_digits=10,decimal_places=2)
    is_offer: bool = None 

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    is_offer: bool

    class Config:
        orm_mode = True  # important to return ORM objects


# Dependency to get db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


