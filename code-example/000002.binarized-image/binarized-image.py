import cv2

# 读取灰度图像
gray_image = cv2.imread('gray.jpg', cv2.IMREAD_GRAYSCALE)

# 二值化
ret, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# 写入文件
cv2.imwrite('binarized_image.jpg', binary_image)

# 打印阈值
print(ret)

# 在一个窗口中显示二值化后的图像
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
