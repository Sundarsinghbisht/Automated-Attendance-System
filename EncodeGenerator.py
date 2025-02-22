import cv2
import face_recognition
import pickle
import os 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("D:\\Programming\\PYTHON\\PROJECT\\AAS\\serviceAccKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' :"https://attendance-systemaas-default-rtdb.firebaseio.com/",
    'storageBucket':"attendance-systemaas.appspot.com"
})
folderPath = 'D:\Programming\PYTHON\PROJECT\AAS\Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentIds.append(os.path.splitext(path)[0])
    
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


def findEncodings(imageList):
    encodeList = []
    for img in imageList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    
    return encodeList

print('Encoding started.....')
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIDs = [encodeListKnown,studentIds]
print('Encoding completed.....')

file = open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownWithIDs,file)
file.close()
print('file saved')