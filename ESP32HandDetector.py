import cv2 as cv 
from cvzone.HandTrackingModule import HandDetector

URL ="http://192.168.4.1:81/stream"
cap = cv.VideoCapture(URL)
detector = HandDetector(detectionCon=0.2 , maxHands= 2)
xy = (10,50)
while True:
    ret , webcam = cap.read()
    hand , frame = detector.findHands(webcam)
    if hand:
        hand1 = hand[0]
        lmlist1 = hand1["lmList"]
        #length, info, frame = detector.findDistance(lmlist1[4][:-1], lmlist1[8][:-1], frame)
        finger = detector.fingersUp(hand1)
        cv.putText(frame,f"{finger}",xy,cv.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
    else :
        cv.putText(frame,"No Hand",xy,cv.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)


    
    cv.imshow('webcam', webcam)
    keyexit = cv.waitKey(5) & 0xFF
    if keyexit == 27:
        break

cv.destroyAllWindows()
cap.release()