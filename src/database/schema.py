"""
Database schema for the application.
This module contains the schema definitions for the database models.
It includes the Pydantic models used for data validation and serialization.
"""

from pydantic import BaseModel

class ItemSchema(BaseModel):
    """
    Schema for the Item model.
    """
    task: str
