import cv2 as cv
import numpy as np

img = cv.imread('./photos/Profile.jpg')
# cv.imshow('Cat', img)

def translate(img, x, y):
	transMat = np.float32([[1, 0, x], [0, 1, y]])
	dimensions = (img.shape[1], img.shape[0])
	return cv.warpAffine(img, transMat, dimensions)

def rotate(img, angle, rotPoint = None):
	(height, width) = img.shape[:2]

	if rotPoint is None:
		rotPoint = (width//2, height//2)

	rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
	dimensions = (width, height)

	return cv.warpAffine(img, rotMat, dimensions)

# -x left
# -y up
# x right
# y down

translated = translate(img, 100, 20)
cv.imshow('TranslateCat', translated)

rotated = rotate(img, 45)
cv.imshow('RotatedCat', rotated)

cv.waitKey(0)
