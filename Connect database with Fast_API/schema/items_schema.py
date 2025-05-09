# schemas.py
from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional
class Item(BaseModel):
    name: str = Field(max_length=50)
    description: str = Field(max_length=200)
    price: Decimal = Field(max_digits=10, decimal_places=2)
    is_offer: bool = None

class CategoryResponse(BaseModel):
    id : int 
    name : str

    class Config:
        orm_mode = True

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: Decimal
    is_offer: bool
    category = Optional[CategoryResponse]

    class Config:
        orm_mode = True

