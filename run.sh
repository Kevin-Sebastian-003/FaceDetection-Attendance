#!/bin/sh
sudo apt update
sudo apt upgrade
sudo apt install python3-opencv
sudo apt install python3-pip
sudo apt install ffmpeg
sudo pip3 install numpy cmake virtualenv virtualenvwrapper
virtualenv venv
source venv/bin/activate
pip3 install cmake dlib face_recognition numpy opencv-python
deactivate
echo "done! proceed with face recognition"
