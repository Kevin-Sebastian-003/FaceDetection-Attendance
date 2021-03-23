import Video2Image
import FaceRecognition
import EncodingFeeder
import os
import time
import multiprocessing
import sys
import logging

os.system("./RemovePass.sh")
computationType = ["SINGLE_CORE",1]
processes = []
logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

print("Please store \ntraining video in '/videos/train/'\ntesting video in '/videos/test/'\n")
if input("Is the above conditon is met? (y/n): ") != 'y':
    sys.exit(0)
if input("Do you want to enable multi-core? (y/n): ") == "y":
        computationType[0] = "MULTI_CORE"
        computationType[1] = multiprocessing.cpu_count()
print("Starting with " + str(computationType[0]) + " running on " + str(computationType[1]) \
    + " core(s)")
startTime = time.time()

Video2Image.convert("training")
Video2Image.convert("testing")


dirs = os.listdir("images/training")
for person in dirs:
    resultQueue = multiprocessing.Queue()
    p = multiprocessing.Process(target = EncodingFeeder.encoder, args = (str("images/training/" + person + "/"),))
    processes.append(p)
    p.start()
    if computationType[1] == 1:
        p.join()
if computationType[1] > 1:
        for process in processes:
            process.join()
# A dictionary of cached encodings
trainedEncodings = EncodingFeeder.load_encodings()
encodingTime = time.time()
print("Encoding and loading it to memory took : " + str(encodingTime - startTime) + " Seconds")


path = "images/testing/"
dirs = os.listdir(path)
for dir in dirs:
    images = os.listdir(path + dir + "/")
    resultQueue = multiprocessing.Queue()
    for image in images:
        print("comparing trained encodings with test image")      
        p = multiprocessing.Process(target = FaceRecognition.comparator, 
        args = (str(path + dir + "/" + image), trainedEncodings, resultQueue, ))
        processes.append(p)
        p.start()
        if computationType[1] == 1:
            p.join()
    if computationType[1] > 1:
        for process in processes:
            process.join()
    i =0
    print("Results : ")
    while not resultQueue.empty():
        print("Identified Faces in image " + images[i] + " are : " + str(resultQueue.get()))
        i+=1


faceRecognitionTime = time.time()
print("Encoding took : " + str(faceRecognitionTime - encodingTime) + " Seconds")
endTime = time.time()
print("Task completed in " + str(endTime - startTime) + " Seconds")


















# #the followinglines are from murtaza's workshop/facerecognitionattendance

# basic 
# imgElon = fr.load_image_file('images/training/elon_musk.jpg')
# imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
# imgTest = fr.load_image_file('images/training/elon_musk.jpg')
# imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
# #------------------------------------------------------------------------
# #displays rectangle on face
# faceLoc = fr.face_locations(imgElon)[0]
# encodeElon = fr.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

# faceLocTest = fr.face_locations(imgTest)[0]
# encodeTest = fr.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)
# #------------------------------------------------------------------------
# results = fr.compare_faces([encodeElon],encodeTest)
# faceDis = fr.face_distance([encodeElon],encodeTest)
# print(results,faceDis)
# cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
# #------------------------------------------------------------------------
# cv2.imshow('Elon Musk',imgElon)
# cv2.imshow('Elon Test',imgTest)
# cv2.waitKey(0)

# attendance project (indentation required)
# import cv2
# import numpy as np
# import face_recognition
# import os
# from datetime import datetime
# # from PIL import ImageGrab

# path = 'ImagesAttendance'
# images = []
# classNames = []
# myList = os.listdir(path)
# print(myList)
# for cl in myList:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])
#     print(classNames)

# def findEncodings(images):
# encodeList = []
# for img in images:
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     encode = face_recognition.face_encodings(img)[0]
#     encodeList.append(encode)
# return encodeList

# def markAttendance(name):
# with open('Attendance.csv','r+') as f:
# myDataList = f.readlines()
# nameList = []
# for line in myDataList:
# entry = line.split(',')
# nameList.append(entry[0])
# if name not in nameList:
# now = datetime.now()
# dtString = now.strftime('%H:%M:%S')
# f.writelines(f'\n{name},{dtString}')

# #### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# # def captureScreen(bbox=(300,300,690+300,530+300)):
# #     capScr = np.array(ImageGrab.grab(bbox))
# #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
# #     return capScr

# encodeListKnown = findEncodings(images)
# print('Encoding Complete')

# cap = cv2.VideoCapture(0)

# while True:
# success, img = cap.read()
# #img = captureScreen()
# imgS = cv2.resize(img,(0,0),None,0.25,0.25)
# imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

# facesCurFrame = face_recognition.face_locations(imgS)
# encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

# for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
# matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
# faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
# #print(faceDis)
# matchIndex = np.argmin(faceDis)

# if matches[matchIndex]:
# name = classNames[matchIndex].upper()
# #print(name)
# y1,x2,y2,x1 = faceLoc
# y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
# cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
# cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
# cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
# markAttendance(name)

# cv2.imshow('Webcam',img)
# cv2.waitKey(1)