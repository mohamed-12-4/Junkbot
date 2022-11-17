from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base




"""
emplyees{
name 
id 
occupations/ rule
}

Attendings{
date
emplyee_id -> employees.id
isinthebuilding 
}

"""
class Employees(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    rule = Column(String)

class Attendings(Base):
    __tablename__ = "attendings"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    emplyee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)

