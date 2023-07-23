
# Required imports
from collections import deque
import numpy as np
import cv2
import tkinter as tk
from tkVideoPlayer import TkinterVideo
from tkinter import filedialog as fd
from collections import deque
import numpy as np
import cv2
import tkinter as tk
from tkVideoPlayer import TkinterVideo
from tkinter import *
from tkinter import filedialog
from tkinter import Button, filedialog as fd
from PIL import ImageTk, Image 
import sys
import os

filename = 0

class Parameters:
    
    def __init__(self):
        self.CLASSES = open("model/action_recognition_kinetics.txt"
                            ).read().strip().split("\n")
        self.ACTION_RESNET = 'model/resnet-34_kinetics.onnx'
        #self.VIDEO_PATH = None
        self.VIDEO_PATH = filename
        self.SAMPLE_DURATION = 16
        self.SAMPLE_SIZE = 112



param = Parameters()


captures = deque(maxlen=param.SAMPLE_DURATION)



net = cv2.dnn.readNet(model=param.ACTION_RESNET)

vs= cv2.VideoCapture(param.VIDEO_PATH if param.VIDEO_PATH else 0)
while True:
    # Loop over and read capture from the given video input
    (grabbed, capture) = vs.read()

    # break when no frame is grabbed (or end if the video)
    if not grabbed:
        break

    # resize frame and append it to our deque
    capture = cv2.resize(capture, dsize=(600, 350))
    captures.append(capture)

    # Process further only when the deque is filled
    if len(captures) < param.SAMPLE_DURATION:
        continue

    # now that our captures array is filled we can
    # construct our image blob
    # We will use SAMPLE_SIZE as height and width for
    # modifying the captured frame
    imageBlob = cv2.dnn.blobFromImages(captures, 1.0,
                                       (param.SAMPLE_SIZE,
                                        param.SAMPLE_SIZE),
                                       (114.7748, 107.7354, 99.4750),
                                       swapRB=True, crop=True)

    # Manipulate the image blob to make it fit as as input
    # for the pre-trained OpenCV's
    # Human Action Recognition Model
    imageBlob = np.transpose(imageBlob, (1, 0, 2, 3))
    imageBlob = np.expand_dims(imageBlob, axis=0)

    # Forward pass through model to make prediction
    net.setInput(imageBlob)
    outputs = net.forward()
    # Index the maximum probability
    label = param.CLASSES[np.argmax(outputs)]

    # Show the predicted activity
    cv2.rectangle(capture, (0, 350), (250,300), (255, 240, 245), -1)
    cv2.putText(capture, label, (10, 330), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 0, 0), 2)

    # Display it on the screen
    cv2.imshow("Human Activity Recognition", capture)

    key = cv2.waitKey(1) & 0xFF
    # Press key 'q' to break the loop
    if key == ord("q"):
        break

