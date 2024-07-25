from models import Student, Lecturer, Course, registered_courses, lecturer_courses
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.environ.get('DATABASE_URL'))
Session = sessionmaker(bind=engine)
session = Session()


session.add_all([
    Student(
        first_name="Magnus", last_name="Tetteh", email="mt@gmail.com", programme="Computer Engineering" , index_number= 3040621, address="Brunei" , phone=245612314 , image_url="../Images/Magnus_Tetteh.jpg"
    ),
    Student(
        first_name="Daniel", last_name="Otchere", email="Do@gmail.com", programme="Computer Engineering" , index_number=3045223 , address="Ayeduase" , phone=552647894 , image_url="../Images/Daniel_Otchere.jpg"
    ),
    Student(
        first_name="Marvin", last_name="Selasi", email="Ms@gmail.com", programme="Electrical Engineering" , index_number=3145223 , address="Ayeduase" , phone=541237865 , image_url="../Images/Marvin_Selasi.jpg"
    ),
    Student(
        first_name="Bill", last_name="Gates", email="gates123@gmail.com", programme="Electrical Engineering", index_number=3045237, address="Seattle", phone=208241234, image_url="../Images/Bill_Gates_photo.jpg"
    )
])

session.add_all([
    Lecturer(
    first_name='Bob', last_name='Titan', email='nharnharyhaw984@gmail.com', phone='0506609243', address='Obuasi', password=generate_password_hash('peacock2')
    ),
    Lecturer(
    first_name='Alice', last_name='Wonderland', email='awonderland@gmail.com', phone='0557894321', address='Kumasi', password=generate_password_hash('wonder123')
    ),
    Lecturer(
    first_name='Charlie', last_name='Chaplin', email='cchaplin@gmail.com', phone='0567891234', address='Takoradi', password=generate_password_hash('chaplin123')
    ),
    Lecturer(
    first_name='David', last_name='Livingstone', email='dlivingstone@gmail.com', phone='0577890321', address='Tamale', password=generate_password_hash('explore123')
    ),
    Lecturer(
    first_name='Emily', last_name='Bronte', email='ebronte@gmail.com', phone='0587893210', address='Cape Coast', password=generate_password_hash('wuthering123')
    ),
    Lecturer(
    first_name='Frank', last_name='Sinatra', email='fsinatra@gmail.com', phone='0597812345', address='Accra', password=generate_password_hash('oldblue123')
    ),
    Lecturer(
    first_name='Benjamin', last_name='Kommey', email='nokommey2017@gmail.com', phone='0507703286', address='Knust-Kumasi', password=generate_password_hash('kommey123')
    ),
    Course(
    course_code='CSC211', course_name='Computer Organization and Architecture'
    ),
    Course(
    course_code='CSC301', course_name='Operating Systems'
    ),
    Course(
    course_code='ELE201', course_name='Circuit Theory'
    ),
    Course(
    course_code='ELE311', course_name='Digital Electronics'
    ),
    Course(
    course_code='ELE401', course_name='Control Systems'
    ),
    Course(
    course_code='COE371', course_name='Linear Electronics'
    ),
    Course(
    course_code='COE271', course_name='Semiconductor Devices'
    )
])



student1 = session.query(Student).filter(Student.id == 1).first()
student2 = session.query(Student).filter(Student.id == 2).first()
student3 = session.query(Student).filter(Student.id == 3).first()
student4 = session.query(Student).filter(Student.id == 4).first()

course1 = session.query(Course).filter(Course.id == 1).first()
course2 = session.query(Course).filter(Course.id == 2).first()
course3 = session.query(Course).filter(Course.id == 3).first()
course4 = session.query(Course).filter(Course.id == 4).first()
course5 = session.query(Course).filter(Course.id == 5).first()
course6 = session.query(Course).filter(Course.id == 6).first()
course7 = session.query(Course).filter(Course.id == 7).first()

#student with id 1
session.execute(
    registered_courses.insert().values(
        student_id=student1.id, course_id=course1.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student1.id, course_id=course2.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student1.id, course_id=course5.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student1.id, course_id=course6.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student1.id, course_id=course7.id
    )
)

#student with id 2
session.execute(
    registered_courses.insert().values(
        student_id=student2.id, course_id=course2.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student2.id, course_id=course3.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student2.id, course_id=course5.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student2.id, course_id=course6.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student2.id, course_id=course7.id
    )
)

#student with id 3
session.execute(
    registered_courses.insert().values(
        student_id=student3.id, course_id=course1.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student3.id, course_id=course5.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student3.id, course_id=course3.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student3.id, course_id=course6.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student3.id, course_id=course7.id
    )
)

#student with id 4
session.execute(
    registered_courses.insert().values(
        student_id=student4.id, course_id=course4.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student4.id, course_id=course5.id
    )
)
session.execute(
    registered_courses.insert().values(
        student_id=student4.id, course_id=course3.id
    )
)
#session.commit()

lecturer1 = session.query(Lecturer).filter(Lecturer.id == 1).first()
lecturer2 = session.query(Lecturer).filter(Lecturer.id == 2).first()
lecturer3 = session.query(Lecturer).filter(Lecturer.id == 3).first()
lecturer4 = session.query(Lecturer).filter(Lecturer.id == 4).first()
lecturer5 = session.query(Lecturer).filter(Lecturer.id == 5).first()
lecturer6 = session.query(Lecturer).filter(Lecturer.id == 6).first()
lecturer7 = session.query(Lecturer).filter(Lecturer.id == 7).first()


#lecturer with id 1
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer1.id, course_id=course1.id
    )
)
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer1.id, course_id=course2.id
    )
)

#lecturer with id 2
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer2.id, course_id=course3.id
    )
)
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer2.id, course_id=course4.id
    )
)

#lecturer with id 3
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer3.id, course_id=course3.id
    )
)
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer3.id, course_id=course5.id
    )
)

#lecturer with id 4
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer4.id, course_id=course2.id
    )
)
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer4.id, course_id=course4.id
    )
)

#lecturer with id 5
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer5.id, course_id=course3.id
    )
)
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer5.id, course_id=course4.id
    )
)

#lecturer with id 6
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer6.id, course_id=course5.id
    )
)
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer6.id, course_id=course2.id
    )
)

#lecturer with id 7
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer7.id, course_id=course6.id
    )
)
session.execute(
    lecturer_courses.insert().values(
        lecturer_id=lecturer7.id, course_id=course7.id
    )
)
session.commit()