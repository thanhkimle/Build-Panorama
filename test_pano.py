import numpy as np
import scipy as sp
import cv2
import scipy.ndimage as nd
import panorama as pano

img = cv2.imread('test.png', 1)
cv2.imshow('img', img)
mask = pano.createImageMask(img)
cv2.imshow('mask', mask)
key = cv2.waitKey(0)

# img = cv2.imread("lena.jpg", 0)
# h, w, d = np.atleast_3d(img).shape
# #cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(d)
# # print(np.atleast_3d(img.shape))
# # c = pano.getImageCorners(img)
# # (tl1, tr1, br1, bl1) = c
# # # print(c)
# # # print(tr1[0, 0])
# # # print(tr1[0, 1])
# # xy = np.array([[1], [2]])
# # print(xy[1])