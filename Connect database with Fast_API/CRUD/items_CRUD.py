# crud.py
from sqlalchemy.orm import Session
from models.items_models import ItemModel
from schema.items_schema import Item  # Import from models.py
from decimal import Decimal

def get_item(db: Session, item_id: int):
    return db.query(ItemModel).filter(ItemModel.id == item_id).first()

def create_item(db: Session, item: Item):
    db_item = ItemModel(
        name=item.name,
        description=item.description,
        price=item.price,
        is_offer=item.is_offer
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items_by_query(db: Session, item_name: str = None, item_price: Decimal = None):
    if item_name is not None:
        db_item = db.query(ItemModel).filter(ItemModel.name == item_name).first()
        return [db_item] if db_item else []  # Wrap in a list to return in the correct format

    if item_price is not None:
        db_items = db.query(ItemModel).filter(ItemModel.price > item_price).all()
        return db_items  # Return list of ItemModel
    
    if (item_name is None ) and (item_price is None) :
        db_items = db.query(ItemModel).all() 
        return db_items
    return []  # Return empty list if no parameters match

    
