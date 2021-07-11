import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8') # blank image frame
# cv.imshow('Blank', blank)

blank[200:300, 300:400] = 0, 255, 255 # manipulate the color channels
# cv.imshow('Color', blank)

cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness = 2) # Specify frame, start point and other corner point, thickness
# cv.imshow('Ractangle', blank)

cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness = -1 )
cv.imshow('Circle', blank)

cv.waitKey(0)