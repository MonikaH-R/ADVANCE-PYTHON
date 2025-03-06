# image shape , image size, image dtype
import cv2
image = cv2.imread("images.jpeg") # Load an image
cv2.imshow("Display Window", image)
cv2.waitKey()
cv2.destroyAllWindows()
print("Image Shape:",image.shape) # (height, width, channels)
print("Image Size:",image.size) # Total number of pixels
print("Data Type:",image.dtype) # Image array data type
