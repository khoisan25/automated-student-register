from easygui import *
import sys, subprocess
import time

image = "resources/logo.png"
image2 = "resources/camera.png"
msg = "                            Please pick an option below"
choices = ["Add Student","Register Students","Cancel"]
reply = buttonbox(msg, image=image, choices=choices)
if reply == "Add Student":
    msgbox("*Immediately after submiting the following form,\n please sit upright and face the camera\n\n*Press 'Ok' to continue",image=image2)
    process = subprocess.Popen(["python2", "add_student_gui.py"], stdout=subprocess.PIPE)
    process.wait()

elif reply == "Register Students":
	msgbox("Getting ready to take picture.\n please position yourself in a visible position for the picture.\n \n Click OK to take picture")
	cmd = ["python2", "takeNow.py"]
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	p.wait()

	result = p.communicate()
	msgbox(result)
	time.sleep(2)

	cmd = ["python2", "registerNow.py"]
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	p.wait()

	result = p.communicate()
	msgbox(result)
	time.sleep(2)

elif reply == "resources/logo.png":
	msgbox("Starting realtime recognition...\n Click 'OK' to continue.")
	process = subprocess.Popen(["python2", "realtimedetector.py"], stdout=subprocess.PIPE)
	process.wait()
else:
    sys.exit(0)