import cv2
import numpy as np
import os

saveDirect = "C:/Users/EWA/Documents/Open CV"

image1 = cv2.imread("Images/London_Eye.jpg", 1)
cv2.imshow("First Image", image1)

cv2.waitKey(0)

image2 = cv2.imread("Images/London_Eye.jpg", 0)

cv2.imshow("Grey Scale Image", image2)

cv2.waitKey(0)

imageGraph = np.ones((10, 10), np.uint8)

finalImage = cv2.erode(image1, imageGraph)

cv2.imshow("Eroded image", finalImage)

cv2.waitKey(0)

Edges1 = cv2.Canny(image1, 100, 200)
cv2.imshow("Edge Detection", Edges1)

cv2.waitKey(0)

os.chdir(saveDirect)
cv2.imwrite("EdgeDetectionLondon_Eye.jpg", Edges1)
print("file is successfully saved")