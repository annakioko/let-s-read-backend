from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
import re
from enum import Enum
from sqlalchemy import CheckConstraint

db = SQLAlchemy()


#Product model
class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String, CheckConstraint("gender IN ('Male', 'Female')"))
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    quantity_available = db.Column(db.Integer)
    image = db.Column(db.String, nullable=True)

    # relationship with category 
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category', backref='products')

    @validates('description')
    def validate_description(self, key, description):
        if not 5 <= len(description) <= 100:
           raise ValueError("Description must be between 5 and 100 characters.")
        return description
    
    def __repr__(self):
        return f"<Product {self.id}, {self.name}, {self.gender}, {self.category}, {self.description}, {self.price}>"
    

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'description': self.description,
            'price': str(self.price),  
            'quantity_available': self.quantity_available,
            'image': self.image,
            'category': self.category.serialize() if self.category else None
        }
    


#Category Model
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)


    def __repr__(self):
        return f"<Category {self.id}, {self.name}>"
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
           
        }




#class Review(db.Model, SerializerMixin):
#    __tablename__ = 'reviews'

 #   id = db.Column(db.Integer, primary_key=True)
  #  description = db.Column(db.String, nullable=False)

    # Foreign Key
   # book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
   
    # Relationship with book
    #book = db.relationship('Book', back_populates='reviews')

    #@validates('description')
    #def validate_description(self, key, description):
     #   if not 5 <= len(description) <= 100:
      #      raise ValueError("Description must be between 5 and 100 characters.")
       # return description

    #def __repr__(self):
     #   return f"<Review {self.id}, {self.description}>"

#class Book(db.Model, SerializerMixin):
 #   __tablename__ = 'books' 
   
  #  id = db.Column(db.Integer, primary_key=True)
   # title = db.Column(db.String, nullable=False)
    #author = db.Column(db.String, nullable=False)
    #year = db.Column(db.String, nullable=False)
    #description = db.Column(db.String, nullable=False)

    # Relationship with reviews
    #reviews = db.relationship('Review', back_populates='book')

    #def __repr__(self):
     #   return f"<Book {self.title}, {self.author}, {self.year}, {self.description}>"
