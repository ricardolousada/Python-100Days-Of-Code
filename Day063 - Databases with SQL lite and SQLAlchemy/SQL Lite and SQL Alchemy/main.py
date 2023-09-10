# Created by Ricardo Lousada

import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()

sql_command = ("CREATE TABLE books"
               "(id INTEGER PRIMARY KEY,"
               "title varchar(250) NOT NULL UNIQUE,"
               "author varchar(250) NOT NULL,"
               "rating FLOAT NOT NULL)")

# cursor.execute(sql_command)

insert_book_command = "INSERT INTO books VALUES(1,'Harry Potter','J.K Rowling','9.3')"

# cursor.execute(insert_book_command)
# db.commit()


app = Flask(__name__)

##CREATE DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
# Create the extension
db = SQLAlchemy()
# initialise the app with the extension
db.init_app(app)

##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

"""
with app.app_context():
    db.create_all()

# Create a Record
with app.app_context():
    new_book = Book(id=1,title="Harry Potter", author="J.K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
"""

#read all records
with app.app_context():
    result= db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    print(all_books)
    print(type(all_books))

#read a Particular Record by Query
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

#update a particular Record By Query
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

#Upadate a record By Primary Key
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book,id)
    book_to_update.title = "Harry Potter and the Globet of Fire"
    db.session.commit()

#Delete a Particular Record By Primary Key
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book,id)
    db.session.delete(book_to_delete)
    db.session.commit()