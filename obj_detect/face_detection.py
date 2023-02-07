#Face Detection
import cv2

def detectFace(img, mask_factor):
    filename = img.split(".")[0] # 取得檔案名稱(不添加副檔名)
    img = cv2.imread(img) # 讀取圖檔
    img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 透過轉換函式轉為灰階影像
    color = (0, 255, 0)  # 定義框的顏色
    
    # OpenCV 人臉識別分類器
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    # 調用偵測識別人臉函式
    faceRects = face_classifier.detectMultiScale(
        grayImg, scaleFactor=1.1, minNeighbors=3, minSize=(8, 8))
    
    # 大於 0 則檢測到人臉
    if len(faceRects):  
        # 框出每一張人臉
        for faceRect in faceRects: 
            x, y, w, h = faceRect
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    
    #Masking
    if mask_factor ==1:
        for (x,y,w,h) in faceRects:
            mosaic = img[y:y+h, x:x+w]
            level = 15
            mh = int(h/level)
            mw = int(w/level)  
            mosaic = cv2.resize(mosaic, (mw,mh), interpolation=cv2.INTER_LINEAR) 
            mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_NEAREST) 
            img[y:y+h, x:x+w] = mosaic
        cv2.imshow('masked_img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 
    
    # 將結果圖片輸出
    cv2.imwrite(filename + "_face.jpg", img)

detectFace('obj_detect/portugal.jpg',0)

