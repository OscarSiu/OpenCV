import cv2
import sys

path = 'iu.jpg'
img = cv2.imread(path,1); #1= colour & neglect transparency, 0= greyscale, -1 = unchanged including alpha channel

if img is None:
    sys.exit("Image not found")

cv2.imshow('IU',img)
cv2.waitKey(0)

# Flipped Image
flipHorizontal = cv2.flip(img, 1)
cv2.imshow('Flipped',flipHorizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save image
status = cv2.imwrite(path,img)
print('image written success?', status)

