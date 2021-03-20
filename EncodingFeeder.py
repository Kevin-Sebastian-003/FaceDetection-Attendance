import os
import json
import cv2
import face_recognition as fr
import numpy as np
import multiprocessing
import Logger as logfile

def encoder(dir):
    """
    A function that encodes the training images in
    the path provided and stores it in json format.
    parameters : directory where images are stored
    return : a Dict with image names and
            128 different encodings per image.
            128 encodings are not in numpy array format
            due to restrictions on serializing data into json
    """
    fileName = "cached_encodings/" + dir.split("/")[2] + ".json"
    if os.path.isfile(fileName) != True:
        print("creating encodings for : " + dir.split("/")[2])
        files = os.listdir(dir)
        encoded = {}
        for f in files:
            # loads image
            loadedImage = cv2.cvtColor(fr.load_image_file(dir + f),cv2.COLOR_BGR2RGB)
            # using try block in case face is not detected
            try:
                # using [0] as training images should contain single faces only
                encoding = fr.face_encodings(loadedImage)[0]
                encoded[f.split(".")[0]] = list(encoding)
            except:
                logfile.log_it("Face wasn't detected : "+dir+f)
        # json file wil contain the encoded data for each usn
        fileName = "cached_encodings/" + dir.split("/")[2] + ".json"
        averageEncodings = [0] * 128
        for i in range(0,128):
            for key in encoded.keys():
                averageEncodings[i]=averageEncodings[i]+encoded[key][i]
            averageEncodings[i]=averageEncodings[i]/len(encoded.keys())
        with open(fileName, 'w') as outfile:
            json.dump(averageEncodings, outfile)
        logfile.log_it("created encoding for : " + dir.split("/")[2])

def load_encodings():
    """
    function to make a dictionary of all
    cached encodings and load it into memory.
    Otherwise each encoding comparison must be
    read from disk.
    """
    encoding = {}
    files = os.listdir("cached_encodings/" )
    for file in files:
        fileName = "cached_encodings/" + file
        # the following conversions are done as numpy array 
        # cannot be serialized and stored in json
        # format returned by json is stored in this list
        rawEncodings = []
        # usable format will be stored in the return encoding
        with open(fileName, 'r') as infile:
            rawEncodings = json.load(infile)
        # converting back to numpy array for further usage
        encoding[file.split(".")[0]] = np.array(rawEncodings)
    return encoding