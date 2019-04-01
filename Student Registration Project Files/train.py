import cognitive_face as CF
from global_variables import personGroupId

Key = str(open('resources/APIkey.txt').read().strip())
CF.Key.set(Key)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  
CF.BaseUrl.set(BASE_URL)

TrainPersonGroup = CF.person_group.train(personGroupId)
print TrainPersonGroup
print("Training in progress...")
print("Finished training person group")
