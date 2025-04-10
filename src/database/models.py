from sqlalchemy import Column, Integer, String
from .configurations import Base

class TodoItem(Base):
    __tablename__ = "todo_items"
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String(256), index=True)