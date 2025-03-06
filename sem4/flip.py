import cv2

# Load image
image = cv2.imread('image.jpeg')

# Flip horizontally
flipped_h = cv2.flip(image, 1)

# Flip vertically
flipped_v = cv2.flip(image, 0)

# Flip both horizontally and vertically
flipped_hv = cv2.flip(image, -1)

# Show results
cv2.imshow("Original", image)
cv2.imshow("Flipped Horizontally", flipped_h)
cv2.imshow("Flipped Vertically", flipped_v)
cv2.imshow("Flipped Both", flipped_hv)

cv2.waitKey(0)
cv2.destroyAllWindows()
