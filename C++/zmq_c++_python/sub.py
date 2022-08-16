import sys 
import zmq 
import os 
import time 
import numpy as np 
import cv2 

from msg_pb2 import OcvMat  # Will be produced ... Please read README.md 

context = zmq.Context()
socket = context.socket(zmq.REP) 
socket.bind("tcp://*:5000")

ocv_mat = OcvMat() 
print("Listening for incoming messages") 

while True:
    try:
        t = time.time() 
        raw_msg = socket.recv()
        ocv_mat.parseFromString(raw_msg) 
        img = np.frombuffer(ocv_mat.mat_data, dtype=np.uint8)
        img = img.reshape(ocv_mat.rows, ocv_mat.cols, ocv_mat.channels) 

        fps = 1 / (time.time() - t)
        cv2.imshow("img", img)
        print(fps)
        if cv2.waitKey(1) == ord('q'):
            break 
    except KeyboardInterrupt:
        print("EXITING")
        exit()
    
