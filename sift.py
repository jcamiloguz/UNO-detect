import cv2
import skimage
from skimage.morphology import erosion, dilation, opening, closing, white_tophat,disk
import numpy as  np
import matplotlib.pyplot as plt

def sift(testCard):
    result =''#Numero de carta selecionada
    finalMatch=0 #Mayor de matches
    cards=['1','2','3','4','5','6','7','8','9']
    for cardName in cards:
        filename=cardName+'.jpeg'
        path='./Cartas/'+filename
        # print(path)
        trainCard=cv2.imread(path)

        trainCard_gray=cv2.cvtColor(trainCard,cv2.COLOR_BGR2GRAY)
        testCard_gray=cv2.cvtColor(testCard,cv2.COLOR_BGR2GRAY)

        trainCard_blur = cv2.GaussianBlur(trainCard_gray, (5, 5), 0)
        testCard_blur = cv2.GaussianBlur(testCard_gray, (5, 5), 0)

        # train_thres = cv2.adaptiveThreshold(trainCard_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
        #     cv2.THRESH_BINARY,11,2)
        # test_thres = cv2.adaptiveThreshold(testCard_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
        #     cv2.THRESH_BINARY,11,2)
        # test_thres= closing(test_thres, disk(1))
        # train_thres= closing(train_thres, disk(1))
        sift=cv2.xfeatures2d.SIFT_create()

        train_keypoints, train_descriptor = sift.detectAndCompute(trainCard_blur, None)
        test_keypoints, test_descriptor = sift.detectAndCompute(testCard_blur, None)

        BFMatcher=cv2.BFMatcher()

        matches = BFMatcher.knnMatch(train_descriptor, test_descriptor,k=2)

        good = []# matches que cumplen con la condicion v
        for m, n in matches:
            if m.distance < 0.5 * n.distance:
                good.append([m])

        # result = cv2.drawMatches(trainCard_gray, train_keypoints, testCard_gray, test_keypoints, matches, testCard_gray,
        #                          flags=2)
        #
        # # Display the best matching points
        # plt.rcParams['figure.figsize'] = [14.0, 7.0]
        # plt.title('Best Matching Points')
        # plt.imshow(result)
        # plt.show()
        # matches = sorted(matches, key=lambda x: x.distance)
        # cv2.imshow('data'+cardName,testCard_blur)
        # cv2.imshow('train'+cardName,trainCard_blur)
        # print("Number of Matching : ", len(good))
        uniMatch=len(good)
        if uniMatch>finalMatch:
            result=cardName
            finalMatch=uniMatch
    return result

