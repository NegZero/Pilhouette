from PIL import Image, ImageFilter

#Image.open("IMG_2203.JPG").convert("L").point(lambda x: 0 if x<190 else 255, '1').save("result.JPG")
#Image.open("IMG_2203.JPG").filter(ImageFilter.FIND_EDGES).save("result.JPG")

import cv2;
import numpy as np;

"""
# Read image
im_in = cv2.imread("IMG_2203.JPG", cv2.IMREAD_GRAYSCALE);

# Threshold.
# Set values equal to or above 220 to 0.
# Set values below 220 to 255.

th, im_th = cv2.threshold(im_in, 180, 255, cv2.THRESH_BINARY_INV);

# Copy the thresholded image.
im_floodfill = im_th.copy()

# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255);

# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)

# Combine the two images to get the foreground.
im_out = cv2.bitwise_not(im_th | im_floodfill_inv)

# Display images.
cv2.imshow("Thresholded Image", im_th)
cv2.imshow("Floodfilled Image", im_floodfill)
cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
cv2.imshow("Foreground", im_out)
cv2.waitKey(0)

"""

im = cv2.imread("temp/raw.jpg", cv2.IMREAD_GRAYSCALE)
retr, thresh = cv2.threshold(im, 200, 255, cv2.THRESH_BINARY)

h,w = thresh.shape[:2]
slate = np.zeros((h+2,w+2), np.uint8)

cv2.copyMakeBorder(thresh, 1,1,1,1, cv2.BORDER_CONSTANT, dst=slate, value=(0,0,0))


cont = cv2.findContours(slate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]

slate1 = np.zeros((h+2, w+2), np.uint8)

cv2.drawContours(slate1, cont, -1, (1.0,1.0,1.0), cv2.FILLED)
cv2.imshow("thresh", thresh)
cv2.imshow("CU",slate1)
cv2.waitKey(0)

