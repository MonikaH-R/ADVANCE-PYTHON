import cv2
image = cv2.imread("images.jpeg")  # Load an image
#Get pixel value at (y=50, x=100)
pixel_value = image[50, 100] # Returns [Blue, Green, Red] val
print("BGR Pixel Value:", pixel_value)
cv2.imshow("Display Window", image)
cv2.waitKey(0)
cv2.destroyAllWindows()