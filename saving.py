import cv2

image=cv2.imread("python.png")


if image is not None:
    success=cv2.imwrite("output_savedimage.png",image)
    if success:
        print("hamne kiya save image")
    else:
        print("image save nahoi huii")
else:
    print("image load hi nahi hui")