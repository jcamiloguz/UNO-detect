import cv2
import numpy as np


def process_img(img):
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img_grey, (5, 5), 0)
    thresh = 100
    # Adatative tresh
    # thresh_level = bkg_level + 170
    # img_w, img_h = np.shape(img)[:2]
    # bkg_level = imgray[int(img_h/100)][int(img_w/2)] # Buscar un promedio de ROI
    # get threshold image
    ret, thresh_img = cv2.threshold(blur, thresh, 255, cv2.THRESH_BINARY)
    # find contours

    _ ,contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    peri = cv2.arcLength(contours[0], True)
    corner = cv2.approxPolyDP(contours[0], 0.01 * peri, True)
    # print(corner)
    if len(corner)==4:
        img_contours = np.zeros(img.shape)
        # draw the contours on the empty image
        #cv2.drawContours(img, contours[0], -1, (0, 255, 0), 10)
        # cv2.drawContours(img_contours, contours[0], -1, (0, 255, 0), 10)

        #                      X             \                 Y
        #                 X  \  X+10         \               Y   \  Y+10
        # img[corner[0][0][1] :corner[0][0][1] + 10, corner[0][0][0]:corner[0][0][0] + 10]=(0, 0, 0)#Color Negro RGB
        # img[corner[1][0][1]: corner[1][0][1] + 10, corner[1][0][0]:corner[1][0][0] + 10]=(0, 0, 0)
        # img[corner[2][0][1]: corner[2][0][1] + 10, corner[2][0][0]:corner[2][0][0] + 10]=(0, 0, 0)
        # img[corner[3][0][1]: corner[3][0][1] + 10, corner[3][0][0]:corner[3][0][0] + 10]=(0, 0, 0)

        corner=np.float32(corner)
        print(corner[0][0])
        pntsOrde=np.float32([corner[1][0],corner[0][0],corner[2][0],corner[3][0]])

        print(pntsOrde)
        pntAPegar = np.float32([[0,0],[200,0],[0,320],[200,320]])#depende tamano del resultado que queramos
        print(pntAPegar)
        M = cv2.getPerspectiveTransform(pntsOrde, pntAPegar)
        img = cv2.warpPerspective(img, M, (200, 320))# Perspectiva de UNO carta 1:1.6

    return img

img=cv2.imread('2B2.jpeg')
img=process_img(img)
temp_rect = np.zeros((4,2), dtype = "float32")
cv2.imshow('imagen',img)
cv2.waitKey(0)
cv2.xfeatures2d.SIFT_create()
# average = np.sum(corner, axis=0) / len(corner)  # entrega promedio (centro) de X y promedio de Y (posicion)
# xCentro = int(average[0][0])
# yCentro = int(average[0][1])
# x, y, w, h = cv2.boundingRect(contours[0])
# test = np.sum(corner, axis=2)  # suma cada X y Y
# # print('np.sum axis=2:',test)