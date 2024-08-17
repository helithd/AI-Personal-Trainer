import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0

while True:
    success, img = cap.read()
    # img = cv2.imread("Ai Trainer/test.jpg")
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)
    #
    # left arm
    if len(lmList) != 0:
        # # right arm
        # angle = detector.findAngle(img, 16, 14, 12)
        # left arm
        angle = detector.findAngle(img, 11, 13, 15)

        per = np.interp(angle, (205, 305), (0, 100))
        bar = np.interp(angle, (205, 305), (650, 100))
        # print(angle, per)

        # check for the dumbbell curls
        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0

        print(count)
        # Draw Bar
        cv2.rectangle(img, (800, int(bar)), (1000, 650), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(per)}', (830, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

        # Draw Curl Count
        cv2.rectangle(img, (0, 0), (250, 250), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(count)}', (50, 200), cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 0), 15)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
