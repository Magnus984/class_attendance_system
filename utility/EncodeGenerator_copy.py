#!/usr/bin/python3
"""Defines a class for generating encodings of images 
and saving them in a pickle file"""
import cv2
import face_recognition
import os
import pickle

class EncodeGen(): 
    """Defines methods for importing images,
    getting encodings and saving them in a pickle file"""

    def __init__(self):
        """Import images from Images directory"""
        #Get paths from the database
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"current_dir: {current_dir}")
        
        folder_path = os.path.join(current_dir, '../Images')
        print(f"folder_path: {folder_path}")
        path_list = os.listdir(folder_path)
        print(f"path_list: {path_list}")
        self.__img_list = []
        self.__ids = []

        for path in path_list:
            print(os.path.join(folder_path, path))
            self.__img_list.append(cv2.imread(os.path.join(folder_path, path)))
            self.__ids.append(os.path.splitext(path)[0])

    @property
    def idList(self):
        return self.__ids
    
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