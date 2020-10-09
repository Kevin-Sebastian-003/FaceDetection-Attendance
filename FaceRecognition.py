#variables have infoInfo format, methods have info_info format
import os
import json
import cv2
import face_recognition as fr
import numpy as np

def encoder():
    """
    A function that encodes the training images in
    the path provided and stores it in json format.
    This function must be modified to integrate for
    muliple training locations/databases/different
    calling modules.
    parameters : None
    return : a Dict with image names and
            128 different encodings per image.
            128 encodings are not in numpy array format
            due to restrictions on serializing data into json
    """
    path = "./images/training/"
    files = os.listdir(path)
    encoded = {}
    for f in files:
        #loads image
        loadedImage = fr.load_image_file(path + f)
        loadedImage = cv2.cvtColor(loadedImage,cv2.COLOR_BGR2RGB)
        #using try block in case face is not detected
        try:
            #using [0] as training images should contain single faces only
            encoding = fr.face_encodings(loadedImage)[0]
            encoded[f.split(".")[0]] = list(encoding)
        except:
            pass
    #json file wil contain the encoded data for each usn
    with open('cached_encodings/json.txt', 'w') as outfile:
        json.dump(encoded, outfile)
    return encoded

def get_encoding():
    """
    A function to check if json file exists and fetch the encodings.
    calls encoder() if no file is found. It also converts the json
    to usable formmat before sending to calling function
    parameters : None
    return : list of encodings ((pre)processed for formatting)
    """
    if os.path.isfile('cached_encodings/json.txt'):
        #the following conversions are done as numpy array 
        #cannot be serialized and stored in json
        #format returned by json is stored in this dict
        rawEncodings = {}
        #usable format will be stored in the this dict
        encodings = {}
        with open('cached_encodings/json.txt', 'r') as infile:
            rawEncodings = json.load(infile)
        for key in rawEncodings.keys():
            #converting back to numpy array for further usage
            encodings[key] = np.array(rawEncodings.get(key))
        return encodings
    return encoder()

def comparator(compareImage):
    """
    This function will compare the testimage passed as parameter
    to the available encodings and return the result.
    parameters : compareImage, preloaded image, already converted
                to RGB
    return : 1. result list containing boolean value for match. 
             2. keys list containing keys of training faces
    Note : modify function to integrate display_result()
    """
    trainedEncodingsDict = get_encoding()
    trainedEncodings = list(trainedEncodingsDict.values())
    result = [False]*len(trainedEncodings)
    #using try block to avoid error in case test image face cannot be identified
    try:
        # #use the following to see the image with a rectangle
        # #for multiface run it multiple times and change the index in faceloc below
        # compareImage = cv2.resize(compareImage, (0, 0), fx=0.15, fy=0.15)
        # faceLoc = fr.face_locations(compareImage)[0]
        # cv2.rectangle(compareImage,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
        # cv2.imshow('Elon Test',compareImage)
        # cv2.waitKey(0)

        #get a list of lists of faces(encodings) found in the test image
        compareEncodings = fr.face_encodings(compareImage)
        #for each encoding in test image compare and update result list
        for encoding in compareEncodings:
            res = fr.compare_faces(trainedEncodings,encoding,0.6)
            size = len(res)
            #for every new encoding found update the result
            for i in range(0,size):
                if res[i]!=result[i]:
                    result[i] = True
    except:
        print("Can't detect image")
    return result,list(trainedEncodingsDict.keys())

def display_result(result, keys):
    """
    A Function to display the faces found. This function
    is not required and should be removed. Alterrnatively
    the logic should be used in the calling function
    parameters : 1. result containing boolean values
                 2. keys containing list of values for display
    return : None
    """
    identifiedFaces = []
    size = len(keys)
    for i in range(0,size):
        if result[i]==True:
           identifiedFaces.append(keys[i])
    print("Identified Faces :" + str(identifiedFaces))

def alpha():
    """
    This is the source function and hence the name.
    All function calls must be made from here.
    Incase classes are used, make sure to retain this.
    i.e. use as a main method
    parameters : None
    return : None
    """
    path = "./images/testing/"
    testSubject = "dual_test2.jpg"
    loadedImage = fr.load_image_file(path + testSubject)
    loadedImage = cv2.cvtColor(loadedImage,cv2.COLOR_BGR2RGB)
    result, keys = comparator(loadedImage)
    display_result(result, keys)

alpha()

#the followinglines are from murtaza's workshop/facerecognitionattendance

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
# 
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

#attendance project (indentation required)
# import cv2
# import numpy as np
# import face_recognition
# import os
# from datetime import datetime
# # from PIL import ImageGrab
# 
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
# 
# def findEncodings(images):
# encodeList = []
# for img in images:
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     encode = face_recognition.face_encodings(img)[0]
#     encodeList.append(encode)
# return encodeList
# 
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
# 
# #### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# # def captureScreen(bbox=(300,300,690+300,530+300)):
# #     capScr = np.array(ImageGrab.grab(bbox))
# #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
# #     return capScr
# 
# encodeListKnown = findEncodings(images)
# print('Encoding Complete')
# 
# cap = cv2.VideoCapture(0)
# 
# while True:
# success, img = cap.read()
# #img = captureScreen()
# imgS = cv2.resize(img,(0,0),None,0.25,0.25)
# imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
# 
# facesCurFrame = face_recognition.face_locations(imgS)
# encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
# 
# for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
# matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
# faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
# #print(faceDis)
# matchIndex = np.argmin(faceDis)
# 
# if matches[matchIndex]:
# name = classNames[matchIndex].upper()
# #print(name)
# y1,x2,y2,x1 = faceLoc
# y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
# cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
# cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
# cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
# markAttendance(name)
# 
# cv2.imshow('Webcam',img)
# cv2.waitKey(1)