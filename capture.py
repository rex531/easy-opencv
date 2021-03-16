import threading
import cv2
import numpy as np
global timer


def startShot():
    global num
    ret, frame = cap.read()
    if num != 10:
        cv2.imshow("capture", frame)
        cv2.imwrite("C:\\Users\\Rex\\Desktop\\opencv\\test"+ str(num) + '.jpg', frame)
    num += 1
    if num == 10:
        cap.release()
        cv2.destroyAllWindows()
        for i in range(10):
            img = cv2.imread('C:\\Users\\Rex\\Desktop\\opencv\\test%d.jpg' %(i))
        for j in range(10):
            cv2.imshow('C:\\Users\\Rex\\Desktop\\opencv\\test%d.jpg' %(j), img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    timer = threading.Timer(1, startShot)
    timer.start()

num = 0
cap = cv2.VideoCapture(0)
timer = threading.Timer(1, startShot)
timer.start()
