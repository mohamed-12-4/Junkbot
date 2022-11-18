from pydantic import BaseModel
from datetime import datetime 
class EmployeeCreate(BaseModel):
    name: str
    rule: str

class AttendanceCreate(BaseModel):
    employee_id: int
    time: datetime

    class Config:
        orm_mode = True