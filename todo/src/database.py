from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()

TODO_DATABASE_URL = os.getenv("TODO_DATABASE_URL")

engine = create_engine(TODO_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

