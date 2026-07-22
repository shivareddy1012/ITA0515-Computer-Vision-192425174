import cv2

img = cv2.imread("image9.jpg")

if img is None:
    print("Image not found")
else:
    cw = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
    ccw = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

    cv2.imshow("Clockwise",cw)
    cv2.imshow("Counter Clockwise",ccw)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
