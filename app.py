"""Module for backend routes and logic"""
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from utility.db_models import Lecturer, Attendance, Course, lecturer_courses, registered_courses


app = Flask(__name__)
app.secret_key = 'my_key'
engine = create_engine("mysql+mysqldb://root:windowsql@localhost:3306/class_attendance_system_v2")
Session = sessionmaker(bind=engine)
session = Session()


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return session.query(Lecturer).get(user_id)
"""
def valid_login(email, password):
    Check the email and password against 
    email and password fields in user model
    lecturer = session.query(Lecturer).filter(Lecturer.email == email).first()
    if lecturer and check_password_hash(lecturer.password, password):
        print("login valid")
        return True
    else:
        return False
"""

@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Login logic"""
    error = None
    if request.method == 'POST':
        email = request.form['Username']
        password = request.form['password']
        lecturer = session.query(Lecturer).filter(Lecturer.email == email).first()
        if lecturer and check_password_hash(lecturer.password, password):
            login_user(lecturer)
            print("login valid")
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid email/password"
    return render_template('login.html', error=error)


@app.route('/forgot-password', methods=['GET', 'POST'], strict_slashes=False)
def forgot_password():
    error = None
    if request.method == 'POST':
        form_email = request.form['change-password']
        email_list = session.query(Lecturer.email).all()
        for i in range(len(email_list)):
            print(email_list[i][0])
            if email_list[i][0] == form_email:
                return redirect(url_for('change_password'))
        else:    
            error = 'Invalid email'
    return render_template('forgot_password.html', error=error)


@app.route('/change-password', methods=['GET', 'POST'], strict_slashes=False)
def change_password():
    return render_template('change_password.html')


@app.route('/dashboard', methods=['GET'], strict_slashes=False)
def dashboard():
    return render_template('dashboard.html')

@app.route('/check-attendance', methods=['GET', 'POST'], strict_slashes=False)
def check_attendance():
    if request.method == 'POST':
        date = request.form['date']
        start_time = request.form['start-time']
        end_time = request.form['end-time']
        course_code =request.form['course-code']
        student_id =  request.form['student-id']

        lecturer = current_user
        # Check if the provided course code is valid and associated with the lecturer
        course = session.query(Course).filter_by(course_code=course_code).first()
        if not course:
            return render_template('check_attendance.html', error="Invalid course code")
        if not session.query(lecturer_courses).filter_by(
            lecturer_id=lecturer.id, course_id=course.id
            ).first():
            return render_template('check_attendance.html', error="You are not assigned to this course")

        try:
            #Validating student_id if any is provided
            if student_id:
                student_id = int(student_id)
        except ValueError:
            return render_template('check_attendance.html', error='Invalid student ID')

        attendance = session.query(Attendance)\
        .join(Attendance.student)\
        .join(registered_courses, registered_courses.c.student_id == Attendance.student_id)\
        .join(Course, registered_courses.c.course_id == Course.id)\
        .filter(
            Attendance.date == date, and_(
                Attendance.time >= start_time,
                Attendance.time <= end_time
            ),
            Course.course_code == course_code
        )
    
        if student_id:
            attendance = attendance.filter(Attendance.student_id.id == student_id).first()
        else:
            attendance = attendance.all()
        
        if not attendance:
            render_template('check_attendance.html', error='No attendance records found')
        return render_template('print_attendance.html', attendance=attendance)
    return render_template('check_attendance.html')

@app.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
def profile():
    pass

@app.route('/print-attendance', methods=['GET', 'POST'], strict_slashes=False)
def print_attendance():
    pass

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)