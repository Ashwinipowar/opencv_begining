import cv2
image=cv2.imread("python.png")
if image is None:
    print("image not loaded")

else:
    (h,w)= image.shape[:2]#iska matlab hai 2 hi value lenge ham
    center=(w//2,h//2)
    m=cv2.getRotationMatrix2D(center,90,1.0)
    rotated=cv2.warpAffine(image,m,(w,h))

    cv2.imshow("original", image)
    cv2.imshow("rotated 90 degree",rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
