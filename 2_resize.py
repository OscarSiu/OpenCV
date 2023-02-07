#Geometric transformations

import cv2
import numpy as np

img = cv2.imread('iu.jpg', 1)
#cv2.imshow('img',img);
print(img.shape); #print dimension and channels

#SCALING
#img_resized = cv2.resize(img, (600,400), interpolation = cv2.INTER_NEAREST)
img_resized = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
cv2.imshow('resized', img_resized)

#ROTATION
#img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

cv2.waitKey(0)
cv2.destroyAllWindows()

#INTER_NEAREST   nearest-neighbor interpolation
#INTER_LINEAR    bilinear interpolation (use by default)
#INTER_AREA      resampling by pixel area relation
#INTER_CUBIC     bicubic interpolation over 4x4 pixel neighborhood
#INTER_LANCZOS4  Lanczos interpolation over 8x8 pixel neighborhood

#transformation functions
#cv2.warpAffine()
#cv2.warpPerspective