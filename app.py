"""Module for backend routes and logic"""
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utility.db_models import Lecturer


app = Flask(__name__)
engine = create_engine("mysql+mysqldb://root:windowsql@localhost:3306/class_attendance_system_v2")
Session = sessionmaker(bind=engine)
session = Session()


def valid_login(email, password):
    """
    Check the email and password against 
    email and password fields in user model
    """
    lecturer = session.query(Lecturer).filter(Lecturer.email == email).first()
    if lecturer and check_password_hash(lecturer.password_hash, password):
        return True
    else:
        return False

@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Login logic"""
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if valid_login(email, password):
            redirect(url_for('check_attendance'))
        else:
            error = "Invalid username/password"
    return render_template('login.html', error=error)

@app.route('/check-attendance', methods=['GET', 'POST'], strict_slashes=False)
def check_attendance():
    pass

@app.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
def profile():
    pass

@app.route('/print-attendance', methods=['GET', 'POST'], strict_slashes=False)
def print_attendance():
    pass
