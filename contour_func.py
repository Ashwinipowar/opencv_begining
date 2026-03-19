#here we gave the trianle image
#this o/p will show the border on the trianlge
import cv2
img=cv2.imread("image Resizing and Shaping\Edge detection an thresholding\image.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,210,255,cv2.THRESH_BINARY)

#find contours
#this underscore for variable which will we in future

contours , heirachy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,-1,(0,255,0),3)

cv2.imshow("contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
