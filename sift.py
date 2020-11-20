import cv2
import skimage
from skimage.morphology import erosion, dilation, opening, closing, white_tophat,disk
import numpy as  np
import matplotlib.pyplot as plt

def sift(testCard, cardsDescriptors):
    result =''#Numero de carta selecionada
    finalMatch=0 #Mayor de matches
    for cardDescriptor in cardsDescriptors:

        testCard_gray=cv2.cvtColor(testCard,cv2.COLOR_BGR2GRAY)

        testCard_blur = cv2.GaussianBlur(testCard_gray, (5, 5), 0)
        testCard_blur=cv2.medianBlur(testCard_blur,3)
        # train_thres = cv2.adaptiveThreshold(trainCard_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
        #     cv2.THRESH_BINARY,11,2)
        # test_thres = cv2.adaptiveThreshold(testCard_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
        #     cv2.THRESH_BINARY,11,2)
        # test_thres= closing(test_thres, disk(1))
        # train_thres= closing(train_thres, disk(1))
        sift=cv2.xfeatures2d.SIFT_create()

        test_keypoints, test_descriptor = sift.detectAndCompute(testCard_blur, None)

        BFMatcher=cv2.BFMatcher()

        matches = BFMatcher.knnMatch(cardDescriptor[0], test_descriptor,k=2)

        good = []# matches que cumplen con la condicion v
        for m, n in matches:
            if m.distance < 0.5 * n.distance:
                good.append([m])
        cv2.imshow('info',testCard_blur)
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
            result=cardDescriptor[1]
            finalMatch=uniMatch
    return result

