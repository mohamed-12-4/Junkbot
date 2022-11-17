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

class Attendings(Base):
    __tablename__ = "attendings"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    emplyee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)

