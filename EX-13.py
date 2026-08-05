import cv2
import numpy as np

cap = cv2.VideoCapture("video13.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    rows, cols = frame.shape[:2]

    pts1 = np.float32([[50,50],[300,50],[50,300],[300,300]])
    pts2 = np.float32([[0,0],[300,0],[100,300],[300,300]])

    M = cv2.getPerspectiveTransform(pts1,pts2)

    result = cv2.warpPerspective(frame,M,(cols,rows))

    cv2.imshow("Perspective Video",result)

    if cv2.waitKey(25)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
