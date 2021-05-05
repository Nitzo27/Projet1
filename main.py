import cv2
import operator

haut_du_corps = cv2.CascadeClassifier("./haarcascade_upperbody.xml")
bas_du_corps = cv2.CascadeClassifier("./haarcascade_lowerbody.xml")
face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_alt2.xml")
profile_cascade = cv2.CascadeClassifier("./haarcascade_profileface.xml")


def premier_code():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        tidemark = cv2.getTickCount()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corps = haut_du_corps.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
        for x, y, w, h in corps:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - tidemark)
        cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.imshow('video', frame)
    cap.release()
    cv2.destroyAllWindows()


def deuxieme_code():
    bool isDetected = False
    cap = cv2.VideoCapture(0)
    width = int(cap.get(3))
    marge = 70

    while True:
        ret, frame = cap.read()
        tab_face = []
        tidemark = cv2.getTickCount()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(5, 5))
        for x, y, w, h in face:
            tab_face.append([x, y, x + w, y + h])
        face = profile_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)
        for x, y, w, h in face:
            tab_face.append([x, y, x + w, y + h])
        gray2 = cv2.flip(gray, 1)
        face = profile_cascade.detectMultiScale(gray2, scaleFactor=1.2, minNeighbors=4)
        for x, y, w, h in face:
            tab_face.append([width - x, y, width - (x + w), y + h])
        tab_face = sorted(tab_face, key=operator.itemgetter(0, 1))
        index = 0
        for x, y, x2, y2 in tab_face:
            if not index or (x - tab_face[index - 1][0] > marge or y - tab_face[index - 1][1] > marge):
                cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 2)
                isDetected = True
            index += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if(isDetected == True)
            print("Dectecté")
        else
            print("personne")

        cv2.imshow('video', frame)
    cap.release()
    cv2.destroyAllWindows()


#premier_code()
deuxieme_code()
