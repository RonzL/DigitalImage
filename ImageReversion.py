import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont


# 给图片加上中文文字
def add_text(img, text):
    # 图像从cv格式转换成pil格式
    img_PIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    font = ImageFont.truetype(r"D:\Program Files\JetBrains\IntelliJ IDEA 2019.1\plugins\android\lib\layoutlib\data\fonts\NotoSansCJK-Regular.ttc", 30)
    # 文字输出位置
    position = (0, 0)
    # 输出内容
    draw = ImageDraw.Draw(img_PIL)
    # 设置文本位置、内容、字体、颜色
    draw.text(position, text, font=font, fill=(255, 10, 10))
    # 转换回cv格式
    img_OpenCV = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)
    return img_OpenCV


# 设置窗口大小可调整
def set_window(img, name, text):
    size = img.shape
    # 设置窗口大小可调
    cv2.namedWindow(name, 0)
    cv2.resizeWindow(name, size[1], size[0])
    # 添加文字并显示图片
    cv2.imshow(name, add_text(img, text))


# 主方法
if __name__ == '__main__':
    # 读取图像
    before = cv2.imread(r'C:\Users\Ronz\Desktop\DigitalImage\img\Fig0304(a)(breast_digital_Xray).tif')
    # 设置窗口可放缩，添加中文文字并打印原始图片
    set_window(before, 'before', '姓名刘壮志的原始图片')
    # 最大图像灰度值减去原图像，即可得到反转的图像
    after = 255 - before
    # 设置窗口可放缩，添加中文文字并打印反转后图片
    set_window(after, 'after', '姓名刘壮志的图像反转图片')
    cv2.waitKey(0)
