#can flip by horizontal
import cv2
image=cv2.imread("python.png")
if image is None:
    print("could not load image")
else:
    flipped_horizontal=cv2.flip(image,1)
    flipped_vertical=cv2.flip(image,0)
    flipped_both=cv2.flip(image,-1)

    cv2.imshow("origonal",image)
    cv2.imshow("flipped_horizontal",flipped_horizontal)
    cv2.imshow("flipped_vertical",flipped_vertical)
    cv2.imshow("both",flipped_both)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
