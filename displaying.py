import cv2
 
image=cv2.imread("python.png")
  
if image is not None:
    cv2.imshow("image showin", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("image could not found")