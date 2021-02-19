<<<<<<< HEAD
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

#importing mages form directory

path = 'ImageData'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)

def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]  # to encode the face
        encodelist.append(encode)
    return encodelist

def markAttendance(name):
    with open('attendance.csv','r+') as f:
        myDatalist = f.readline()
        nameList = []
        for line in myDatalist:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M')
            f.writelines(f'\n{name},{dtString}')



encodeKnownList = findEncodings(images)
print('Encoding complete')

# find the matches for encoding

cap = cv2.VideoCapture(0)
while True:
    success, img =cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)  # to locate the face
    encodesCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)  # to encode the face

    for encodeFace,faceLoc in zip(encodesCurFrame,faceCurFrame):
        matches = face_recognition.compare_faces(encodeKnownList,encodeFace)
        faceDis = face_recognition.face_distance(encodeKnownList,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),2)
            markAttendance(name)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)

=======
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

#importing mages form directory

path = 'ImageData'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)

def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]  # to encode the face
        encodelist.append(encode)
    return encodelist

def markAttendance(name):
    with open('attendance.csv','r+') as f:
        myDatalist = f.readline()
        nameList = []
        for line in myDatalist:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M')
            f.writelines(f'\n{name},{dtString}')



encodeKnownList = findEncodings(images)
print('Encoding complete')

# find the matches for encoding

cap = cv2.VideoCapture(0)
while True:
    success, img =cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)  # to locate the face
    encodesCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)  # to encode the face

    for encodeFace,faceLoc in zip(encodesCurFrame,faceCurFrame):
        matches = face_recognition.compare_faces(encodeKnownList,encodeFace)
        faceDis = face_recognition.face_distance(encodeKnownList,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),2)
            markAttendance(name)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)

>>>>>>> ed1583217f4d550237f8dc19c59edbdb240fb358
