import cv2

# 读取图像
img = cv2.imread('example.jpeg')

# 将图像转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 将灰度图像保存到文件
cv2.imwrite('gray.jpg', gray)
