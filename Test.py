import cv2
import numpy as np
import matplotlib.pyplot as plt

from sift import sift


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
        # cv2.drawContours(img, contours[0], -1, (0, 255, 0), 10)
        # cv2.drawContours(img_contours, contours[0], -1, (0, 255, 0), 10)

        #                      X             \                 Y
        #                 X  \  X+10         \               Y   \  Y+10
        # img[corner[0][0][1] :corner[0][0][1] + 10, corner[0][0][0]:corner[0][0][0] + 10]=(0, 0, 0)#Color Negro RGB
        # img[corner[1][0][1]: corner[1][0][1] + 10, corner[1][0][0]:corner[1][0][0] + 10]=(0, 0, 0)
        # img[corner[2][0][1]: corner[2][0][1] + 10, corner[2][0][0]:corner[2][0][0] + 10]=(0, 0, 0)
        # img[corner[3][0][1]: corner[3][0][1] + 10, corner[3][0][0]:corner[3][0][0] + 10]=(0, 0, 0)

        # Obtenemos el ROI de la carta usando la función getPerspective transform
        corner=np.float32(corner)
        # print(corner[0][0])
        pntsOrde=np.float32([corner[1][0], corner[0][0], corner[2][0], corner[3][0]])

        # print(pntsOrde)
        pntAPegar = np.float32([[0, 0], [200, 0], [0, 320], [200, 320]])  # Depende tamaño del resultado que queramos
        # print(pntAPegar)
        M = cv2.getPerspectiveTransform(pntsOrde, pntAPegar)
        img = cv2.warpPerspective(img, M, (200, 320))  # Perspectiva de UNO carta 1:1.6

        #               Histograma
        #     color = ('r', 'g', 'b')
        #     img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # ##Imagen normal con su histograma
        #     plt.figure(figsize=(12, 4))
        #     plt.subplot(1, 2, 1), plt.imshow(img)
        #     plt.axis("off")
        #
        #     for i, c in enumerate(color):
        #         hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        #         plt.subplot(1, 2, 2), plt.plot(hist, color=c)
        #         plt.xlim([0, 256])

        # Obtenemos el color de la carta
        # Primero establecemos una lista de fronteras en el espacio de color RGB (o BGR), donde las entradas son dos
        # arrays que establecen el limite inferior y el limite superior, por ejemplo:
        # El color rojo tiene ([17, 15, 100], [50, 56, 255]). Acá estamos diciendo que todos los pixeles de la img
        # que tengan R>=100, G>=15, B>=17 y R<=255, G<=56, B<=50 serán considerados de color rojo.
        # Hacemos esto mismo con los otros colores.
        colors = [
            ([0, 90, 60], [40, 255, 120], 'verde'), #verde
            ([25, 146, 190], [62, 200, 250], 'amarillo'),  #amarillo
            ([86, 31, 4], [255, 100, 80], 'azul'),#azul
            ([17, 15, 100], [50, 56, 255], 'rojo'),#rojo
        ]

        # Creamos un loop que vaya recorriendo nuestras fronteras

        for (lower, upper, color) in colors:
            # Creamos un array NumPy que procede de las fronteras, esto se hace porque OpenCV solo acepta que
            # estos limites sean arreglos NumPy. Procedemos a pasar los limites a datos tipo 8-bit integer.
            lower = np.array(lower, dtype="uint8")
            upper = np.array(upper, dtype="uint8")
            # El inRange recibe la img que se le detectará el color, asi como el limite inferior y superior del color.
            mask = cv2.inRange(img, lower, upper)
            # Una mascara binaria es retornada, en donde los pixeles blancos representan los pixeles que
            # estan adentro de los limites y los negros representan los que no.
            # Aplicamos el método bitwise que lo que hace es aplicar la máscara a la img, mostrando solo los pixeles
            # en la img que tienen un valor blanco (255) en la máscara.
            output = cv2.bitwise_and(img, img, mask=mask)
            # mostramos la img normal y después la img con la mascara aplicada
            # cv2.imshow("images", np.hstack([img, output]))
            totalPix=sum(sum(mask))
            # print(totalPix)
            if(totalPix>9000):
                # print('La carta es: ', color)
                defColor=color



            # cv2.imshow('d',mask)
            # print(output)


        return img, defColor

# img=cv2.imread('2G.jpeg')
# img,color=process_img(img) # Aplicamos la función que detecta el color
# sift(img)
# # cv2.imshow('data',img)
# # cv2.waitKey(0)
# number = sift(img)
# print('La carta es '+number+' de color '+color)

# average = np.sum(corner, axis=0) / len(corner)  # entrega promedio (centro) de X y promedio de Y (posicion)
# xCentro = int(average[0][0])
# yCentro = int(average[0][1])
# x, y, w, h = cv2.boundingRect(contours[0])
# test = np.sum(corner, axis=2)  # suma cada X y Y
# # print('np.sum axis=2:',test)