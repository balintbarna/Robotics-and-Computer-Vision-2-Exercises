import numpy as np
import cv2

imPath = "flamingo.jpg"
imPath2 = "target/separated.png"

flamingo = cv2.imread(imPath)
flamHSV = cv2.cvtColor(flamingo, cv2.COLOR_BGR2HSV)

lower = np.array([20,0,0])
upper = np.array([40,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(flamHSV, lower, upper)
mask = 255 - mask

# Bitwise-AND mask and original image
separated = cv2.bitwise_and(flamingo, flamingo, mask = mask)

cv2.imwrite(imPath2, separated)