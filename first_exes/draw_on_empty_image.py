import numpy as np
import cv2
import matplotlib.pyplot as plt

imPath = "target/myim.png"
imPath2 = "target/myim2.png"

image = np.zeros((100, 200, 3),np.uint8)
cv2.line(image, (5,5), (31,31), (0,0,255),3)
cv2.imwrite(imPath, image)

image = cv2.imread(imPath)
cv2.line(image, (50,50), (31,31), (0,255,0),3)
cv2.imwrite(imPath2, image)

dim = [image.shape[0], image.shape[1]]
imRed = np.zeros((dim[0], dim[1]),np.uint8)
for i in range(0, dim[0]):
    for j in range(0,dim[1]):
        imRed[i][j] = image[i][j][2]

cv2.imwrite("target/imRed.png", imRed)


img = cv2.imread("hsv.PNG")
mylist = []
for pixel in img[500]:
    mylist.append(pixel[1])

plt.plot(mylist)
plt.savefig('green_plot.png')
plt.show()