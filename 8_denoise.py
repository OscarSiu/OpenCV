import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('iu.jpg')
cv.imshow('IU', img)
cv.waitKey(0)


dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(dst)
plt.show()
