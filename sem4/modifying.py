#Modifying Image Pixels
import cv2
image = cv2.imread("image1.jpeg") # Load an image
cv2.imshow("Before changing", image)
image[10, 20] = [0, 35, 0] #Change pixel color at (50,100) to green
cv2.imshow("After changing", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

