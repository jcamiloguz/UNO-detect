import cv2
import numpy as np

def process_img(img):
    # convert img to grey
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # use Gaussian blur
    blur = cv2.GaussianBlur(img_grey, (5, 5), 0)
    # set a thresh
    thresh = 100
    # Adatative tresh
    # thresh_level = bkg_level + 170
    # img_w, img_h = np.shape(img)[:2]
    # bkg_level = imgray[int(img_h/100)][int(img_w/2)] # Buscar un promedio de ROI
    # get threshold image
    ret, thresh_img = cv2.threshold(blur, thresh, 255, cv2.THRESH_BINARY)
    # find contours

    contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    peri = cv2.arcLength(contours[0], True)
    corner = cv2.approxPolyDP(contours[0], 0.01 * peri, True)
    print(corner)
    if len(corner)==4:
        # create an empty image for contours
        img_contours = np.zeros(img.shape)
        # draw the contours on the empty image
        cv2.drawContours(img, contours[0], -1, (0, 255, 0), 10)
        cv2.drawContours(img_contours, contours[0], -1, (0, 255, 0), 10)

        # draw square points
        #                      X             \                 Y
        #                 X  \  X+10         \               Y   \  Y+10
        img[corner[0][0][1] :corner[0][0][1] + 10, corner[0][0][0]:corner[0][0][0] + 10]=(0, 0, 0)#Color Negro RGB
        img[corner[1][0][1]: corner[1][0][1] + 10, corner[1][0][0]:corner[1][0][0] + 10]=(0, 0, 0)
        img[corner[2][0][1]: corner[2][0][1] + 10, corner[2][0][0]:corner[2][0][0] + 10]=(0, 0, 0)
        img[corner[3][0][1]: corner[3][0][1] + 10, corner[3][0][0]:corner[3][0][0] + 10]=(0, 0, 0)
        average = np.sum(corner, axis=0) / len(corner)
        print(average)
        # print image
        # cv2.imshow('contours con imagen', img)


        # cv2.waitKey(0)
    return img

