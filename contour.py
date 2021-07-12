import cv2 as cv
import numpy as np

img = cv.imread('./photos/city.png')
blank = np.zeros(img.shape, dtype='uint8')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)

ret, thresh = cv.threshold(canny, 125, 255, cv.THRESH_BINARY)

#  Returns al list of contours and hierarchical representation of contours
# RETR_EXTERNAL - returns external contours, RETR_TREE - retruns hierarchical contours under a contour
# Approximation method - 
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours', blank)

cv.waitKey(0)