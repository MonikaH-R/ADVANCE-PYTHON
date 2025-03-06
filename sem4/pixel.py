#Get pixel value at (y=50, x=100)
import cv2
image = cv2.imread("image1.jpeg")
pixel_value = image [50,100]
print("BGR Pixel Value:", pixel_value)
cv2.waitKey(0)
cv2.destroyAllWindows()
