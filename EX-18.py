import cv2

img = cv2.imread("image18.jpg")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    cv2.imshow("Original", img)
    cv2.imshow("Sobel Y", sobely)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
