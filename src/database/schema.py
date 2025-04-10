from pydantic import BaseModel

class ItemSchema(BaseModel):
    """
    Schema for the Item model.
    """
    task: str
