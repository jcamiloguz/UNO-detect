import numpy as np
import cv2

import sift
from Test import process_img
from sift import sift

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # processed_img=process_img(frame)
    cv2.imshow('frame',frame)


    if cv2.waitKey(1) & 0xFF == ord('f'):
        img, color = process_img(frame)  # Aplicamos la función que detecta el color
        sift(img)
        number = sift(img)
        print('La carta es ' + number + ' de color ' + color)

        break

cap.release()
cv2.destroyAllWindows()