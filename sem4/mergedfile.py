import cv2
images = cv2.imread("images.jpeg") # Load an image
b,g,r = cv2.split(images)
images_merged = cv2.merge([b,g,r])
cv2.imshow("Display Window", images)
cv2.waitKey(0)
cv2.destroyAllWindows()