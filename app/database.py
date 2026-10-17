from sqlmodel import create_engine, Session
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/db.sqlite")
engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    from app.models import EmployeeOnboarding
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)
