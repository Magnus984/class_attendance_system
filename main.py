#!/usr/bin/python3
"""Running camera"""
import cv2
import face_recognition
import MySQLdb
import numpy as np
import pickle
import datetime
from utility.EncodeGenerator import EncodeGen
from models import Student, Attendance

# loads encoding file
print("Loading encoded file...")
with open("EncodeFile.p", mode='rb') as file:
    encode_list_known_ids = pickle.load(file)

# unpacking 
encode_list_known, ids = encode_list_known_ids
#print(encode_list_known)
#print(ids)
print("Loading completed")

capture = cv2.VideoCapture(0)
#cap.set(3, 1268)
#cap.set(4, 720)


while (True):
    success, img = capture.read()

    img_small = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)

    # Getting encoding of faces
    curr_frame = face_recognition.face_locations(img_small)
    encode_curr_frame = face_recognition.face_encodings(img_small, curr_frame)
    for encode_face, face_loc in zip(encode_curr_frame, curr_frame):
        print(len(curr_frame))
        #print("i am in the for loop")
        #matches = face_recognition.compare_faces(encode_list_known, encode_face)
        face_distance = face_recognition.face_distance(encode_list_known, encode_face)
        print("face_distance: ", face_distance)
        min_index = np.argmin(face_distance)
        print("min_index: ", min_index)
        """The assumption here is that the index is always id - 1"""
        student_id = ids[min_index]
        print(f"Student with id {student_id} is present")
        attendance = Attendance(
            date=datetime.date.today(), time=datetime.datetime.now(), student_id=student_id
            )
        EncodeGen.session.add(attendance)
        EncodeGen.session.commit()
        #print("matches:", matches)
        #print("Distances:", face_distance)
    

    cv2.imshow("Attendance", img)
    cv2.waitKey(1)


EncodeGen.session.close()
"""
cur.close()
db.close()
"""