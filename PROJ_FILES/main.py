import pandas
import numpy
from pyzbar.pyzbar import decode
import cv2

img=cv2.imread('1.png')

#code=decode(img)
#print(code)


#barcode.(what ever ) these are the attributes present in the thing
#you are just accessing it via this thing

for barcode in decode(img):
    print(barcode.data)
    #the data is comming in bytes
    #we need to convert that data
    my_data = barcode.data.decode('utf-8')
    print(my_data)
    #here my data was differnt so
    #AS IT WAS ALREADY FORMATTED HUST HAD A B IN FRONT

  #  print(barcode.rect)
  #  print(barcode.polygon)



    #To convert from bytes to str, you use .decode to
    # interpret the bytes using a specific encoding like UTF-8,
    # which will yield a str with readable characters.

