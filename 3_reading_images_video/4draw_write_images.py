import cv2
import numpy as np

blank = np.zeros((500, 500), dtype='uint8')

img = cv2.imread('assets/fotos/cat.jpg')
cv2.imshow('gato', blank)

cv2.waitKey(0)