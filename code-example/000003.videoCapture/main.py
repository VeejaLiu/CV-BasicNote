from time import sleep

import cv2

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('Test camera')
success, frame = cameraCapture.read()
while success:
    # 27 is ESC key
    if cv2.waitKey(1) == 27:
        break
    cv2.imshow('Test camera', frame)
    sleep(0.5)
    success, frame = cameraCapture.read()

cameraCapture.release()

# https://blog.csdn.net/kingroc/article/details/83000885