import cv2
import numpy as np

im = cv2.imread("IMG_2203.JPG", cv2.IMREAD_GRAYSCALE)
bim = cv2.copyMakeBorder(im, 1,1,1,1, cv2.BORDER_CONSTANT, value=[255,255,255])

cv2.imshow("bim", bim)

retr, thresh = cv2.threshold(bim, 210, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("thresh", thresh)

cont = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

cv2.drawContours(thresh, cont, -1, [255, 255, 255], cv2.FILLED)
cv2.imshow("filled", thresh)
cv2.imwrite("filled.png", thresh)

cv2.waitKey(0)
