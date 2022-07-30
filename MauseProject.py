import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

##########################
wCam, hCam = 640, 480

#########################

pTime = 0


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)

# print(wScr, hScr)

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)


    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        #print((x1,y1),(x2,y2))
        #fingersUp metodu ile açık olan parmaklarımızı 1 kapalı olanları 0 yapıyoruz
        fingers=detector.fingersUp()
        print(fingers)
        #hareket modu için işaret parmağı 1 orta parmak 0 olmalı
        if fingers[1]==1 and fingers[2]==0:
            x3=np.interp(x1)


    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2,
                (144, 27,51), 2)
    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)