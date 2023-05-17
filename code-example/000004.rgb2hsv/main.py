import cv2

# 读取图像
img = cv2.imread('example.jpeg')

# 将图像从RGB颜色空间转换到HSV颜色空间
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# 拆分通道
h, s, v = cv2.split(img_hsv)

# 在 HSV 颜色空间的图像上加上 H, S, V 三个通道的标签，并保存处理后的图像
cv2.putText(img_hsv, 'HSV', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(h, 'H', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(s, 'S', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(v, 'V', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imwrite('img_hsv.jpg', img_hsv)
cv2.imwrite('img_h.jpg', h)
cv2.imwrite('img_s.jpg', s)
cv2.imwrite('img_v.jpg', v)

# # 显示HSV颜色空间的图像
# cv2.imshow('img HSV', img_hsv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # 逐个通道显示
# cv2.imshow('img H', h)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# cv2.imshow('img S', s)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# cv2.imshow('img V', v)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 把五张图片拼在一个图片里面，并保存在文件中
img_hsv = cv2.imread('img_hsv.jpg')
img_h = cv2.imread('img_h.jpg')
img_s = cv2.imread('img_s.jpg')
img_v = cv2.imread('img_v.jpg')

# 拼接所有图片，包括原图，按照上面两张，分别为原图和HSV颜色空间的图片，下面三张，分别是三个通道的图片
img_compare = cv2.hconcat([img, img_hsv, img_h, img_s, img_v])

# 保存图片
cv2.imwrite('img_compare.jpg', img_compare)

# 显示图片，从屏幕最左边开始显示
cv2.imshow('Compare Images', img_compare)
cv2.moveWindow('Compare Images', 0, 0)
cv2.waitKey(0)
cv2.destroyAllWindows()
