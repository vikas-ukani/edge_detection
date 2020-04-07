import sys

import cv2
import numpy as np

image_name = sys.argv[1]

# Load Image and Convert into Gray
image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
height, weight = image.shape

sobel_horizontal = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
laplacian = cv2.Laplacian(image, cv2.CV_64F)
canny = cv2.Canny(image, 50, 240)

cv2.imshow("Original", image)
cv2.imshow("Sobel Horizontal", sobel_horizontal)
cv2.imshow("Sobel Vertical", sobel_vertical)
cv2.imshow("Laplacian", laplacian)
cv2.imshow("Canny", canny)

cv2.waitKey()

# print(laplacian)