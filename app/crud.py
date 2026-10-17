from typing import List, Optional
from sqlmodel import select
from app.models import EmployeeOnboarding
from app.database import get_session

def create_employee(employee: EmployeeOnboarding) -> EmployeeOnboarding:
    with get_session() as session:
        session.add(employee)
        session.commit()
        session.refresh(employee)
        return employee

def get_employee(employee_id: int) -> Optional[EmployeeOnboarding]:
    with get_session() as session:
        statement = select(EmployeeOnboarding).where(EmployeeOnboarding.id == employee_id)
        result = session.exec(statement).one_or_none()
        return result

def list_employees(limit: int = 100) -> List[EmployeeOnboarding]:
    with get_session() as session:
        statement = select(EmployeeOnboarding).limit(limit)
        return session.exec(statement).all()
