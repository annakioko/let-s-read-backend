from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
import re

db = SQLAlchemy()

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)

    # Foreign Key
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
   
    # Relationship with book
    book = db.relationship('Book', back_populates='reviews')

    @validates('description')
    def validate_description(self, key, description):
        if not 5 <= len(description) <= 100:
            raise ValueError("Description must be between 5 and 100 characters.")
        return description

    def __repr__(self):
        return f"<Review {self.id}, {self.description}>"

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books' 
   
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    # Relationship with reviews
    reviews = db.relationship('Review', back_populates='book')

    def __repr__(self):
        return f"<Book {self.title}, {self.author}, {self.year}, {self.description}>"
