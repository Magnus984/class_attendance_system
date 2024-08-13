# Class Attendance System
An automatic class attendance system that uses artificial intelligence to recognize faces.
The Ageitgey face_recognition module was utilized here

## Table of Contents
- [Background](background)
- [Project Overview](project-overview)
- [Features](features)
- [Tech Stack](tech-stack)

## Background
To wrap up my four-year BSc. Computer Engineering degree at the Kwame Nkrumah University of Science and Technology, I worked on this project together with my two partners. Attendance taking is manual in most Ghanaian Universities and this somehow has a negative effect on the learning process in these universities. This project seeks to automate the process to eliminate if not all, but some inconsistencies causing this negative effect.

## Project Overview
The class attendance system is divided into two parts. First is the face recognition application. This application is converted to a .exe file and set up on a server where it runs. Currently, it is written to use the web camera of your end device but the idea was to connect it to a cluster of installed cameras per the architecture. The faces of students are encoded and stored in a pickle file. What this application does is to detect faces when it runs, and compare these faces to the already encoded faces in the pickle file, if a face matches the attendance table in the database is updated.
Secondly, there is a web application for accessing attendance records. This application is only accessible to lecturers. One interesting thing about our system is that the two applications share a common database. This means that the attendance records that are being retrieved are from the same database that was updated by the face recognition application.

## Features
### Face recognition application
- **Face Detection**
- **Face Recognition**

### Web application
- **User(lecturer) Authentication**
- **User Profile Update**
- **Filtering options**

## Tech Stack
- **Frontend**:
  - HTML, CSS, Javascript

- **Backend**:
  - Python with Flask
  - SQLAlchemy or for database interactions

- **Database**:
  - MySQL for relational data storage

- **Server and Deployment**:
  - Nginx as the proxy server
  - Gunicorn as the application server
  - Deployed on an azure virtual machine instance