# FaceDetection-Attendance
This project manages attendance using face recognition from video sources like PTZ cameras. Libraries used - face_recognition, opencv, numpy. Face recognition model was created by davisking using dlib.
please use this file for logging and sharing information. The final README will contain only required information and the logs will be transferred to project.log . Remember to provide documentation to all new content/existing content.

# Note
File name - FileName
class name - ClassName
method name - method_name
variable name - variableName

# Working
Starts from alpha.py. first check if video is converted to set of training and testing images. once that is done, depending on the multi procssing type, each image in the test images will be sent to comparator in FaceRecognition.py. comparator will ask get_encoding to return list of encodings for each pre trained image. get_encoding will check if the training images in each directory (corresponds to each individual) has been extracted and converted to encodings and is stored in cached_encoding directory(each encoding file name is the name of each directory under the training images seen earlier). If the file already exists, it sends back all the encodings of different images of a single persoon back to the comparator method. Note - get_encodings in turn calls the encoder for encoding images in case that was not done.

# Usage
After cloning the repository to remote -
Read requirements.txt before proceeding.
If working on linux system (Ubuntu 20.04+) run script "run.sh" ($./run.sh).
If working on windows, open "run.sh" and install required libraries.
Before running "FaceDetection.py" load the training images into ./images/training/ and the test images into ./images/testing/ .


# Logs

# 17-03-2021
- Added a logger file to store errors and issues in running, rather than have it display on the screen.
- Moved encoding functionality to a different file. Encoder is called only once in the begining. This avoids calling encoder everytime an image is encountered.
- Encoding is also done using multi-processing. The different file makes this possible. 

# 12-11-2020
- Added support for feeding images from videos to FaceRecognition.py
- Added Multi-core support
- Change : now encoding file contains encodings of all images of a single person instead of images of multiple persons

New branch dev1 will now contain this repo. Video data can be obtained from dataset branch. all are under master branch.
next step : compare performance for GPU, performance with other models under dev2 and dev3 branches.
-> structure of project will be made parallel to progress of software. Dropping the idea of creating a structure first (at present).

{Author : Kevin Sebastian}

# 08-10-2020

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

{Author : Kevin Sebastian}

# 05-10-2020
Guys this is tushar here MultiFaceCode is the working final code ignore MULTI 
Along with MultiFaceCode im sending a data set called faces please put all images for training in that file and put the faces file in your project 
the test images can be anything with many people or two please test or more then 2 take individual pictures and name them and put it in faces folder then take a group picture as the test images i have commented in the code the line at which you have to put the path to the test jpg
use test images are varying distances and varying number of people as discussed

# References
https://github.com/davisking/dlib-models
https://github.com/ageitgey/face_recognition
https://www.murtazahassan.com
