import cv2

images = cv2.imread("images.jpeg")
cropped = images[50:200,100:300] # crop [y1:y2, x1:x2] height and width of the images
cv2.imshow("Cropped Images: ",cropped)
cv2.waitKey()
cv2.destroyAllWindows()