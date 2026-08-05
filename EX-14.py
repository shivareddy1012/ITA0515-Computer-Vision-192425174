import cv2
import numpy as np

img = cv2.imread("image14.jpg")

if img is None:
    print("Image not found")
else:
    rows, cols = img.shape[:2]

    src = np.float32([[50,50],[250,50],[50,250],[250,250]])
    dst = np.float32([[10,100],[250,50],[100,250],[250,250]])

    H,_ = cv2.findHomography(src,dst)

    output = cv2.warpPerspective(img,H,(cols,rows))

    cv2.imshow("Original",img)
    cv2.imshow("Homography",output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
