import cv2

def drawContour(img):

    isCard=False
    corner=0
    imgWithCountors=img
    # Pasar a escala de grises
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Pasarle el
    blur = cv2.GaussianBlur(img_grey, (5, 5), 0)
    # Pasarle Threshold
    thresh = 100
    ret, thresh_img = cv2.threshold(blur, thresh, 255, cv2.THRESH_BINARY)
    # Encontrar Contornos
    dummy ,contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if(len(contours)>0):
        # Encontrar Perimetro
        peri = cv2.arcLength(contours[0], True)
        # Encontrar esquinas, 10% del perimetro en precision, True= contorno cerrado
        corner = cv2.approxPolyDP(contours[0], 0.01 * peri, True)
        if len(corner)==4:
            # dibujar Contorno
            cv2.drawContours(imgWithCountors, contours[0], -1, (0, 255, 0), 10)

            # Dibujar Esquinas
            #                      X             \                 Y
            #                 X  \  X+10         \               Y   \  Y+10
            img[corner[0][0][1] :corner[0][0][1] + 10, corner[0][0][0]:corner[0][0][0] + 10]=(0, 0, 0)#Color Negro RGB
            img[corner[1][0][1]: corner[1][0][1] + 10, corner[1][0][0]:corner[1][0][0] + 10]=(0, 0, 0)
            img[corner[2][0][1]: corner[2][0][1] + 10, corner[2][0][0]:corner[2][0][0] + 10]=(0, 0, 0)
            img[corner[3][0][1]: corner[3][0][1] + 10, corner[3][0][0]:corner[3][0][0] + 10]=(0, 0, 0)
            isCard=True
    return img,imgWithCountors, corner, isCard

