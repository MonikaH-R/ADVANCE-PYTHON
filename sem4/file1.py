import cv2
image = cv2.imread("images.jpeg") # Load an image
cv2.imshow("Display Window", image)
cv2.waitKey(0)
cv2.destroyAllWindows()