# main.py
from fastapi import FastAPI
from routes import items_routes 

app = FastAPI()

app.include_router(items_routes.item_router)
