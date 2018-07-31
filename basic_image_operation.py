import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = '/Data/' + 'test.jpg'
dim = (560,560)
# Load an color image in grayscale
grayimg = cv2.imread(image_path,0)
gresize = cv2.resize(grayimg, dim, interpolation = cv2.INTER_AREA)
inensity_value_g = gresize[559,1]

print "inensity_value_g",inensity_value_g
gimgshape = gresize.shape
print "gimgshape",gimgshape
cv2.imshow('grayimg',gresize)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load an color image
colorimage = cv2.imread(image_path,1)

cresize = cv2.resize(colorimage, dim, interpolation = cv2.INTER_AREA)
inensity_value_c = cresize[100,100]
print "inensity_value_c",inensity_value_c
cimgshape = cresize.shape
print "cimgshape",cimgshape
cv2.imshow('colorimage',cresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
