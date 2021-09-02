import numpy as np
import cv2

h, w = 300, 300
canvas = np.zeros((h, w, 3), dtype="uint8")
red = (0, 0, 255)
black = (0, 0, 0)
green = (0, 255, 0)

for i in range(0, h, 10):
    for j in range(0, w, 10):
        if (i+j) % 2 == 1:
            cv2.rectangle(canvas, (10*i, 10*j), (10*i+10, 10*j+10), red, -1)

cv2.circle(canvas, (h//2, w//2), 50, green, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
