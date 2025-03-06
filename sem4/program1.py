import cv2

# Read an image
images = cv2.imread("images.jpeg")

# Display the image
cv2.imshow("Displayed Images", images)
cv2.waitKey(0)  # Wait until a key is pressed
cv2.destroyAllWindows()

# Save the image
cv2.imwrite("output.jpeg", images)
