from db import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status


class Login_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, id, username, password, email):
        id = id
        self.username = username
        self.password = password
        self.email = email

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String())
    address = db.Column(db.String())
    country = db.Column(db.String())

    def __init__(self, first_name, last_name, email, phone, password, gender, address, country):
      
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = password
        self.gender = gender
        self.address = address
        self.country = country

class BorrowRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrowed_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime)

    def __init__(self, user_id, book_id, borrowed_data, return_date):
        
        self.user_id = user_id
        self.book_id = book_id
        self.borrowed_date = borrowed_data
        self.return_date = return_date



