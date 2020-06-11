import cv2
import numpy as np
from matplotlib import pyplot as plt


def test():
    img = cv2.imread('data/img_160.png', 0)  # 0是第二个参数，将其转为灰度图
    # 应用5种不同的阈值方法
    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, th1, th2, th3, th4, th5]

    # 使用Matplotlib显示
    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i], fontsize=8)
        plt.xticks([]), plt.yticks([])  # 隐藏坐标轴

    plt.show()


if __name__ == '__main__':
    test()
