imutil
numpy
scikitlearn
opencv_python
import os

print("Select a option from below :\n")
print("1. Extract embed data from images\n2. Train images\n3.Recognize images\n")
n = int(input())

if(n==1):
    os.system('cmd /c "python extract_embeddings.py --dataset dataset --embeddings output/PyPower_embed.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7"')
elif(n==2):
    os.system('cmd /c "python train_model.py --embeddings output/PyPower_embed.pickle --recognizer output/PyPower_recognizer.pickle --le output/PyPower_label.pickle"')
elif (n==3):
    os.system('cmd /c "python recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/PyPower_recognizer.pickle --le output/PyPower_label.pickle"')
else:
    print("invalid input")