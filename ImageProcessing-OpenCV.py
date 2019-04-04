# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Import the library
import cv2
import numpy as np

#Import the imaages
img = cv2.imread('C:/Users/100064135/Downloads/A.jpg',1)

#Show and display the images
cv2.imshow('image',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()

#Understand the image shape
print (img.shape)

#Cropping the image
crop_img = img[1200:1500,4100:6800]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Write the images
cv2.imwrite('C:/Users/100064135/Downloads/A_Cropped_3.png',crop_img)

#Convert the image type from "bmp" to "png"
from PIL import Image
img = Image.open('C:/Python27/image.bmp')
new_img = img.resize( (256, 256) )
new_img.save( 'C:/Python27/image.png', 'png')