import cv2 as cv
import numpy as np

## Defines a blank image

blank = np.zeros((500, 500, 3), dtype = 'uint8') # blank image frame
cv.imshow('Blank', blank)

## Manipulate color channels of the image

blank[200:300, 300:400] = 0, 255, 255 # manipulate the color channels
cv.imshow('Color', blank)

## Draws a rectangle with 2 corners specified

cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness = 2) # Specify frame, start point and other corner point, thickness
cv.imshow('Ractangle', blank)

## Draws a circle with center and radius defined

cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness = -1 )
cv.imshow('Circle', blank)

## Draws a line with start and end specified

cv.line(blank, (100, 250), (20, 25), (255, 255, 255), thickness = 3)
cv.imshow('Line', blank)

# Writes a text on the frame

cv.putText(blank, 'OpenCV', (300, 400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness = 2)
cv.imshow('Text', blank)

cv.waitKey(0) # Frame will close in no time, this line holds your frame window for infinite time