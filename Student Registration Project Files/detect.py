import cv2
import dlib
import os
import sys
import sqlite3
import time


#cam = cv2.VideoCapture(1)
detector = dlib.get_frontal_face_detector()

#add caera later limkted number of rns n server, i might include it later 
#update also included test to specify image path, do not iclude it t the final project

#specify image path thats why i need two arguments
if len(sys.argv) is not 1:
	img = cv2.imread(str(sys.argv[1]))
	detections = detector(img, 1)
	if not os.path.exists('./RegisterNow'): #didnt work last time, make sure its created
		os.makedirs('./RegisterNow')
	print "detected faces = " + str(len(detections))

	#dont use it if you dont know it, should append detected faces to file
	for i, d in enumerate(detections):
   		cv2.imwrite('./RegisterNow/face' + str(i + 1) + '.jpg', img[d.top():d.bottom(), d.left():d.right()])

   	print("faces detected")
   	print("cropping faces...")
   	time.sleep(1)

   	print("faces saved.")
