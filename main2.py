#! /usr/bin/env python
import cv2
import operator

haut_du_corps = cv2.CascadeClassifier("/home/pi/Desktop/testeur/haarcascade_upperbody.xml")
bas_du_corps = cv2.CascadeClassifier("/home/pi/Desktop/testeur/haarcascade_lowerbody.xml")
face_cascade = cv2.CascadeClassifier("/home/pi/Desktop/testeur/haarcascade_frontalface_alt2.xml")
profile_cascade = cv2.CascadeClassifier("/home/pi/Desktop/testeur/haarcascade_profileface.xml")

def deuxieme_code():
    cap = cv2.VideoCapture(0)
    width = int(cap.get(3))
    marge = 70

    while True:
        isDetected = False
        ret, frame = cap.read()
        tab_face = []
        tidemark = cv2.getTickCount()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(5, 5))
        for x, y, w, h in face:
            tab_face.append([x, y, x + w, y + h])
            isDetected = True
        face = profile_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)
        for x, y, w, h in face:
            tab_face.append([x, y, x + w, y + h])
            isDetected = True
        gray2 = cv2.flip(gray, 1)
        face = profile_cascade.detectMultiScale(gray2, scaleFactor=1.2, minNeighbors=4)
        for x, y, w, h in face:
            tab_face.append([width - x, y, width - (x + w), y + h])
            isDetected = True
        tab_face = sorted(tab_face, key=operator.itemgetter(0, 1))
        index = 0
        for x, y, x2, y2 in tab_face:
            if not index or (x - tab_face[index - 1][0] > marge or y - tab_face[index - 1][1] > marge):
                cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 2)
            index += 1
            isDetected = True
            position = [x,y,x2,y2]

        if isDetected == True:
            if(str(x)<100 & str(x)>0):
                my_msg.data= '20'
            if (str(x) < 200 & str(x) > 100):
                my_msg.data = '40'
            if (str(x) < 300 & str(x) > 200):
                my_msg.data = '60'
            if (str(x) < 400 & str(x) > 300):
                my_msg.data = '40'
            if (str(x) < 500 & str(x) > 400):
                my_msg.data = '50'
            if (str(x) < 600 & str(x) > 500):
                my_msg.data = '60   '
            if (str(x) < 700 & str(x) > 600):
                my_msg.data = '70'
            if (str(x) < 800 & str(x) > 700):
                my_msg.data = '80'
            if (str(x) < 900 & str(x) > 800):
                my_msg.data = '90'
            my_msg.data(my_msg)
        if isDetected == False:
            print("personne")

    cap.release()

deuxieme_code()


