#!/usr/bin/python3
"""Running camera"""
import cv2
import face_recognition
import MySQLdb
import numpy as np
import pickle
import utility
import datetime

# loads encoding file
print("Loading encoded file...")
with open("EncodeFile.p", mode='rb') as file:
    encode_list_known = pickle.load(file)

#print(encode_list_known_ids)
# unpacking 
#encode_list_known, ids = encode_list_known_ids
#print(encode_list_known)
#print(ids)
print("Loading completed")

capture = cv2.VideoCapture(0)
#cap.set(3, 1268)
#cap.set(4, 720)


if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            port=3306, user='root',
            passwd='windowsql',
            db='class_attendance_system'
    )
cur = db.cursor()

while (True):
    success, img = capture.read()

    img_small = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)

    # Getting encoding of faces
    curr_frame = face_recognition.face_locations(img_small)
    encode_curr_frame = face_recognition.face_encodings(img_small, curr_frame)
    for encode_face, face_loc in zip(encode_curr_frame, curr_frame):
        print(len(curr_frame))
        print("i am in the for loop")
        #matches = face_recognition.compare_faces(encode_list_known, encode_face)
        face_distance = face_recognition.face_distance(encode_list_known, encode_face)
        min_index = np.argmin(face_distance)
        """The assumption here is that the index is always id - 1"""
        student_id = min_index + 1
        print(f"Student with id {student_id} is present")
        insert_stmt1 = (
                "INSERT INTO attendance (date, time, student_id) "
                "VALUES (%s, %s, %s)"
                )
        data = (datetime.date.today(), datetime.datetime.now().time(), student_id)
        cur.execute(insert_stmt1, data)
        db.commit()
        #print("matches:", matches)
        #print("Distances:", face_distance)
    

    cv2.imshow("Attendance", img)
    cv2.waitKey(1)
    break

cur.close()
db.close()