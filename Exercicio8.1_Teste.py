import cv2
import numpy as np
import os

from PyQt6.QtGui import QGradient

folder = "Files"
file = "moedas.jpg"

image = cv2.imread(os.path.join(folder, file))
cv2.imshow("image", image)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray = image_gray/255.0
cv2.imshow("gray", image_gray)

def on_track_bar(value):
    threshold = value/100.0
    ret, image_thresholded = cv2.threshold(image_gray,
                                           threshold,
                                           1,
                                           cv2.THRESH_BINARY)
    cv2.imshow("image_thresholded", image_thresholded)

    image_thresholded = (image_thresholded*255).astype(np.uint8)

    contours, hierarchy = cv2.findContours(image_thresholded,
                                            cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_NONE)

    image_contours = np.zeros(image_thresholded.shape, np.uint8)
    cv2.drawContours(image = image_contours,
                     contours = contours,
                     contourIdx=-11,
                     color=255,
                     thickness=-1)

    cv2.imshow("image_contours", image_contours)

    image_contours2 = np.zeros(image_thresholded.shape, np.uint8)
    image_circles = np.zeros(image.shape, np.uint8)
    for i in range(len(contours)):
        cv2.drawContours(image = image_contours2,
                         contours=contours,
                         contourIdx=i,
                         color=255,
                         thickness=2)
        contour = contours[i]
        c_area = cv2.contourArea(contour)
        p = cv2.arcLength(contour, closed=True)
        print("Contour {} area = {}; perimeter={} ".format(i, c_area, p))

        M = cv2.moments(contour)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.circle(image_circles, (cx, cy), 2, (0, 255, 255), -1)

    cv2.imshow("image_contours2", image_contours2)
    cv2.imshow("image_circles", image_circles)

cv2.namedWindow("image_thresholded")
cv2.createTrackbar("Threshold",
                   "image_thresholded",
                   50,
                   100,
                   on_track_bar)

cv2.waitKey(0)