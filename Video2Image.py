# convert videos into images and store in location
# Source ./video/... , Destination ./Images/...
# for each video make folder and store images in each
# get accurate faces only around 30 images
import cv2
import os
import subprocess
import shlex

def convert(feedType):
    """
    converts each video to image and stores in directory
    named after the video file under the location specifiedlocation
    """
    path = "videos/" + feedType + "/"
    videos = os.listdir(path)
    for video in videos:
        if os.path.isdir("images/" + feedType + "/" + video.split(".")[0]) != True:
            print("extracting images from provided video(s) in " + path + video)
            os.mkdir("images/" + feedType + "/" + video.split(".")[0])
            cmd = "ffprobe -loglevel error -select_streams v:0 -show_entries stream_tags=rotate -of default=nw=1:nk=1"
            args = shlex.split(cmd)
            args.append(path + video)
            # run the ffprobe process, decode stdout into utf-8 & convert to int
            ffprobeOutput = subprocess.check_output(args).decode('utf-8')
            rotation = 0
            # check if cmdis gives an output. is 0 if no output is given (no rotation)
            if len(ffprobeOutput) > 0:
                rotation = int(ffprobeOutput)
            vidcap = cv2.VideoCapture(path + video)
            vidcap.get(cv2.CAP_PROP_POS_MSEC)
            fps = vidcap.get(cv2.CAP_PROP_FPS)
            frameCount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration = frameCount / fps * 1000
            interval = duration / 10
            # The 10 implies the number of images required. Change it for more images to be extracted. 
            count = 0
            success, image = vidcap.read()
            while count < 10 and success:
                success, image = vidcap.read()
                if rotation == 90:
                    image = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
                if rotation == 270:
                    image = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
                if rotation == 180:
                    image = cv2.rotate(image,cv2.ROTATE_180)
                # cv2.ROTATE_90_COUNTERCLOCKWISE : 270deg
                # cv2.ROTATE_180 : 180deg
                # cv2.cv2.ROTATE_90_CLOCKWISE : 90deg
                # image = cv2.rotate(image,)
                cv2.imwrite("images/" + feedType + "/" + video.split(".")[0] + "/" + 
                video.split(".")[0] + str(count) + ".jpeg", image)
                # save frame as JPEG file
                count+=1
                vidcap.set(cv2.CAP_PROP_POS_MSEC,count*interval)