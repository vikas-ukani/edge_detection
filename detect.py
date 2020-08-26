import sys # system important
import cv2 # computer visualization
import numpy as np # multi-dimensional array # linear algebra

# Get arguments from command line.
image_name = sys.argv[1] # take an argument from command line

# Load Image and Convert into Gray
image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE) # read image with gray scal image
height, weight = image.shape

# Make sobel for better customization.
sobel_horizontal = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
laplacian = cv2.Laplacian(image, cv2.CV_64F)
canny = cv2.Canny(image, 50, 240)

# show all images MODELS here.
cv2.imshow("Original", image)
cv2.imshow("Sobel Horizontal", sobel_horizontal)
cv2.imshow("Sobel Vertical", sobel_vertical)
cv2.imshow("Laplacian", laplacian)
cv2.imshow("Canny", canny)

# Wait for EXIT ...
cv2.waitKey()

