import cv2
import numpy as np

# 读取上层目录中example-images目录中的lena.png图片
img = cv2.imread("../example-images/lena.png")

# 展示图片
cv2.imshow("lena", img)

# 获取图片的高度和宽度
height, width = img.shape[:2]

# 打印图片的高度和宽度
print("height: %d, width: %d" % (height, width))

# 获取图片中心点的坐标
centerX, centerY = height // 2, width // 2

# 打印图片中心点的坐标
print("centerX: %d, centerY: %d" % (centerX, centerY))

# 获取图片中心点的像素值
centerPixel = img[centerX, centerY]

# 以中心像素为中心，打印周围九个点像素值
# leftTop, top, rightTop
leftTop = img[centerX - 1, centerY - 1]
top = img[centerX - 1, centerY]
rightTop = img[centerX - 1, centerY + 1]
print("%s, %s, %s" % (leftTop, top, rightTop))
# left, center, right
left = img[centerX, centerY - 1]
center = img[centerX, centerY]
right = img[centerX, centerY + 1]
print("%s, %s, %s" % (left, center, right))
# leftBottom, bottom, rightBottom
leftBottom = img[centerX + 1, centerY - 1]
bottom = img[centerX + 1, centerY]
rightBottom = img[centerX + 1, centerY + 1]
print("%s, %s, %s" % (leftBottom, bottom, rightBottom))

# 绘制一张图片，图片大小为300x300，分别为上面的九个颜色，方位对应起来
# 创建一个300x300的空白图片
img1 = np.zeros((300, 300, 3), np.uint8)
img1[0:100, 0:100] = leftTop
img1[0:100, 100:200] = top
img1[0:100, 200:300] = rightTop
img1[100:200, 0:100] = left
img1[100:200, 100:200] = center
img1[100:200, 200:300] = right
img1[200:300, 0:100] = leftBottom
img1[200:300, 100:200] = bottom
img1[200:300, 200:300] = rightBottom

# 展示图片
cv2.imshow("result", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
