import cv2

img = cv2.imread('obj_detect/qatar.png', 1)
#img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Cars detection
car = cv2.CascadeClassifier('obj_detect/cars.xml')
gray = cv2.medianBlur(gray, 3)
cars = car.detectMultiScale(img, 1.1, 3)

#Draw frame
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('car detect', img)
cv2.waitKey(0)
cv2.destroyAllWindows()