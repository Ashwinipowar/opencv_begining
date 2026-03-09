import cv2
image=cv2.imread("python.png")

if image is None:
    print("image nahi mili")
else:
    resize=cv2.resize(image,(300,300))
    cv2.imshow("original image",image)
    cv2.imshow("resized_image",resize)
    cv2.imwrite("resized_output.png",resize)
