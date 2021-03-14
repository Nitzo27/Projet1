import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    cv2.imshow('img', img)
    if cv2.waitKey(100) & 0xff == ord('q'):
        break
