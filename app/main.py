from fastapi import FastAPI, HTTPException
from typing import List
from app.database import init_db
from app.models import EmployeeOnboarding
from app.crud import create_employee, get_employee, list_employees

app = FastAPI(title="Emergent APHID Onboarding API", version="0")

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/onboarding", response_model=EmployeeOnboarding)
def create_onboarding(employee: EmployeeOnboarding):
    return create_employee(employee)

@app.get("/onboarding/{employee_id}", response_model=EmployeeOnboarding)
def read_onboarding(employee_id: int):
    emp = get_employee(employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee onboarding record not found")
    return emp

@app.get("/onboarding", response_model=List[EmployeeOnboarding])
def read_onboardings():
    return list_employees()
