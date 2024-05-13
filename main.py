from fastapi import FastAPI
from app.routers import endpoints
from app import database, models

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(endpoints.router, prefix="/api")