import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

folder = "Files"
files = []
files.append("baboon.png")
files.append("cao.jpg")
files.append("lena.png")
files.append("Sharbat_Gula.jpg")
files.append("moedas.jpg")

kernel_media_3x3 = 1/9 * np.ones((3, 3))
kernel_media_5x5 = 1/25 * np.ones((5, 5))
kernel_media_7x7 = 1/49 * np.ones((7, 7))

kernel_highpass_A = 1/6 * np.array([[0, -1, 0],
                                    [-1, 4, -1],
                                    [0, -1, 0]])

kernel_highpass_B = 1/9 * np.array([[-1, -1, -1],
                                    [-1,  8, -1],
                                    [-1, -1, -1]])

kernel_highpass_C = 1/16 * np.array([[-1, -2, -1],
                                     [-2,  12, -2],
                                     [-1, -2, -1]])

for i, file in enumerate(files):
    image = cv2.imread(os.path.join(folder, file))
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image_gray_lowpass_3x3 = cv2.filter2D(src=image_gray,
                                          ddepth=-1,
                                          kernel=kernel_media_3x3)
    image_gray_lowpass_5x5 = cv2.filter2D(src=image_gray,
                                          ddepth=-1,
                                          kernel=kernel_media_5x5)
    image_gray_lowpass_7x7 = cv2.filter2D(src=image_gray,
                                          ddepth=-1,
                                          kernel=kernel_media_7x7)

    image_blur_3x3 = cv2.blur(image_gray, (3, 3))
    image_blur_5x5 = cv2.blur(image_gray, (5, 5))
    image_blur_7x7 = cv2.blur(image_gray, (7, 7))

    gaussian_blur_3x3 = cv2.GaussianBlur(image_gray, (3, 3), 0)
    gaussian_blur_5x5 = cv2.GaussianBlur(image_gray, (5, 5), 0)
    gaussian_blur_7x7 = cv2.GaussianBlur(image_gray, (7, 7), 0)

    median_blur_3x3 = cv2.medianBlur(image_gray, 3)
    median_blur_5x5 = cv2.medianBlur(image_gray, 5)
    median_blur_7x7 = cv2.medianBlur(image_gray, 7)

    image_gray_highpass_A = cv2.filter2D(src=image_gray,
                                          ddepth=-1,
                                          kernel=kernel_highpass_A)
    image_gray_highpass_B = cv2.filter2D(src=image_gray,
                                          ddepth=-1,
                                          kernel=kernel_highpass_B)
    image_gray_highpass_C = cv2.filter2D(src=image_gray,
                                          ddepth=-1,
                                          kernel=kernel_highpass_C)

    plt.subplots(dpi=300, layout='constrained')
    plt.axis('off')

    plt.subplot(5, 4, 1)
    plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB))
    plt.title("image")
    plt.axis('off')

    plt.subplot(5, 4, 2)
    plt.imshow(cv2.cvtColor(image_gray_lowpass_3x3, cv2.COLOR_BGR2RGB))
    plt.title("low-pass image 3x3")
    plt.axis('off')

    plt.subplot(5, 4, 3)
    plt.imshow(cv2.cvtColor(image_gray_lowpass_5x5, cv2.COLOR_BGR2RGB))
    plt.title("low-pass image 5x5")
    plt.axis('off')

    plt.subplot(5, 4, 4)
    plt.imshow(cv2.cvtColor(image_gray_lowpass_7x7, cv2.COLOR_BGR2RGB))
    plt.title("low-pass image 7x7")
    plt.axis('off')

    plt.subplot(5, 4, 6)
    plt.imshow(cv2.cvtColor(image_blur_3x3, cv2.COLOR_BGR2RGB))
    plt.title("blur 3x3")
    plt.axis('off')

    plt.subplot(5, 4, 7)
    plt.imshow(cv2.cvtColor(image_blur_5x5, cv2.COLOR_BGR2RGB))
    plt.title("blur 5x5")
    plt.axis('off')

    plt.subplot(5, 4, 8)
    plt.imshow(cv2.cvtColor(image_blur_7x7, cv2.COLOR_BGR2RGB))
    plt.title("blur 7x7")
    plt.axis('off')

    plt.subplot(5, 4, 10)
    plt.imshow(cv2.cvtColor(gaussian_blur_3x3, cv2.COLOR_BGR2RGB))
    plt.title("gaussian blur 3x3")
    plt.axis('off')

    plt.subplot(5, 4, 11)
    plt.imshow(cv2.cvtColor(gaussian_blur_5x5, cv2.COLOR_BGR2RGB))
    plt.title("gaussian blur 5x5")
    plt.axis('off')

    plt.subplot(5, 4, 12)
    plt.imshow(cv2.cvtColor(gaussian_blur_7x7, cv2.COLOR_BGR2RGB))
    plt.title("gaussian blur 7x7")
    plt.axis('off')

    plt.subplot(5, 4, 14)
    plt.imshow(cv2.cvtColor(median_blur_3x3, cv2.COLOR_BGR2RGB))
    plt.title("median blur 3x3")
    plt.axis('off')

    plt.subplot(5, 4, 15)
    plt.imshow(cv2.cvtColor(median_blur_5x5, cv2.COLOR_BGR2RGB))
    plt.title("median blur 5x5")
    plt.axis('off')

    plt.subplot(5, 4, 16)
    plt.imshow(cv2.cvtColor(median_blur_7x7, cv2.COLOR_BGR2RGB))
    plt.title("median blur 7x7")
    plt.axis('off')

    plt.subplot(5, 4, 18)
    plt.imshow(cv2.cvtColor(10*image_gray_highpass_A, cv2.COLOR_BGR2RGB))
    plt.title("highpass A")
    plt.axis('off')

    plt.subplot(5, 4, 19)
    plt.imshow(cv2.cvtColor(10*image_gray_highpass_B, cv2.COLOR_BGR2RGB))
    plt.title("highpass B")
    plt.axis('off')

    plt.subplot(5, 4, 20)
    plt.imshow(cv2.cvtColor(10*image_gray_highpass_C, cv2.COLOR_BGR2RGB))
    plt.title("highpass C")
    plt.axis('off')

    plt.show()




