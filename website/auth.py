from flask import Blueprint, Flask, render_template, request, session
from pymongo import MongoClient
loggedIn = False
client = MongoClient('mongodb+srv://yuvbindal:Xww24MOIaDv7Xc3t@cluster0.xgajwdp.mongodb.net/?retryWrites=true&w=majority')
db = client['hackathon']
collection = db['login']



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # check if user exists in the database
        user = collection.find_one({'username': username, 'password': password})
        if user:
            session['LoggedIn'] =True
            return render_template('home.html')
        else:
            return render_template('login.html', message='Invalid username or password!')
    
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        # check if user already exists in the database
        existing_user = collection.find_one({'$or': [{'username': username}, {'email': email}]})
        if existing_user:
            return render_template('sign_up.html', message='Username or email already exists!')
        
        
        # insert new user into the database
        collection.insert_one({'username': username, 'password': password, 'email': email})
        session['LoggedIn'] =True
      
        return render_template('home.html')
    
    return render_template('sign_up.html')

@auth.route('/scan')
def scan():
    return render_template('scan.html')




