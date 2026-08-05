import cv2
import numpy as np

img = cv2.imread("image12.jpg")

if img is None:
    print("Image not found")
else:
    rows, cols = img.shape[:2]

    pts1 = np.float32([[50,50],[300,50],[50,300],[300,300]])
    pts2 = np.float32([[0,0],[300,0],[100,300],[300,300]])

    M = cv2.getPerspectiveTransform(pts1,pts2)

    output = cv2.warpPerspective(img,M,(cols,rows))

    cv2.imshow("Original",img)
    cv2.imshow("Perspective",output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
