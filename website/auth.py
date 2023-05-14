from flask import Blueprint, Flask, render_template, request, session
from pymongo import MongoClient

loggedIn = False
client = MongoClient('mongodb+srv://yuvbindal:Xww24MOIaDv7Xc3t@cluster0.xgajwdp.mongodb.net/?retryWrites=true&w=majority')
db = client['hackathon']
collection = db['login']
global USERNAME 
global PASSWORD

def check_user(username, password):
    user = collection.find_one({"username": f"{username}"})
    if user is None:
        return False
    elif user["password"] == password:
        return True
    else:
        return False
    
def get_username():
    return session.get('username', None)

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # check if user exists in the database
        user = check_user(username, password)
        if user:
            session['username'] = username

            session['LoggedIn'] =True
            USERNAME = username
            PASSWORD = password
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
        session['username'] = username


        return render_template('home.html')
    
    return render_template('sign_up.html')

def get_username_password():
    return USERNAME, PASSWORD