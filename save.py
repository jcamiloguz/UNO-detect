import cv2


def save():
    cardsDescripitors=[]
    audiosPath=[]
    cardsName = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'stop', 'change']
    audiosName = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'stop', 'change','intro','red','blue','yellow','green','welcome']
    for cardName in cardsName:
        cardPath = './Cartas/' + cardName +'.jpeg'
        trainCard = cv2.imread(cardPath)

        trainCard_gray = cv2.cvtColor(trainCard, cv2.COLOR_BGR2GRAY)
        trainCard_blur = cv2.GaussianBlur(trainCard_gray, (5, 5), 0)
        trainCard_blur = cv2.medianBlur(trainCard_blur, 3)

        sift = cv2.xfeatures2d.SIFT_create()
        train_keypoints, train_descriptor = sift.detectAndCompute(trainCard_blur, None)
        cardsDescripitors.append((train_descriptor,cardName))# agregar el cada descriptor a la lista

    for audioName in audiosName:
        audioPath='./audios/'+audioName+'.mp3'
        audiosPath.append((audioPath,audioName))

    return cardsDescripitors,audiosPath

