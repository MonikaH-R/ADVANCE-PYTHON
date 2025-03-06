import cv2
images=cv2.imread("images.jpeg")#load the image
cv2.imshow("Display Window",images)
cv2.waitKey()
cv2.destroyAllWindows()
print("Images Shape:",images.shape)
print("Images Size:",images.size)
print("Data Type:",images.dtype)