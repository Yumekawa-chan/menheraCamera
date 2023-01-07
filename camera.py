import datetime
import time
import cv2

cap = cv2.VideoCapture(0)

num = 1

while True:
    dt_now = datetime.datetime.now()
    if dt_now.second == 0:
        for i in range(10):
            ret,frame = cap.read()
        cv2.imwrite("./images/"+str(num)+".jpg",frame)
        cap.release()
        num += 1
        print(num)
        if num == 31:
            num = 1
        time.sleep(55)
