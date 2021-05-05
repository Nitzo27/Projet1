import cv2
import operator

haut_du_corps = cv2.CascadeClassifier("./haarcascade_upperbody.xml")
bas_du_corps = cv2.CascadeClassifier("./haarcascade_lowerbody.xml")
face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_alt2.xml")
profile_cascade = cv2.CascadeClassifier("./haarcascade_profileface.xml")

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
            
        if isDetected == True :
            print("Dectecté")
        if isDetected == False :
            print("personne")

    cap.release()

deuxieme_code()
