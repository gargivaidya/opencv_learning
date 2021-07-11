import cv2 as cv

img = cv.imread('./photos/Profile.jpg')
cv.imshow('Cat', img)

## Convert to grayscale, only see intensity of image pixels
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # converts RGB ro grayscale
cv.imshow('GrayCat', gray)

## Blurring images, removes noise in image using Gaussian blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('BlurCat', blur)

cv.waitKey(0)

