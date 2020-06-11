from PIL import Image


def main1():
    i = 1
    j = 1
    img0 = Image.open("img_48.png")  # 读取系统的内照片
    img = img0.convert('RGB')
    width = img.size[0]  # 长度
    height = img.size[1]  # 宽度
    for i in range(0, width):  # 遍历所有长度的点
        for j in range(0, height):
            data = (img.getpixel((i, j)))
            #print(data)
            if data[0] == 0:  #背景
                img.putpixel((i, j), (255, 255, 255, 255))
            elif data[0] == 1:  #铁水
                img.putpixel((i, j), (0, 140, 210, 255))
            elif data[0] == 2:   #铁渣
                img.putpixel((i, j), (228, 0, 144, 255))
            elif data[0] == 3:   #扒渣铲
                img.putpixel((i, j), (0, 175, 77, 255))
            else:   #探针
                img.putpixel((i, j), (255, 225, 0, 255))
    #img = img.convert("RGB")
    img.save("testee1.png")  # 保存修改像素点后的图片


if __name__=='__main__':
    main1()
