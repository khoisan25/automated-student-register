import sys
import cognitive_face as CF
from global_variables import personGroupId
import sqlite3

#student id i stored in terminal
print("opening temp file...")
fileID = (open('resources/temp.txt').read().strip())[-12:]
print("connecting API to server")
#confirm api key with server 
Key = str(open('resources/APIkey.txt').read().strip())
CF.Key.set(Key)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  
CF.BaseUrl.set(BASE_URL)

#need 2 arguments for terminal, remeber stored temp variable. ask sammer
if len(sys.argv) > 1:
    #str(sys.argv[1]) incase anything goes wring
    CreatePersonGroup = CF.person.create(personGroupId, fileID)
    print(CreatePersonGroup)

    extractId = fileID[-4:]
    print("conecting face to database...")
    connect = sqlite3.connect("Face-DataBase")
    cmd = "SELECT * FROM Students WHERE ID = " + extractId
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          # checking wheather the id exist or not
        isRecordExist = 1
    if isRecordExist == 1:                                                      # updating name and roll no
        connect.execute("UPDATE Students SET personID = ? WHERE ID = ?",(CreatePersonGroup['personId'], extractId))
    connect.commit()                                                            # commiting into the database
    connect.close()
    print "Person ID successfully added to the database"