import cv2

cap = cv2.VideoCapture(1)

if not cap.isOpened():
   print("Cannot open camera")
   exit()
   
   
# Set frame dimensions
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)

while(True):
  # capture frame by frame
  ret, frame = cap.read()
  
  if not ret:
     print("Cannot receive frame (stream end?). Exiting ... ")
     break
     
  gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  
  # Display resulting frame
  cv2.imshow('frame', gray)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


cap.release()
cv2.destroyAllWindows()
