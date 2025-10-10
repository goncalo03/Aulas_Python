import cv2
import numpy as np
import os

folder = "Files"
file = "moedas.jpg"

image = cv2.imread(os.path.join(folder, file))
cv2.imshow("image", image)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray = (image_gray/255.0).astype(np.float32)

Mx = np.array([[-1,0,1],
               [-2,0,2],
               [-1,0,1]])

My = np.array([[-1,-2,-1],
               [0,0,0],
               [1,2,1]])

dx = cv2.filter2D(image_gray, -1, kernel = Mx)
dy = cv2.filter2D(image_gray, -1, kernel = My)

gradient_magnitude = np.sqrt(dx**2 + dy**2)
cv2.imshow("gradient magnitude", gradient_magnitude)

gradient_direction = np.arctan(dy/dx)
#cv2.imshow("gradient direction", (gradient_direction + np.pi/2)/np.pi)

#cv2.imshow("dx", dx)
#cv2.imshow("dy", dy)

max_gradient_magnitude = np.max(gradient_magnitude)

threshold = max_gradient_magnitude / 2.0

def on_change_threshold(val):
    global threshold
    threshold = val/100.0
    ret, image_thresholded = cv2.threshold(src=gradient_magnitude,
                                         thresh=threshold,
                                         maxval=threshold,
                                         type=cv2.THRESH_BINARY)

    cv2.imshow("image_thresholded", image_thresholded)

cv2.namedWindow("image_thresholded")
cv2.createTrackbar("image_thresholded",
                   "image_thresholded",
                   int(threshold * 100),
                   int(max_gradient_magnitude * 100),
                   on_change_threshold)

cv2.waitKey(0)