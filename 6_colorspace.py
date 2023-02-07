import cv2
import numpy as np

path = 'iu.jpg'
img = cv2.imread(path,1)
B, G, R = cv2.split(img)

cv2.imshow('original',img)
cv2.waitKey(0)

cv2.imshow('blue',B)
cv2.waitKey(0)

cv2.imshow('green',G)
cv2.waitKey(0)

cv2.imshow('red',R)
cv2.waitKey(0)

px = img[100,100]
print('px: ', px)


#HSV color scheme
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('red value:', img.item(10,10,2)) #access red value
img.itemset((10,10,2),100) #modify red value
print('new red value: ',img.item(10,10,2))

print('image shape: ',img.shape) #no. of rows, no. of columns, no. of channels.
print('image size: ',img.size)
print('image data type: ',img.dtype) #datatype

#img = cv.merge((b,g,r))
#b = img [:,:,0]
#g = img [:,:,1]
#r = img [:,:,2]

#img[:,:,2] = 0 //setting all values in red channgel as zero
