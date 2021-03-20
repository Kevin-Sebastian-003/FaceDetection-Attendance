# variables have infoInfo format, methods have info_info format
import os
import json
import cv2
import face_recognition as fr
import numpy as np
import multiprocessing
import Logger as logfile

def comparator(fileName, trainedFaces,resultQueue):
    """
    This function will compare the testimage passed as parameter
    to the available encodings and return the result.
    parameters : testImage, preloaded image, already converted
                to RGB
    return : 1. result list containing boolean value for match. 
             2. keys list containing keys of training faces
    Note : modify function to integrate display_result()
    """
    testImage = cv2.cvtColor(fr.load_image_file(fileName),cv2.COLOR_BGR2RGB)
    try:
        # get a list of lists of faces(encodings) found in the test image
        allFaces = fr.face_encodings(testImage)
        for face in allFaces:
            res = fr.compare_faces(list(trainedFaces.values()),face,0.6)
        print (res)
        
    except Exception as e:
            logfile.log_it(e)


#     # path = "images/training/"
#     # tempDirs = os.listdir(path)
#     # dirs = []
#     # for dir in tempDirs:
#     #     dirs.append(path+dir+"/")
#     # result = []
#     for dir in dirs:
#         trainedEncodingsDict = get_encoding(dir)
#         trainedEncodings = list(trainedEncodingsDict.values())
#         positive = 0
#         # using try block to avoid error in case test image face cannot be identified
#             # for each encoding in test image compare and update result list
#             for encoding in compareEncodings:
#                 res = fr.compare_faces(trainedEncodings,encoding,0.6)
#                 # for every new encoding found update the result
#                 for i in range(0,len(res)):
#                     if res[i]:
#                         positive+=1
        
#         if positive > len(trainedEncodings)*2/3:
#             # update final result only if encodings match face by atleast 2/3
#             result.append(dir.split("/")[2])
# # faceLoc = fr.face_locations(imgElon)[0]
# # encodeElon = fr.face_encodings(imgElon)[0]
# # cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
# # cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
# # cv2.imshow('Elon Musk',imgElon)
#     resultQueue.put(result)  