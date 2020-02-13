import numpy as np
import cv2

normalPath = "input/normal.JPG"
underPath = "input/under.JPG"
src_img = cv2.imread(underPath)
hsv = cv2.cvtColor(src_img, cv2.COLOR_BGR2HSV)
img = hsv
lower = np.array([40,130,100])
upper = np.array([90,255,255])
mask = cv2.inRange(img, lower, upper)
filtered_mask = cv2.medianBlur(mask, 9)
masked = cv2.bitwise_and(src_img, src_img, mask = filtered_mask)

cv2.imwrite("output/ex1.JPG",masked)