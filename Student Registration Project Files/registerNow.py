import os
import shutil
import subprocess
from easygui import *
import time


folderPath = './picsNow'
registerNow = './RegisterNow'
for image in os.listdir(folderPath):
	if os.path.exists(registerNow):
		shutil.rmtree(registerNow)
	os.makedirs(registerNow)

	cmd = ["python2", "detect.py", os.path.join(folderPath, image)]
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	p.wait()

	result = p.communicate()
	msgbox(result)
	time.sleep(2)

	cmd = ["python2", "spreadsheet.py"]
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	p.wait()

	result = p.communicate()
	msgbox(result)
	time.sleep(2)


	cmd = ["python2", "identify.py"]
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	p.wait()

	result = p.communicate()
	msgbox(result)
	time.sleep(2)






