from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

from .database import Base




"""
emplyoees{
name 
id 
occupations/ rule
}

Attendings{
date
emplyee_id -> emplyoees.id
isinthebuilding 
}

"""

# adding database schemas and models

class Employees(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    rule = Column(String)

class Attendance(Base):
    __tablename__ = "attentance"

    id = Column(Integer, primary_key=True, index=True)
    time = Column(TIMESTAMP(timezone=True), )
    employee_id = Column(Integer, ForeignKey("employees.id"))