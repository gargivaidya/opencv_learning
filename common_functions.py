import cv2 as cv

img = cv.imread('./photos/Profile.jpg')
# cv.imshow('Cat', img)

## Convert to grayscale, only see intensity of image pixels
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # converts RGB ro grayscale
# cv.imshow('GrayCat', gray)

## Blurring images, removes noise in image using Gaussian blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('BlurCat', blur)

# Detects edge in image
canny = cv.Canny(img, 12, 100)
# cv.imshow('EdgeCat', canny)

## Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations = 1)
# cv.imshow('DilateCat', dilated)

## Eroding the dilated image
eroded = cv.erode(canny, (3, 3), iterations = 1)
cv.imshow('ErodeCat', eroded)

## Resize
resized = cv.resize(img, (100, 100), interpolation = cv.INTER_CUBIC)
# cv.imshow('ResizeCat', resized)

## Cropping
cropped = img[50:200, 100:200]
cv.imshow('CropCat', cropped)


cv.waitKey(0)

