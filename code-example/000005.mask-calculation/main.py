import os

import cv2
import numpy as np


def mask_calculation(image_path):
    # '/Users/liuweijia/IdeaProjects/CV-BasicNote/code-example/example-images/qq-snooker.png'
    print("开始处理 images_path: ", image_path)
    # 根据文件全路径限定名获取文件名
    full_file_name = os.path.basename(image_path)
    # print(full_file_name)
    # 根据文件全路径限定名获取文件名和扩展名
    file_name, file_extension = os.path.splitext(full_file_name)

    # 读取图片
    img1 = cv2.imread(image_path)

    # img1.shape[0] 为图片的高度. img1.shape[1] 为图片的宽度, 分离变量
    height, width = img1.shape[0], img1.shape[1]
    # 计算图片的中心点的横纵坐标
    center_x, center_y = width // 2, height // 2

    # 创建一个和图片一样大小的掩码图像
    mask = np.zeros((height, width), dtype=np.uint8)
    # 画一个圆形的掩码，圆心为图片中心，半径为原图片横纵坐标的最大值，颜色为白色，厚度为-1，表示填充
    cv2.circle(mask, (center_x, center_y), min(center_x, center_y), (255, 255, 255), -1)

    # 执行 AND 操作, 即掩码图像与原图像进行与操作, 结果为掩码图像中白色部分对应的原图像中的像素值
    result = cv2.bitwise_and(img1, img1, mask)

    # 用白色填充外部
    white = 255
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if not mask[i, j]:
                result[i, j] = white

    # 将原图和掩码图片和结果并排显示，hstack()表示水平拼接
    img_compare = np.hstack((img1, np.dstack((mask, mask, mask)), result))

    # 保存结果
    # 将灰度图像保存到output文件夹中
    # 如果output文件夹不存在，则创建
    if not os.path.exists('output'):
        os.mkdir('output')
    cv2.imwrite('output/' + file_name + '-mask-calculation' + file_extension, img_compare)

    # cv2.imshow('mask', img_compare)
    # cv2.waitKey(0)
    print("处理完成 images_path: ", image_path)


if __name__ == '__main__':
    # 获取当前工作目录
    current_path = os.getcwd()
    # print(current_path)
    # 获取上一层目录
    parent_path = os.path.dirname(current_path)
    # print(parent_path)
    # 获取上一层目录中的example-images目录
    example_images_path = os.path.join(parent_path, 'example-images')
    # print(example_images_path)
    # 获取其中所有文件
    files = os.listdir(example_images_path)
    # print(files)

    all_images_path = []
    # 遍历所有文件
    for file in files:
        # 获取文件的绝对路径
        file_path = os.path.join(example_images_path, file)
        print(file_path)
        # 将文件的绝对路径添加到列表中
        all_images_path.append(file_path)

    for image_path in all_images_path:
        mask_calculation(image_path)
