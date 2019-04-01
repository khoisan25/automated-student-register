import os
import face_recognition

currentDir = os.path.dirname(os.path.abspath(__file__))
directory = os.path.join(currentDir, 'picsNow')
for i in range(len(os.listdir(directory))):
 	for j in range(i + 1, len(os.listdir(directory))):

 		#print os.listdir(directory)[i]

		known_image = face_recognition.load_image_file(directory +"/"+ os.listdir(directory)[i])
		unknown_image = face_recognition.load_image_file(directory +"/"+ os.listdir(directory)[j])

		try:
			known_encoding = face_recognition.face_encodings(known_image)
			unknown_encoding = face_recognition.face_encodings(unknown_image)

			results = face_recognition.compare_faces([known_encoding], unknown_encoding)
		except Exception, e:
			print "done"


# 	if filename.endswith(".jpg"):


# for i in range(len(mylist)):
#     for j in range(i + 1, len(mylist)):
#         compare(mylist[i], mylist[j])
