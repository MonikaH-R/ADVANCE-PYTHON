import cv2
img=cv2.imread("image1.jpeg")
roi=cv2.selectROI("Select Region",img,fromCenter=False,showCrosshair=True)
x,y,w,h=roi
cropped_img=img[y:y+h,x:x+w]
cv2.imshow("Cropped Image1",cropped_img)
cv2.imwrite("cropped.jpeg",cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()