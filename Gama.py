import cv2
import numpy as np
def Gama(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)


img = cv2.imread('kedi.jpg')
gammaImg = Gamma(img, 3)

cv2.imshow(img)
cv2.imshow('Gama dönüşümü3', gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('kedi.jpg')
gammaImg = Gamma(img, 4)

cv2.imshow('Gama dönüşümü4', gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('kedi.jpg')
gammaImg = Gamma(img, 5)

cv2.imshow('Gama dönüşümü5', gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows()