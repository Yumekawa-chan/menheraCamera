import datetime
import time
import cv2

cap = cv2.VideoCapture(0)

print("Camera is operationing!")

while True:
    dt_now = datetime.datetime.now()
    ret,frame = cap.read()
    if dt_now.second == 0:
        cv2.imwrite(f"./images/{dt_now.hour:02}{dt_now.minute:02}.jpg",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(1)
cap.release()
cv2.destroyAllWindows()