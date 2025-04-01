from fastapi import FastAPI
from .database import create_db_and_table
from .routers import root, amenities

app = FastAPI()

app.add_event_handler("startup",create_db_and_table)

app.include_router(root.router)
app.include_router(amenities.router)
