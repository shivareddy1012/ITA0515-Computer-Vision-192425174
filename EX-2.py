import cv2

img = cv2.imread("image2.jpg")

if img is None:
    print("Image not found")
else:
    blur = cv2.GaussianBlur(img,(7,7),0)

    cv2.imshow("Blur",blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
