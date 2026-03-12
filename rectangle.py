import cv2
image=cv2.imread("python.png")
if image is None:
    print("image not loaded")
else:
    print("image loaded successsfully")
    pt1=(20,50)
    pt2=(60,100)
    color=(0,255,0)
    thickness=4

    cv2.rectangle(image,pt1,pt2,color,thickness)
    cv2.imshow("drawed rectange",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()