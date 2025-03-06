import cv2
img=cv2.imread("images.jpeg")
b,g,r = cv2.split(img)
cv2.imshow("images blue",b)
cv2.imshow("images green",g)
cv2.imshow("images red",r)
cv2.waitKey(0)
cv2.destroyAllWindows()