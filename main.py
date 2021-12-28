"""
Main
Bởi: NKDuy
"""

import cv2
import nkdcv  # pip install nkdcv-python==1.3.5
from nkdcv.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(cv2.CAP_PROP_FPS, 60)
segmentor = SelfiSegmentation()
fpsReader = nkdcv.FPS()

listImg = os.listdir("Images")
print(listImg)
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'Images/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.8)

    imgStacked = nkdcv.stackImages([img, imgOut], 2, 1)
    _, imgStacked = fpsReader.update(imgStacked, color=(0, 0, 255))
    print(indexImg)

    cv2.imshow("Image", imgStacked)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg < len(imgList) - 1:
            indexImg += 1
    elif key == ord('q'):
        break
