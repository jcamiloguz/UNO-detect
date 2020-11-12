import cv2
import numpy as np

img = cv2.imread('9R.jpeg', cv2.IMREAD_UNCHANGED)

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
apprsox = cv2.approxPolyDP(contours[0], 0.01*peri, True)
pts = np.float32(approx)

print(pts)

# create an empty image for contours
img_contours = np.zeros(img.shape)
# draw the contours on the empty image
cv2.drawContours(img_contours, contours[0], -1, (0, 255, 0), 3)
# save image
cv2.imwrite('contours.png', img_contours)
