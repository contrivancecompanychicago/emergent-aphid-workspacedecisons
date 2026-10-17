from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class EmployeeOnboarding(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    email: str
    position: Optional[str] = None
    status: str = "pending"
    created_at: datetime = Field(default_factory=datetime.utcnow)
