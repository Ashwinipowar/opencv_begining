#we can draw the circle by giving the radius and another parameters
import cv2
image=cv2.imread("python.png")
if image is None:
    print("image not loaded")
else:
    print("image loaded successsfully")
    cv2.circle(image,(210,300),50,(0,0,255),-1)

    cv2.imshow("drawed circle",image)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
