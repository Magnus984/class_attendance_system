from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_user, login_required
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine, and_, select, update, func
from sqlalchemy.orm import sessionmaker
from models import Lecturer, Attendance, Course, lecturer_courses, registered_courses, Student
import re
import secrets
import logging
import smtplib
import time
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

engine = create_engine(os.environ.get('DATABASE_URL'))
Session = sessionmaker(bind=engine)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    session = Session()  # Create a new session
    try:
        user = session.query(Lecturer).get(user_id)
    finally:
        session.close()  # Close the session
    return user

def valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(email_regex, email))

def valid_phone(number):
    return len(number) == 10

def generate_token():
    return secrets.token_urlsafe(16)

logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Login logic"""
    if request.method == 'POST':
        email = request.form['Username']
        password = request.form['password']
        if not email or not password:
            flash('Please enter email and password.', 'warning')
            return redirect(url_for('login'))
        session = Session()  # Create a new session
        try:
            lecturer = session.query(Lecturer).filter(Lecturer.email == email).first()
            if lecturer and check_password_hash(lecturer.password, password):
                login_user(lecturer)
                flash('Login successful', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid email/password', 'error')
        except Exception as e:
            session.rollback()
            logging.error(f"Error during login: {e}")
            flash('An error occurred. Please try again later.', 'error')
        finally:
            session.close()  # Close the session
    return render_template('login.html')

@app.route('/forgot-password', methods=['GET', 'POST'], strict_slashes=False)
def forgot_password():
    if request.method == 'POST':
        form_email = request.form['change-password']
        if not valid_email(form_email):
            flash('Invalid email', 'error')
            return redirect(url_for('forgot_password'))
        session = Session()  # Create a new session
        try:
            lecturer = session.query(Lecturer).filter_by(email=form_email).first()
            if not lecturer:
                flash('Make sure email has been registered', 'info')
                return redirect(url_for('forgot_password'))

            token = generate_token()
            uid = lecturer.id
            reset_url = "{}://{}/change-password/{}/{}/".format(
                request.scheme, request.host, uid, token
            )
            msg = Message(
                'Password Reset Request',
                sender='CAS admin tettehmagnus35@gmail.com',
                recipients=[form_email]
            )
            msg.body = f"""
            We received a request to reset the password for your account.
            You can reset your password by clicking on the link below:

            {reset_url}

            If you did not request a password reset, please ignore this email.
            """
            start_time = time.time()
            mail.send(msg)
            end_time = time.time()
            logging.debug(f"Email sent to {form_email} in {end_time - start_time:.2f} seconds")
            flash('An email has been sent with instructions to reset your password.', 'success')
        except smtplib.SMTPException as e:
            logging.error(f"Error sending email: {e}")
            flash('There was an error sending the email. Please try again later.', 'error')
        finally:
            session.close()  # Close the session
        return redirect(url_for('login'))
    return render_template('forgot_password.html')

@app.route('/change-password/<int:uid>/<token>/', methods=['GET', 'POST'], strict_slashes=False)
def change_password(uid, token):
    if request.method == 'POST':
        new_password = request.form['NewPassword']
        confirm_password = request.form['ConfirmPassword']

        if new_password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('change_password', uid=uid, token=token))
        if len(new_password) < 8:
            flash('Passwords should be at least 8 characters long', 'error')
            return redirect(url_for('change_password', uid=uid, token=token))

        session = Session()  # Create a new session
        try:
            lecturer = session.query(Lecturer).filter_by(id=uid).first()
            if not lecturer:
                flash('Invalid user', 'error')
                return redirect(url_for('forgot_password'))

            if check_password_hash(lecturer.password, new_password):
                flash('New password should not be similar to the old one', 'error')
                return redirect(url_for('change_password', uid=uid, token=token))

            lecturer.password = generate_password_hash(new_password)
            session.commit()
            flash('Your password has been updated!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            session.rollback()
            logging.error(f"Error changing password: {e}")
            flash('An error occurred. Please try again later.', 'error')
        finally:
            session.close()  # Close the session
    return render_template('change_password.html')

@app.route('/dashboard', methods=['GET'], strict_slashes=False)
@login_required
def dashboard():
    lecturer = current_user
    first_name, last_name = lecturer.first_name, lecturer.last_name
    context = {
        'first_name': first_name,
        'last_name': last_name
    }
    return render_template('dashboard.html', context=context)

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def parse_time(time_str):
    try:
        return datetime.strptime(time_str, "%H:%M:%S").time()
    except ValueError:
        raise ValueError("Invalid time format. Please use HH:MM:SS.")

@app.route('/check-attendance', methods=['GET', 'POST'], strict_slashes=False)
def check_attendance():
    lecturer = current_user
    first_name, last_name = lecturer.first_name, lecturer.last_name
    if request.method == 'POST':
        date = request.form['date']
        start_time = request.form['start-time']
        end_time = request.form['end-time']
        course_code = request.form['course-code']
        student_id = request.form['studentID']

        try:
            valid_date = parse_date(date)
            print(f"Valid date: {valid_date}")
        except ValueError as e:
            flash(str(e), 'error')
            return redirect(url_for('check_attendance'))

        try:
            valid_start_time = parse_time(start_time)
            print(f"Valid time: {valid_start_time}")
        except ValueError as e:
            flash(str(e), 'error')
            return redirect(url_for('check_attendance'))

        try:
            valid_end_time = parse_time(end_time)
            print(f"Valid time: {valid_end_time}")
        except ValueError as e:
            flash(str(e), 'error')
            return redirect(url_for('check_attendance'))

        session = Session()  # Create a new session
        try:
            course = session.query(Course).filter_by(course_code=course_code).first()
            if not course:
                flash('Invalid course code', 'error')
                return redirect(url_for('check_attendance'))
            if not session.query(lecturer_courses).filter_by(
                lecturer_id=lecturer.id, course_id=course.id
            ).first():
                flash('You are not assigned to this course', 'error')
                return redirect(url_for('check_attendance'))

            if student_id:
                try:
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

                reg_courses = session.execute(
                    select(registered_courses.c.course_id).where(registered_courses.c.student_id == student_id)
                )
                course_list = [row[0] for row in reg_courses]
                if course.id not in course_list:
                    flash("Student hasn't registered your course", 'info')
                    return redirect(url_for('check_attendance'))
                attendance = attendance.filter(Attendance.student_id == student_id)
            else:
                min_time_subquery = session.query(
                    Attendance.student_id,
                    func.min(Attendance.time).label('min_time')
                ).filter(
                    Attendance.date == date,
                    Attendance.time >= start_time,
                    Attendance.time <= end_time
                ).group_by(Attendance.student_id).subquery()

                attendance = session.query(Attendance, Student, Course)\
                    .join(Attendance.student)\
                    .join(registered_courses, registered_courses.c.student_id == Attendance.student_id)\
                    .join(Course, registered_courses.c.course_id == Course.id)\
                    .join(min_time_subquery, and_(
                        Attendance.student_id == min_time_subquery.c.student_id,
                        Attendance.time == min_time_subquery.c.min_time
                    ))\
                    .filter(
                        Attendance.date == date,
                        Course.course_code == course_code
                    )
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
        except Exception as e:
            session.rollback()
            logging.error(f"Error checking attendance: {e}")
            flash('An error occurred. Please try again later.', 'error')
        finally:
            session.close()  # Close the session
    return render_template(
        'check_attendance.html',
        first_name=first_name,
        last_name=last_name
    )

@app.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
def profile():
    lecturer = current_user
    first_name, last_name, lecturer_id, lecturer_email, lecturer_address, lecturer_phone = \
        lecturer.first_name, lecturer.last_name, lecturer.id, lecturer.email, lecturer.address, lecturer.phone
    if request.method == 'POST':
        email = request.form['Email']
        address = request.form['Address']
        number = request.form['Phone']
        if not valid_email(email):
            flash('Invalid email', 'warning')
            return redirect(url_for('profile'))
        if not valid_phone(number):
            flash('Invalid phone number', 'warning')
            return redirect(url_for('profile'))
        session = Session()  # Create a new session
        try:
            lecturer = session.query(Lecturer).filter(Lecturer.id == lecturer_id).first()
            if lecturer:
                lecturer.email = email
                lecturer.address = address
                lecturer.phone = number
                session.commit()
                flash('Update successful', 'success')
                return redirect(url_for('profile'))
            else:
                flash('Update unsuccessful', 'error')
        except Exception as e:
            session.rollback()
            logging.error(f"Error updating profile: {e}")
            flash('An error occurred. Please try again later.', 'error')
        finally:
            session.close()  # Close the session
    return render_template(
        'profile_page.html',
        first_name=first_name,
        last_name=last_name,
        lecturer_id=lecturer_id,
        lecturer_email=lecturer_email,
        lecturer_address=lecturer_address,
        lecturer_phone=lecturer_phone
    )

@app.route('/print-attendance', methods=['GET', 'POST'], strict_slashes=False)
def print_attendance():
    return render_template('display_results.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
