from cv2 import cv2
import numpy as np

img = cv2.imread(r'imagem/exemplo2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 1)
decalque = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)

cv2.imshow('Original', img)
cv2.imshow('Decalque', decalque)
cv2.waitKey(0)
cv2.destroyAllWindows()