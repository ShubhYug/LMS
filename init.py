from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import db
from models import BorrowRecord, Login_data, Book, User

db = db
BorrowRecord = BorrowRecord
Login_data = Login_data
Book = Book
User = User


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes
