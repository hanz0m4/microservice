from fastapi import FastAPI
import models, dependencies
from database import engine


app = FastAPI()


models.Base.metadata.create_all(bind=engine)
app.include_router(dependencies.router)
