import cognitive_face as CF
from global_variables import personGroupId
import sys

Key = str(open('resources/APIkey.txt').read().strip())
CF.Key.set(Key)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  
CF.BaseUrl.set(BASE_URL)
print("connecting API to server...")
personGroups = CF.person_group.lists()

print("finding person groups...")
for personGroup in personGroups:
    if personGroupId == personGroup['personGroupId']:
        print personGroupId + " already exists."
        sys.exit()

res = CF.person_group.create(personGroupId)
print res
print("Creating person group...")
print("person group created.")