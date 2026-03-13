import cv2

image=cv2.imread("man threshold.png",cv2.IMREAD_GRAYSCALE)

ret , thresh_img=cv2.threshold(image,120,255,cv2.THRESH_BINARY)

cv2.imshow("original_image",image)
cv2.imshow("threshold image",thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""hamare man pe threshold lower qand upper decide karenge 
range
here we set limit lower is 120
and upper is 255
"""

