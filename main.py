import numpy as np
import cv2

from detectUNO import process_img

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    processed_img=process_img(frame)
    cv2.imshow('frame',processed_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()