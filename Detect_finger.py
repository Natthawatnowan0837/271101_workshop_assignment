import cv2
import mediapipe as mp
from cvzone import FPS
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
detector = HandDetector()
fpsReader = FPS()

FingerName = ["THUMB","INDEX","MIDDLE","RING","PINKY"]
 

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        fingersl = []
        handsl = hands[0]
        fingersl = detector.fingersUp(handsl)   
        print(fingersl)
    
        if fingersl[0] == 1:
            cv2.putText(img,FingerName[0], (50,100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 3)
        if fingersl[1] == 1:
            cv2.putText(img,FingerName[1], (50,150), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 3)
        if fingersl[2] == 1:
            cv2.putText(img,FingerName[2], (50,200), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 3)
        if fingersl[3] == 1:
            cv2.putText(img,FingerName[3], (50,250), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 3)
        if fingersl[4] == 1:
            cv2.putText(img,FingerName[4], (50,300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 3)

    cv2.putText(img,"Press 0 for close", (225,450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 3)
    fps,img = fpsReader.update((img))
    cv2.imshow("Image", img)
    if ord(('0')) == 0xFF & cv2.waitKey(1):
        break
cap.release()
cv2.destroryAllwindows()
