import cv2

img = cv2.imread("image20.jpg")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    lap = cv2.Laplacian(gray, cv2.CV_64F)

    cv2.imshow("Original", img)
    cv2.imshow("Laplacian", lap)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
