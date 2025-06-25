from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    name: str
    description: Optional[str] = None
    pages: int
    author: str
    publisher: str

class BookOut(BookCreate):
    id: int

    class Config:
        orm_mode = True
