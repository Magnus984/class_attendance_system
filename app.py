"""Module for backend routes and logic"""
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine, and_, select
from sqlalchemy.orm import sessionmaker
from utility.db_models import Lecturer, Attendance, Course, lecturer_courses, registered_courses, Student


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
    if request.method == 'POST':
        email = request.form['Username']
        password = request.form['password']
        print('email= ', email)
        print('password= ', password)
        if not email and not password:
            flash('Please enter email and password.', 'warning')
            return redirect(url_for('login'))
        lecturer = session.query(Lecturer).filter(Lecturer.email == email).first()
        if lecturer and check_password_hash(lecturer.password, password):
            login_user(lecturer)
            flash('login successfull', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email/password', 'success')
    return render_template('login.html')


@app.route('/forgot-password', methods=['GET', 'POST'], strict_slashes=False)
def forgot_password():
    if request.method == 'POST':
        form_email = request.form['change-password']
        email_list = session.query(Lecturer.email).all()
        for i in range(len(email_list)):
            if email_list[i][0] == form_email:
                """
                I'll do this instead, an email will be sent instead
                of the redirection.
                """
                return redirect(url_for('change_password'))
        else:    
            flash('Invalid email', 'error')
    return render_template('forgot_password.html')


@app.route('/change-password', methods=['GET', 'POST'], strict_slashes=False)
def change_password():

    return render_template('change_password.html')


@app.route('/dashboard', methods=['GET'], strict_slashes=False)
@login_required
def dashboard():
    lecturer = current_user
    #get the name of the lecturer to display
    first_name, last_name = lecturer.first_name, lecturer.last_name
    print("first_name: ", first_name)
    print("last_name: ", last_name)
    context = {
        'first_name': first_name,
        'last_name': last_name 
    }
    return render_template('dashboard.html', context=context)

@app.route('/check-attendance', methods=['GET', 'POST'], strict_slashes=False)
def check_attendance():
    lecturer = current_user
    first_name, last_name = lecturer.first_name, lecturer.last_name
    if request.method == 'POST':
        date = request.form['date']
        start_time = request.form['start-time']
        end_time = request.form['end-time']
        course_code =request.form['course-code']
        student_id =  request.form['studentID']

        # Check if the provided course code is valid and associated with the lecturer
        course = session.query(Course).filter_by(course_code=course_code).first()

        if not course:
            flash('Invalid course code', 'error')
            print("Invalid course code")
            return redirect(url_for('check_attendance'))
        if not session.query(lecturer_courses).filter_by(
            lecturer_id=lecturer.id, course_id=course.id
            ).first():
            flash('You are not assigned to this course', 'error')
            print("You are not assigned to this course")
            return redirect(url_for('check_attendance'))

        try:
            #Validating student_id if any is provided
            if student_id:
                student_id = int(student_id)
        except ValueError:
            flash('Invalid student ID', 'error')
            return redirect(url_for('check_attendance'))

        attendance = session.query(Attendance, Student, Course)\
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
            reg_courses = session.execute(
                select(registered_courses.c.course_id).where(registered_courses.c.student_id == student_id)
            )
            course_list = [row[0] for row in reg_courses]
            if course.id not in course_list:
                flash("Student hasn't registered your course", 'info')
                return redirect(url_for('check_attendance'))
            attendance = attendance.filter(Attendance.student_id == student_id)
        else:
            attendance = attendance.all()
        
        if not attendance:
            flash('No attendance records found', 'error')
            return redirect(url_for('check_attendance'))
            
        return render_template(
            'display_results.html',
            attendance=attendance,
            first_name=first_name,
            last_name=last_name
            )
    return render_template(
        'check_attendance.html',
        first_name=first_name,
        last_name=last_name
        )

@app.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
def profile():
    return render_template('profile_page.html')

@app.route('/print-attendance', methods=['GET', 'POST'], strict_slashes=False)
def print_attendance():
    return render_template('display_results.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)