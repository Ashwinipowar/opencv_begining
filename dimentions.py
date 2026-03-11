import cv2

image=cv2.imread("python.png")

if image is not None:
    h,w, c =image.shape

    print(f"image loaded:\nHeight: {h}\nwidth:{w}\nchannel:{c}")
else:
    print("image ke dimention dikha nahi pahe and load hi nahi hui")