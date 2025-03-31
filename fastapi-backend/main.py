from fastapi import FastAPI
from .routers import root
from .database import create_db_and_table

app = FastAPI()

app.add_event_handler("startup",create_db_and_table)

app.include_router(root.router)
