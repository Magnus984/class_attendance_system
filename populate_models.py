from utility.db_models import Student, Lecturer, Course
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+mysqldb://root:windowsql@localhost:3306/class_attendance_system_v2")
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
session.commit()