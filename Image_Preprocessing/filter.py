import numpy as np
import cv2
from matplotlib import pyplot as plt


def test():
    image = cv2.imread("data/img_80.png")
    # cv2.imshow("Original", image)
    # cv2.waitKey(0)
    # 领域均值滤波
    blurred = np.hstack([cv2.blur(image, (1, 1)),
                         cv2.blur(image, (2, 2)),
                         cv2.blur(image, (3, 3))
                         ])
    plt.subplot(5, 1, 1), plt.imshow(blurred), plt.title('avg'), plt.xticks([]), plt.yticks([])

    blurred2 = np.hstack([cv2.GaussianBlur(image, (7, 7), 0), # 高斯滤波
                          cv2.GaussianBlur(image, (11, 11), 0),
                          cv2.GaussianBlur(image, (15, 15), 0)
                          ])

    plt.subplot(5, 1, 2), plt.imshow(blurred2), plt.title('Gaussian'), plt.xticks([]), plt.yticks([])

    blurred3 = np.hstack([cv2.medianBlur(image, 7), # 中值滤波
                          cv2.medianBlur(image, 11),
                          cv2.medianBlur(image, 15)
                          ])

    plt.subplot(5, 1, 3), plt.imshow(blurred2), plt.title('Median'), plt.xticks([]), plt.yticks([])

    blurred4 = np.hstack([cv2.bilateralFilter(image, 9, 21, 21),  # 双边滤波
                          cv2.bilateralFilter(image, 15, 31, 31),
                          cv2.bilateralFilter(image, 19, 41, 41)
                          ])
    #cv2.imshow("Averaged", blurred4)
    #cv2.waitKey(0)
    plt.subplot(5, 1, 4), plt.imshow(blurred2), plt.title('Bilateral'), plt.xticks([]), plt.yticks([])
    plt.subplot(5, 1, 5), plt.imshow(image), plt.title('Origin'), plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == '__main__':
    test()
