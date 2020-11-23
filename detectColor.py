import cv2
import numpy as np



def detectColor(img, corner, w, h):
    isCard=False
    defColor=' '
    # corner=np.float32(corner)
    #
    
    pntsOrde=np.float32([corner[1][0], corner[0][0], corner[2][0], corner[3][0]])

    #Encontrar distancia entre corners

    if w>h:
        pntAPegar = np.float32([[0, 0], [320, 0], [0, 200], [320, 200]])  # Depende tamaño del resultado que queramos
        M = cv2.getPerspectiveTransform(pntsOrde, pntAPegar)
        img = cv2.warpPerspective(img, M, (320, 200))  # Perspectiva de UNO carta 1:1.6
    if h>w:
        pntAPegar = np.float32([[0, 0], [200, 0], [0, 320], [200, 320]])  # Depende tamaño del resultado que queramos
        M = cv2.getPerspectiveTransform(pntsOrde, pntAPegar)
        img = cv2.warpPerspective(img, M, (200, 320))  # Perspectiva de UNO carta 1:1.6

    # Obtenemos el color de la carta
    # Primero establecemos una lista de fronteras en el espacio de color RGB (o BGR), donde las entradas son dos
    # arrays que establecen el limite inferior y el limite superior, por ejemplo:
    # El color rojo tiene ([17, 15, 100], [50, 56, 255]). Acá estamos diciendo que todos los pixeles de la img
    # que tengan R>=100, G>=15, B>=17 y R<=255, G<=56, B<=50 serán considerados de color rojo.
    # Hacemos esto mismo con los otros colores.
    colors = [
        ([0, 90, 100], [115, 255, 165], 'green'), #verde
        ([25, 146, 190], [62, 200, 250], 'yellow'),  #amarillo
        ([86, 31, 4], [255, 100, 80], 'blue'),#azul
        ([17, 15, 100], [50, 100, 255], 'red'),#rojo
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
        totalPix=sum(sum(mask))
        if(totalPix>9000):
            defColor=color
            isCard = True


    return img, defColor, isCard

