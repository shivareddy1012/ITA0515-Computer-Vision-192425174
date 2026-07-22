import cv2
import numpy as np

img = cv2.imread("image10.jpg")

if img is None:
    print("Image not found")
else:
    rows, cols = img.shape[:2]

    M = np.float32([[1, 0, 100],
                    [0, 1, 50]])

    moved = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow("Translated Image", moved)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
