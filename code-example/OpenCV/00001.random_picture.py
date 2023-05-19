import cv2
import numpy as np

# 这一行代码创建了一个大小为100x100的随机矩阵，数据类型为float32，数值范围在0到1之间，然后将其乘以1e6来扩大数值范围。
m1 = np.random.rand(300, 300).astype(np.float32) * 1e6

# 展示图片
cv2.imshow("m1", m1)

# 这一行代码使用cv2.minMaxLoc()函数找到矩阵中的最小值和最大值，返回值包括最小值、最大值、最小值的位置和最大值的位置。
minRange, MaxRange, mLoc, MLoC = cv2.minMaxLoc(m1)

# 这一行代码将矩阵缩放到0到255的范围内，并将其数据类型转换为uint8，以便使用cv2.imshow()函数显示图像。
img1 = np.uint8((m1 - minRange) * 255.0 / (MaxRange - minRange))

# 展示图片
cv2.imshow("result", img1)

# 等待显示
cv2.waitKey(0)

# 销毁窗口
cv2.destroyAllWindows()