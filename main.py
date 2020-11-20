import cv2
from playsound import playsound

from detectColor import detectColor
from drawContour import drawContour
from playCard import playCards
from save import save
from sift import sift

cap = cv2.VideoCapture(0)
cardsDescriptors, audiosPath=save()
playsound('./audios/welcome.mp3')

while(True):
    ret, frame = cap.read()

    img,imgContour,corner,isCard,w,h=drawContour(frame)
    cv2.imshow('frame',imgContour)

    if cv2.waitKey(1) & 0xFF == ord(' '):
        if(isCard):
            imgProcessed, color, isCard = detectColor(img,corner,w,h)  # Aplicamos la función que detecta el color
            number = sift(imgProcessed,cardsDescriptors)
            playCards(number,color,audiosPath)
            print('La carta es ' + number + ' de color ' + color)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()