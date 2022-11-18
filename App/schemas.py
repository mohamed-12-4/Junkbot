from pydantic import BaseModel
from datetime import datetime 
class EmployeeCreate(BaseModel):
    name: str
    rule: str

class AttendingCreate(BaseModel):
    employee_id: int
    date: datetime