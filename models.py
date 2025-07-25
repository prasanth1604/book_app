from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    pages = Column(Integer)
    author = Column(String)
    publisher = Column(String)
