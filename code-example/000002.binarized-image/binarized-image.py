import cv2

# 读取灰度图像
gray = cv2.imread('gray.jpg', cv2.IMREAD_GRAYSCALE)

# 二值化
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 写入文件
cv2.imwrite('binarized_image.jpg', binary)

# 写入阈值
print(ret)

# 在一个窗口中显示二值化后的图像
cv2.imshow('binary', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
