# models.py
from sqlalchemy import Column, Integer, Float, Boolean, String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    is_offer = Column(Boolean, default=False)
    categoty_id = Column(Integer,ForeignKey('categories.id'))  
    category = relationship('CategoryModel', back_populates='items')
class CategoryModel(Base):
    __tablename__ = "categories"

    id = Column(Integer,primary_key=True,index=True)
    category = Column(String)
    items = relationship("ItemModel",back_populates="category")