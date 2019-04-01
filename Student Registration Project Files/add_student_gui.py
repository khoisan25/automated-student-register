from easygui import *
import subprocess
import time

msg = "Enter Students information"
title = "Student registration portal"
fieldNames = ["Name","Student ID","Form","House"]
fieldValues = []  # we start with blanks for the values
fieldValues = multenterbox(msg,title, fieldNames)

# make sure that none of the fields was left blank
while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break # no problems found
    fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
# test output first print "Reply was:", fieldValues


fileID = (open('resources/temp.txt').read().strip())[-12:]
output = ""


#run python code from add studdt 

cmd = ["python2", "add_student.py", str(fieldValues[0]), str(fieldValues[1]), str(fieldValues[2]), str(fieldValues[3])]
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p.wait()

result = p.communicate()
msgbox(result)
time.sleep(2)
#################################################
cmd = ["python2", "create_person_group.py"]
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p.wait()

result = p.communicate()
msgbox(result)
time.sleep(2)
################################################
cmd = ["python2", "create_person.py", str(fileID)]
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p.wait()
result = p.communicate()

msgbox(result)
time.sleep(2)
##################################################

cmd = ["python2", "add_person_faces.py"]
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p.wait()
result = p.communicate()

msgbox(result)
time.sleep(4)

#################################################

cmd = ["python2", "train.py"]
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p.wait()
result = p.communicate()

msgbox(result)
time.sleep(2)

##################################################

cmd = ["python2", "get_status.py"]
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p.wait()
result = p.communicate()


msgbox(result)
time.sleep(2)
