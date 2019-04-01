import numpy as np
import cv2
import easygui
import time

# import os
# import glob

# files = glob.glob('/YOUR/PATH/*')
# for f in files:
#     os.remove(f)
# no need to delete image, already being replaced, just added for testing purposes
camID = int(open('resources/cam.txt').read())
cap = cv2.VideoCapture(camID) # video capture source camera (Here webcam of laptop) 
ret,frame = cap.read() # return a single frame in variable `frame`

easygui.msgbox("When ready, please press 's' to take and save picture.")

while(True):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    cv2.imshow('frame', rgb)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        out = cv2.imwrite('picsNow/picsNow.jpg', frame)
        print("Picture saved.")
        print("Detecting faces...")
        time.sleep(1)
        break

cap.release()
cv2.destroyAllWindows()