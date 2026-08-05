import cv2
import numpy as np

img = cv2.imread("image15.jpg")

if img is None:
    print("Image not found")
else:
    rows, cols = img.shape[:2]

    src = np.float32([[50,50],[250,50],[50,250],[250,250]])
    dst = np.float32([[20,80],[260,40],[80,260],[260,260]])

    M = cv2.getPerspectiveTransform(src,dst)

    output = cv2.warpPerspective(img,M,(cols,rows))

    cv2.imshow("Original",img)
    cv2.imshow("DLT Transformation",output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
