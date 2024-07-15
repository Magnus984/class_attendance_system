"""models for database"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table, create_engine, Date, Time
from sqlalchemy.orm import relationship
from flask_login import UserMixin


engine =create_engine("mysql+mysqldb://root:windowsql@localhost:3306/class_attendance_system_v2")
Base = declarative_base()

registered_courses = Table(
    "registered_courses",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("course_id", Integer, ForeignKey("courses.id"))
)

lecturer_courses = Table(
    "lecturer_courses",
    Base.metadata,
    Column("lecturer_id", Integer, ForeignKey("lecturers.id")),
    Column("course_id", Integer, ForeignKey("courses.id"))
)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(15), nullable=False)
    last_name = Column(String(15), nullable=False)
    email = Column(String(45), unique=True, nullable=False)
    programme = Column(String(45), nullable=False)
    index_number = Column(Integer, unique=True, nullable=False)
    address = Column(String(45), nullable=False)
    phone = Column(Integer, unique=True, nullable=False)
    image_url = Column(String(45), unique=True, nullable=False)
    
    attendance = relationship("Attendance", back_populates="student")
    
    course = relationship(
        "Course", secondary=registered_courses,
        back_populates="student"
    )


class Lecturer(Base, UserMixin):
    __tablename__ = 'lecturers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(15), nullable=False)
    last_name = Column(String(15), nullable=False)
    email = Column(String(45), unique=True, nullable=False)
    phone = Column(Integer, unique=True, nullable=False)
    address = Column(String(45), nullable=False)
    password = Column(String(255), nullable=False)

    course =relationship(
        "Course", secondary=lecturer_courses,
        back_populates="lecturer"
        )

class Attendance(Base):
    __tablename__ = 'attendances'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    time = Column(Time(timezone=False))
    
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship("Student", back_populates="attendance")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    course_code = Column(String(15), unique=True, nullable=False)
    course_name = Column(String(45), unique=True, nullable=False)

    student = relationship(
        "Student", secondary=registered_courses,
        back_populates="course"
    )

    lecturer = relationship(
        "Lecturer", secondary=lecturer_courses,
        back_populates="course"
    )

Base.metadata.create_all(engine)