import cv2
image=cv2.imread("grayscale.png")
edge=cv2.Canny(image,50,150)

cv2.imshow("original image",image)
cv2.imshow("edged image",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()