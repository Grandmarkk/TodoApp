"""
This module defines the SQLAlchemy ORM model for the TodoItem.
It includes the database table name and the columns for the todo items.
"""

from sqlalchemy import Column, Integer, String
from .configurations import Base

class TodoItem(Base):
    __tablename__ = "todo_items"
    id = Column(Integer, primary_key=True)
    task = Column(String(256))