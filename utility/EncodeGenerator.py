#!/usr/bin/python3
"""Defines a class for generating encodings of images 
and saving them in a pickle file"""
import cv2
import face_recognition
import os
import pickle
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student
from dotenv import load_dotenv
import os

load_dotenv()


class EncodeGen(): 
    """Defines methods for importing images,
    getting encodings and saving them in a pickle file"""


    engine = create_engine(os.environ.get('DATABASE_URL'))
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        """Import images from Images directory"""
        self.__img_list = []
        self.__ids = []

        current_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"current_dir: {current_dir}")
        #Get paths from the database
        #Retrieve url from database
        for id, image_url in self.session.query(Student.id, Student.image_url):
            print(os.path.join(current_dir, image_url))
            self.__img_list.append(cv2.imread(os.path.join(current_dir, image_url)))
            self.__ids.append(id)



    @property
    def idList(self):
        return self.__ids

    @property
    def imgList(self):
        return self.__img_list
    
    def get_encodings(self):
        """Encodes images and returns list of images encoded"""
        encode_list = []
        for img in self.__img_list:
            # Convert from BGR to RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encode_list.append(encode)

        return encode_list
    

    
    def save_to_pickle(self, encode_list_known_ids):
        """Saves encoding to a pickle file"""
        with open("EncodeFile.p", mode='wb') as file:
            pickle.dump(encode_list_known_ids, file)
        print("File Saved")