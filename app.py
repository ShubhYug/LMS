from werkzeug.security import check_password_hash
from flask import Flask, render_template, request, redirect, url_for, session
from models import BorrowRecord, Login_data, Book, User
from db import app,db
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check():
    return render_template('check.html')

#creat data
@app.route('/create_user_data', methods=['GET', 'POST'])
def create_user_data():    

    if request.method == 'POST':
        try:        
            print(request.form['first_name'])
            first_name = request.form['first_name']
            print(request.form['first_name'])
            last_name = request.form['last_name']
            print(request.form['last_name'])
            email = request.form['email']
            print(request.form['email'])
            password = request.form['password']
            print(request.form['password'])
            phone = request.form['phone']
            print(request.form['phone'])
            gender = request.form['gender']
            print(request.form['gender'])
            address = request.form['address']
            print(request.form['address'])
            country = request.form['country']
            print(request.form['country'])

            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                gender=gender,
                country=country,
                phone=phone,
                address=address
               
            )
            db.session.add(user)
            db.session.commit()
            
            return redirect('/')
        except Exception as e:
            return "An error occurred: " + str(e)
        
    if request.method == 'GET':
        return render_template('create_user_data.html')



@app.route('/book_update/<int:id>', methods=['GET','POST'])
def book_update(id):
    # breakpoint()
    # user = Book.query.get_or_404(id)
    user = Book.query.get(id)
    print(user,"===",id)
    if request.method == 'POST':
        user.title = request.form['title']
        # user.title = request.form['title']
        user.author = request.form['author_name']
        user.status = request.form['status']

        db.session.commit()
        return redirect('/show_book_data')

    return render_template('book_update.html', user = user)


#delete data
@app.route('/book_delete/<int:id>', methods=['POST'])
def book_delete(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect('/show_book_data')


#add book data
@app.route('/add_book_data', methods=['GET', 'POST'])
def add_book_data():
    if request.method == 'POST':
        try:
            title = request.form['title']
            author = request.form['author_name']
            status = request.form['status']

            book = Book(
                title = title,
                author = author,
                status = status
            )
            db.session.add(book)
            db.session.commit()
            
            return redirect('/')
        except Exception as e:
            return "An error occurred: " + str(e)
        
    if request.method == 'GET':
        return render_template('add_book_data.html')

#show books data 
@app.route('/show_book_data', methods=['GET'])
def display_students():
    show_book = Book.query.all()
    return render_template('show_book_data.html', show_book=show_book)



#login authentication

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(email = username).first()

        if user and(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard',username = username))

    return render_template('login.html')

@app.route('/dashboard/<username>/')
def dashboard(username):
    if 'user_id' in session:
        print(username)
        # return redirect(url_for('index',username = username))
        return redirect(url_for('index'))
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True,port=5001)


#update data
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update_book(id):
#     user = User.query.get(id)
#     print(user)
#     print('--------------------------------------------')
#     # if request.method == 'POST':
#     #     user.title = request.form['title']
#     #     user.author = request.form['author_name']
#     #     user.status = request.form['status']


#     #     db.session.commit()
#         # return redirect('/add_book_data')
#     return render_template('book_update.html')
#     # return render_template('book_update.html', user = user)