from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Engine
import os

DB_URL: str = os.getenv("DB_URL")
engine: Engine = create_engine(DB_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)