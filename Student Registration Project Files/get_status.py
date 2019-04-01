import cognitive_face as CF
from global_variables import personGroupId

print("Registering API key on server...")
Key = str(open('resources/APIkey.txt').read().strip())
CF.Key.set(Key)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  
CF.BaseUrl.set(BASE_URL)

print("Collecting status...")
response = CF.person_group.get_status(personGroupId)
print response
print("person successfully added to database, you can now begin regsitering")





#database values 
#ID

#Name

#Roll==Student_Number==Year==ID_Number

#personID

#Form

#House




#   id,name,stu,form,house

#temp storage,remeber to remove 