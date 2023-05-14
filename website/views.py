from flask import Blueprint, render_template, session

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", )
@views.route('/')
def base():
    return render_template("base.html", loggedIn= session.get('loggedIn', False))