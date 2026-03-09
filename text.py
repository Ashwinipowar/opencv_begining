import cv2
image=cv2.imread("python.png")
if image is None:
    print("image not loaded")
else:
    print("image loaded successsfully")
    
    cv2.putText(image,"HELLO ASHWNII",(50,60),cv2.FONT_HERSHEY_COMPLEX,1.2,(255,00),4)
    cv2.imshow("after text",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()