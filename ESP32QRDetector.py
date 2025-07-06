import cv2 as cv
import numpy as np

def Resize(frame,percent=75):
    width = int(frame.shape[1] *percent /100)
    height=int(frame.shape[0] *percent /100)
    dim = (width,height)
    res =cv.resize(frame,dim,interpolation=cv.INTER_AREA)
    return res

def QRDecoder(frame):
    detector = cv.QRCodeDetector()
    data,bbox,_ = detector.detectAndDecode(frame)
    
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame,"QR Data : ",(20,30),font,0.6,(255,0,0),1)
    if bbox is not None:
        contours = [bbox.astype(int)]
        cv.drawContours(frame,contours,-1,(255,0,0),4)
        if data:
            cv.putText(frame,data,(20,50),font,0.6,(0,0,255),1)
    else:
        cv.putText(frame,"NONE",(20,50),font,0.6,(0,0,255),1)
    return frame

URL ="http://192.168.4.1:81/stream"
cap = cv.VideoCapture(URL)
while True:
    ret, frame = cap.read()
    QRDecoder(frame)
    res=Resize(frame,200)
    cv.imshow("Detect QR Code", res)
    if cv.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv.destroyAllWindows()
