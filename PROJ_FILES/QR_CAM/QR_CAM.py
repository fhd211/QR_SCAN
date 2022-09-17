import pandas
import numpy
from pyzbar.pyzbar import decode
import cv2

#img=cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3,650)
cap.set(4,480)

while True:
    success, img = cap.read()
    for barcode in decode(img):
        #print(barcode.data)
        my_data = barcode.data.decode('utf-8')

        print(my_data)
        pts = numpy.array([barcode.polygon], numpy.int32)
        pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2=barcode.rect

        #cv2.putText(img,my_data,(pts2[0],pts2[1]),cv2.FONT)

    cv2.imshow('result', img)
    cv2.waitKey(1)






#cv2.imshow('result',img)
#cv2.waitKey(1)
