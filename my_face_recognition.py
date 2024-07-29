import cv2
import cvzone
import face_recognition
import os
import pickle
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Attendance
from dotenv import load_dotenv
import os
import sys
import numpy as np
import datetime


#load_dotenv()

"""
if getattr(sys, 'frozen', False):
    # If frozen, use the directory containing the executable
    current_dir = os.path.dirname(sys.executable)
else:
    # If not frozen, use the directory containing the script
    current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the Images directory
images_dir = os.path.join(current_dir, 'Images')


image_files = [
    "Bill_Gates_photo.jpg",
    "Daniel_Otchere.jpg",
    "Magnus_Tetteh.jpg",
    "Marvin_Selasi.jpg"
]

for image_file in image_files:
    image_path = os.path.join(images_dir, image_file)
    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to load image: {image_path}")
    else:
        print(f"Successfully loaded image: {image_path}")

"""
#engine = create_engine(os.environ.get('DATABASE_URL'))
engine = create_engine('mysql+mysqldb://root:windowsql@localhost:3306/class_attendance_system_v2')
Session = sessionmaker(bind=engine)
session = Session()

img_list = []
ids = []

current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"current_dir: {current_dir}")
#Get paths from the database
for id, image_url in session.query(Student.id, Student.image_url):
    image_path = os.path.join(current_dir, image_url)
    print(f"Loading image from {image_path}")
    img = cv2.imread(image_path)
    if img is not None:
        img_list.append(img)
        ids.append(id)
    else:
        print(f"Failed to load image from database: {image_path}")

"""
#Encodes images
print("Encoding Begins...")
encode_list = []
for img in img_list:
    # Convert from BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    try:
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    except IndexError as e:
        print(f"Encoding failed for image: {img}, error: {e}")

encode_list_known_ids = [encode_list, ids]
print("Encoding Complete")

# Saving encoding to pickle file
pickle_file_path = os.path.join(current_dir, "EncodeFile.p")
with open("EncodeFile.p", mode='wb') as file:
    pickle.dump(encode_list_known_ids, file)
    print("File Saved")

"""

# loads encoding file
print("Loading encoded file...")
with open("EncodeFile.p", mode='rb') as file:
    encode_list_known_ids = pickle.load(file)

# unpacking 
encode_list_known, ids = encode_list_known_ids
print("Loading completed")

# Capture video for attendance
capture = cv2.VideoCapture(0)
initial_time = datetime.datetime.now()
while ((datetime.datetime.now() - initial_time) < datetime.timedelta(seconds=20)):
    success, img = capture.read()
    if not success:
        print("Failed to capture image from camera")
        continue

    img_small = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)

    # Getting encoding of faces
    curr_frame = face_recognition.face_locations(img_small)
    encode_curr_frame = face_recognition.face_encodings(img_small, curr_frame)
    for encode_face, face_loc in zip(encode_curr_frame, curr_frame):
        print(len(curr_frame))
        face_distance = face_recognition.face_distance(encode_list_known, encode_face)
        print("face_distance: ", face_distance)
        min_index = np.argmin(face_distance)
        print("min_index: ", min_index)

        if face_distance[min_index] < 0.47:  
            """The assumption here is that the index is always id - 1"""
            student_id = ids[min_index]
            print(f"Student with id {student_id} is present")

            y1, x2, y2, x1 = face_loc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = x1, y1, x2 - x1, y2 - y1
            cvzone.cornerRect(img, bbox)
            
            #update database
            attendance = Attendance(
                date=datetime.date.today(), time=datetime.datetime.now(), student_id=student_id
                )
            session.add(attendance)
            session.commit()
        else:
            print("Face distance too high, not updating the database")
    

    cv2.imshow("Attendance", img)
    cv2.waitKey(1)


capture.release()
cv2.destroyAllWindows()
session.close()