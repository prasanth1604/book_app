from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from database import SessionLocal, engine
from models import Book
from schemas import BookCreate, BookOut
from auth import get_current_user

import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=BookOut)
def create_book(book: BookCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=List[BookOut])
def get_books(author: Optional[str] = None, publisher: Optional[str] = None,
              db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    query = db.query(Book)
    if author:
        query = query.filter(Book.author == author)
    if publisher:
        query = query.filter(Book.publisher == publisher)
    return query.all()

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": f"Book {book_id} deleted successfully"}
