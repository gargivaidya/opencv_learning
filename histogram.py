import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./photos/city.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

## Computing histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])


plt.figure()
plt.plot(gray_hist)
plt.show()
cv.waitKey(0)