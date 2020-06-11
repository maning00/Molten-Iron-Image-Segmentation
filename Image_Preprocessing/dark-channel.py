import cv2
import sys
import numpy as np
import math
from datetime import datetime



def zmMinFilterGray(src, r=7):
    '''最小值滤波，r是滤波器半径'''
    return cv2.erode(src, np.ones((2 * r + 1, 2 * r + 1)))


def guidedfilter(I, p, r, eps):
    height, width = I.shape
    m_I = cv2.boxFilter(I, -1, (r, r))
    m_p = cv2.boxFilter(p, -1, (r, r))
    m_Ip = cv2.boxFilter(I * p, -1, (r, r))
    cov_Ip = m_Ip - m_I * m_p

    m_II = cv2.boxFilter(I * I, -1, (r, r))
    var_I = m_II - m_I * m_I

    a = cov_Ip / (var_I + eps)
    b = m_p - a * m_I

    m_a = cv2.boxFilter(a, -1, (r, r))
    m_b = cv2.boxFilter(b, -1, (r, r))
    return m_a * I + m_b


def Defog(m, r, eps, w, maxV1):                 # 输入rgb图像，值范围[0,1]
    '''计算大气遮罩图像V1和光照值A, V1 = 1-t/A'''
    V1 = np.min(m, 2)                           # 得到暗通道图像
    Dark_Channel = zmMinFilterGray(V1, 7)
    # cv2.imwrite('dark.png', Dark_Channel)    # 查看暗通道
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    V1 = guidedfilter(V1, Dark_Channel, r, eps)  # 使用引导滤波优化
    bins = 2000
    ht = np.histogram(V1, bins)                  # 计算大气光照A
    d = np.cumsum(ht[0]) / float(V1.size)
    for lmax in range(bins - 1, 0, -1):
        if d[lmax] <= 0.999:
            break
    A = np.mean(m, 2)[V1 >= ht[1][lmax]].max()
    V1 = np.minimum(V1 * w, maxV1)               # 对值范围进行限制
    return V1, A


def deHaze(m, r=81, eps=0.001, w=1, maxV1=0.85, bGamma=False):
    Y = np.zeros(m.shape)
    Mask_img, A = Defog(m, r, eps, w, maxV1)             # 得到遮罩图像和大气光照

    for k in range(3):
        Y[:,:,k] = (m[:,:,k] - Mask_img)/(1-Mask_img/A)  # 颜色校正
    Y = np.clip(Y, 0, 1)
    if bGamma:
        Y = Y ** (np.log(0.5) / np.log(Y.mean()))       # gamma校正,默认不进行该操作
    return Y


if __name__ == '__main__':
    #for i in range(283, 303):
        #nam = 'data/img_'
        #nam += str(i)
        #nam += '.png'
        #print(nam)
    nam = "imgg.png"
        # t1 = datetime.now()
    m = deHaze(cv2.imread(nam) / 255.0) * 255
    cv2.imwrite(nam, m)
        # t2 = datetime.now()
        # sub = (t2-t1).microseconds * pow(10,-6)
        # print(sub)
        # print(sub, 1.0/sub)
    # cv2.imshow("yes",m)
    # cv2.waitKey(0)

    sys.exit(0)
