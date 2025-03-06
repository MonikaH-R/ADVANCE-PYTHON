import cv2
images = cv2.imread('images.jpeg')
bright_images = cv2.convertScaleAbs(images,alpha=40.0,beta=800) #beta=50% brightness in the image((+) increase)(-) decrease)
dark_image = cv2.convertScaleAbs(images,alpha=40.0,beta=800)
cv2.imshow("Display Window", images)
cv2.waitKey(0)
cv2.destroyAllWindows()