import cv2

img = cv2.imread("image8.jpg")

if img is None:
    print("Image not found")
else:
    small = cv2.resize(img,(300,300))
    large = cv2.resize(img,(800,800))

    cv2.imshow("Small",small)
    cv2.imshow("Large",large)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
