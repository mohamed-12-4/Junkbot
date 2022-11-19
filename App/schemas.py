from pydantic import BaseModel
from datetime import datetime 

class EmployeeOut(BaseModel):
    id: int
    #name: str
 #   rule: str
class EmployeeCreate(BaseModel):
    name: str
    rule: str

class AttendanceCreate(BaseModel):
    time: datetime

    class Config:
        orm_mode = True