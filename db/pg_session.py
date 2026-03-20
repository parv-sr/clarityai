from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Engine

DB_URL: str = "postgresql://postgres:admin%402025@localhost:5432/clarity_ai"
engine: Engine = create_engine(DB_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)