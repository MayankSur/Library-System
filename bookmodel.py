from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

#Database of book avaliable
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    price = db.Column(db.Float, nullable = False)
    isbn = db.Column(db.Integer)

    def json(self):
        return {'name' : self.name,
        'price' : self.price,
        'isbn' : self.isbn}

    @staticmethod
    def add_book(_name, _price, _isbn):
        new_book = Book(name= _name, price = _price, isbn = _isbn)
        db.session.add(new_book)
        db.session.commit()

    @staticmethod
    def get_all_books():
        return [book.json() for book in Book.query.all()]

    def __repr_(self):
        book_object = {
                'name' : self.name,
                'price' : self.price,
                'isbn' : self.isbn
        }

        return json.dumps(book_object)

    @staticmethod
    def get_book(_isbn):
        return Book.json(Book.query.filter_by(isbn=_isbn).first())

    @staticmethod
    def delete_book(_isbn):
            isSuccessful = Book.query.filter_by(isbn=_isbn).delete()
            db.session.commit()
            return isSuccessful

    @staticmethod
    def update_book_price(_isbn, _price):
        bookToUpdate = Book.query.filter_by(isbn=_isbn).first()
        bookToUpdate.price = _price
        db.session.commit()

    @staticmethod
    def update_book_name(_isbn, _name):
        bookToUpdate = Book.query.filter_by(isbn=_isbn).first()
        bookToUpdate.name= _name
        db.session.commit()

    @staticmethod
    def replace_book(_isbn, _name, _price):
        bookToUpdate = Book.query.filter_by(isbn=_isbn).first()
        bookToUpdate.name= _name
        bookToUpdate.price = _price
        db.session.commit()
