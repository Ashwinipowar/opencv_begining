import cv2
 
image=cv2.imread("python.png")
  
if image is None:
    print("image not found error")

else:
    print("image is found")