import cv2                                                                      # openCV
import numpy as np                                                              # for numpy arrays
import sqlite3
import dlib
import os                                                                       # for creating folders

#import sys for arguments as part of tkinter implementation

import sys

#database values 
#ID
#Name
#Roll==Student_Number
#personID
#Form
#House
#Student_Number

##################################
#funtion used to delete empty pictures, got fromg github

def getemptyfiles(rootdir):
    for root, dirs, files in os.walk(rootdir):
        for d in ['RECYCLER', 'RECYCLED']:
            if d in dirs:
                dirs.remove(d)

        for f in files:
            fullname = os.path.join(root, f)
            try:
                if os.path.getsize(fullname) == 0:
                    print fullname
                    os.remove(fullname)
            except WindowsError:
                continue

camID = int(open('resources/cam.txt').read())
cap = cv2.VideoCapture(camID)

detector = dlib.get_frontal_face_detector()

def insertOrUpdate(Id, Name, Student_Number, Form, House) :                                            # this function is for database
    connect = sqlite3.connect("Face-DataBase")                                  # connecting to the database
    cmd = "SELECT * FROM Students WHERE ID = " + Id                             # selecting the row of an id into consideration
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          # checking wheather the id exist or not
        isRecordExist = 1
    if isRecordExist == 1:                                                      # updating name and roll no
        connect.execute("UPDATE Students SET Name = ? WHERE ID = ?",(Name, Id))
        connect.execute("UPDATE Students SET StudentNumber = ? WHERE ID = ?",(Student_Number, Id))
        connect.execute("UPDATE Students SET Form = ? WHERE ID = ?",(Form, Id))
        connect.execute("UPDATE Students SET House = ? WHERE ID = ?",(House, Id))
    else:
    	params = (Id, Name, Student_Number, Form, House)                                               # insering a new student data
    	connect.execute("INSERT INTO Students(ID, Name, StudentNumber, Form, House) VALUES(?, ?, ?, ?, ?)", params)
    connect.commit()                                                            # commiting into the database
    connect.close()                                                             # closing the connection
if len(sys.argv)<3:
    name = raw_input("Enter student's name : ")
    studentidnumber = raw_input("Enter student's 4 digit ID Number : ")
    form = raw_input("Enter student's Form : ")
    studenthouse = raw_input("Enter student's School House : ")
else: 
    name = sys.argv[1]
    studentidnumber = sys.argv[2]
    form = sys.argv[3]
    studenthouse = sys.argv[4]

Id = studentidnumber.strip()


insertOrUpdate(Id, name, studentidnumber, form, studenthouse)                                                  # calling the sqlite3 database


folderName = "Students" + Id                                                        # creating the person or user folder
folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dataset/"+folderName)
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

sampleNum = 0
while(True):
    ret, img = cap.read()                                                       # reading the camera input
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converting to GrayScale
    dets = detector(img, 1)
    for i, d in enumerate(dets):                                                # loop will run for each face detected
        sampleNum += 1
        cv2.imwrite(folderPath + "/User" + Id + str(sampleNum) + ".jpg",
                    img[d.top():d.bottom(), d.left():d.right()])                                                # Saving the faces
        cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2) # ID_Numbering the rectangle
        cv2.waitKey(200)                                                        # waiting time of 200 milisecond, might need to adjust time, make it a while loop
    cv2.imshow('frame', img)                                                    # showing the video input from camera on window
    cv2.waitKey(1)
    if(sampleNum >= 20):                                                        # will take 20 faces
        break
    ##############

    #happened that the cv2 cap was taking empty files, implementation to remove them
    print("clearing empty files...")
    emptyfilepatrol = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dataset/")
    getemptyfiles(emptyfilepatrol)
    #assign id to blank file
    print("saving id in temp file...")
    open('resources/temp.txt', 'w').close()
    with open("resources/temp.txt", "a") as temp:
        temp.write(folderName)
    print("Done...")
cap.release()                                                                   # turning the webcam off
cv2.destroyAllWindows()                                                         # Closing all the opened windows

