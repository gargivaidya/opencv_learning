import cv2 as cv # Import OpenCV package

img = cv.imread('./photos/Profile.jpg') # Store pixel data from jpg in a variable
cv.imshow('Cat', img) # Display image in new window
cv.waitKey(0) # Waits for infinitie amount of time for a key press