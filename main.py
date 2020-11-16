import cv2

from detectColor import detectColor
from drawContour import drawContour
from sift import sift

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    img,imgContour,corner,isCard=drawContour(frame)
    cv2.imshow('frame',imgContour)


    if cv2.waitKey(1) & 0xFF == ord(' '):
        if(isCard):
            imgProcessed, color, isCard = detectColor(img,corner)  # Aplicamos la función que detecta el color
            number = sift(imgProcessed)
            print('La carta es ' + number + ' de color ' + color)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()