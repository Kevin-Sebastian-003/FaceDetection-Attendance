import os
import cv2
import subprocess
import shlex ,json 
import multiprocessing
import logging
# path ="./images/"
# tdirs = os.listdir(path)
# dirs = []
# for dir in tdirs:
#     dirs.append(path+dir+"/") 
# print(dirs)
# for dir in dirs:
#     print("cached_encodings/" + dir.split("/")[2] + ".json")




# def feed(feedType):
#     path = "videos/" + feedType + "/"
#     videos = os.listdir(path)
#     for video in videos:
#         vidcap = cv2.VideoCapture(path + video)
#         vidcap.get(cv2.CAP_PROP_POS_MSEC)
#         fps = vidcap.get(cv2.CAP_PROP_FPS)
#         frameCount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
#         duration = frameCount / fps * 1000
#         interval = duration / 10
#         count = 1
#         success, image = vidcap.read()
#         while count < 10 and success:
#             success, image = vidcap.read()
#             cv2.imwrite(video.split(".")[0] + str(count) + ".jpeg", image)
#             # save frame as JPEG file
#             count+=1
#             vidcap.set(cv2.CAP_PROP_POS_MSEC,count*interval)

# feed ("training")


# def feed(feedType):
#     path = "videos/" + feedType + "/"
#     videos = os.listdir(path)
#     for video in videos:
#         if os.path.isdir("images/" + path + video.split(".")[0]) != True:
#             print("hello")
# feed ("training")

# abc = subprocess.check_output("ffprobe -loglevel error -select_streams v:0 -show_entries stream_tags=rotate -of default=nw=1:nk=1 -i " + "videos/training/kevin.mp4")

# dirs = os.listdir("videos/training")
# for dir in dirs:
#     cmd = "ffprobe -loglevel error -select_streams v:0 -show_entries stream_tags=rotate -of default=nw=1:nk=1"
#     args = shlex.split(cmd)
#     args.append("videos/training/" + dir)
#     # run the ffprobe process, decode stdout into utf-8 & convert to JSON
#     ffprobe_output = subprocess.check_output(args).decode('utf-8')
#     if len(ffprobe_output) > 0:  # Output of cmdis None if it should be 0
#         rotation = int(ffprobe_output)
#     else:
#         rotation = 0
#     print(str(dir) + "  :  " + str(rotation))

# print("Number of cpu : ", multiprocessing.cpu_count())

# files = os.listdir("cached_encodings/" )
# for file in files:
#     fileName = "cached_encodings/" + file + ".json"
#     print(fileName)
# averageEncodings = [0] * 128
# print (averageEncodings)
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('This will get logged to a file')
logging.warning('Admin logged out')