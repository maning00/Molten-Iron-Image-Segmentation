import cv2
from matplotlib import pyplot as plt


def test():
    img = cv2.imread('data/img_240.png', 0)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    canny = cv2.Canny(img, 30, 50)

    plt.imshow(canny, cmap='gray')
    plt.show()


if __name__ == '__main__':
    test()
