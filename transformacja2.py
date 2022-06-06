import cv2

image = cv2.imread('small_beach.jpg')

alpha = 1.6 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)

adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

cv2.imshow('original', image)
cv2.imshow('adjusted', adjusted)
cv2.waitKey()