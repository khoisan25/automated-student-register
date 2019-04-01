import cognitive_face as CF
import sys
import os, time
from global_variables import personGroupId
import urllib
import sqlite3
import cv2
from PIL import Image

print("connecting api to server...")
Key = str(open('resources/APIkey.txt').read().strip())
CF.Key.set(Key)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  
CF.BaseUrl.set(BASE_URL)

#file id set
fileID = (open('resources/temp.txt').read().strip())[-12:]

print("getting person id...")
def get_person_id():
	person_id = ''

    #str(sys.argv[1])[-4:]
	extractId = fileID[-4:]
	connect = sqlite3.connect("Face-DataBase")
	c = connect.cursor()
	cmd = "SELECT * FROM Students WHERE ID = " + extractId
	c.execute(cmd)
	row = c.fetchone()
	person_id = row[3]
	connect.close()
	return person_id
print("extracting directories...")
if len(sys.argv) is 1:
    currentDir = os.path.dirname(os.path.abspath(__file__))
    imageFolder = os.path.join(currentDir, "dataset/" + fileID)
    #print(imageFolder)
    person_id = get_person_id()
    try:
       for filename in os.listdir(imageFolder):
            if filename.endswith(".jpg"):
                print(filename)
                imagepath = os.path.join(imageFolder, filename)
                print(imagepath)
                #imgurl = urllib.pathname2url(os.path.join(imageFolder, filename))

                #redundant code, was trying to parse the url but did not work i decided use the image path instead, took me 2 whole days to figure this out. okay move on the GUI now, need to present it tom Mr Dickie tomorrow
                #i know this comment is a bit redundant but a, just excited that i fiured this out thats why i am writing this 
                imgurl = imagepath
                #print(imageFolder)
                #print(imgurl)
                print("detecting faces...")
                DetectFace = CF.face.detect(imgurl)
                if len(DetectFace) != 1:
            		print "No face detected in image"
                else:
            		DetectFace = CF.person.add_face(imgurl, personGroupId, person_id)
            		print(DetectFace)

    except CF.util.CognitiveFaceException:
        print("Number of face detection limit reached")
                    	
            #remember to clear text file 
            
    open('resources/temp.txt', 'w').close()
    time.sleep(2)
