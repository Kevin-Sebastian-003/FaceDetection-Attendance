# FaceDetection-Attendance
This project manages attendance using face recognition from video sources like PTZ cameras. Libraries used - face_recognition, opencv, numpy. Face recognition model was created by davisking using dlib.
please use this file for logging and sharing information. The final README will contain only required information and the logs will be transferred to project.log . Remember to provide documentation to all new content/existing content. 

# Branch Information
dataset - all images for testing
dev1 - development on facerecogniton using dlib model
dev2 - development on facerecogniton using facenet, openface, opencv dnn
dev3 - development using facenet by davidsandberg

# Usage
After cloning the repository to remote -
Read requirements.txt before proceeding.
If working on linux system (Ubuntu 20.04+) run script "run.sh" ($./run.sh).
If working on windows, open "run.sh" and install required libraries.
Before running "FaceDetection.py" load the training images into ./images/training/ and the test images into ./images/testing/ .

# 08-10-2020
This is the second log by Kevin Sebastian. 

- Multiface testing is now available in FaceRecognition.py.
- Updated the structure of the project.

None of the previous files are deleted. They are in either extras or images. The root directory will contain all the modules and libraries (or update requirements.txt to download required libraries in host system). The root contains 3 directories - images, etc and cached_encodings.
images : will be used only during testing and will not be used during deployement. Further images will be sourced from elsehwhere*
etc : store all of the depreciated files, reference files etc. here.
cached_encodings : will be used during testing. on deployement directory will be moved elsewhere*
* elsewhere could be in the same directory, on another disk, cloud or cached into the RAM

I will be updating the structure with further progress of the project. 
The working diagram will be shared shortly (i.e. class diagrams, UML diagrams)
-> Classes must be introduced into the project.
-> need to create a main module that calls other modules
-> follow the working diagram once created

Please feel free to go through the code. Documentation and comments are provided.
Also if you would like to modify anything please do share, communicate and update.
From this point on please use branches and upload all the code to your branch and request for a pull. Once code is reviewed branch can be pulled to master.

THIS WILL BE THE NEW MASTER

# 05-10-2020
Guys this is tushar here MultiFaceCode is the working final code ignore MULTI 
Along with MultiFaceCode im sending a data set called faces please put all images for training in that file and put the faces file in your project 
the test images can be anything with many people or two please test or more then 2 take individual pictures and name them and put it in faces folder then take a group picture as the test images i have commented in the code the line at which you have to put the path to the test jpg
use test images are varying distances and varying number of people as discussed

# References
https://github.com/davisking/dlib-models
https://github.com/ageitgey/face_recognition
https://www.murtazahassan.com
