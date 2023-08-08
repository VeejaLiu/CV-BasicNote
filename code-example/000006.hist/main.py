import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def gray_hist_calculation(image_path, name, extension):
    print("开始处理 images_path: ", image_path)

    # 读取图片
    img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 生成灰度直方图, img1为输入图像，[0]表示通道数，None表示没有使用mask，[256]表示灰度级数，[0,256]表示像素值范围
    histogram = cv2.calcHist(img_gray, [3], None, [256], [0, 256])

    # 画出直方图
    # 显示原始图像
    plt.subplot(1, 2, 1)
    plt.imshow(img_gray, cmap='gray')
    plt.title('Original Image(Gray)')

    # 显示直方图
    plt.subplot(1, 2, 2)
    plt.plot(histogram)
    plt.title('Gray Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    plt.tight_layout()

    # 保存结果
    if not os.path.exists('output'):
        os.mkdir('output')
    output_file_path = 'output/' + name + '-gray-hist-calculation' + extension
    plt.savefig(output_file_path)

    print("处理完成 images_path: ", image_path)

def color_hist_calculation(image_path, name, extension):
    print("开始处理 images_path: ", image_path)

    # 读取图片
    color_image = cv2.imread(image_path)

    # 分割通道
    # b, g, r = cv2.split(img)
    blue_channel = color_image[:, :, 0]
    green_channel = color_image[:, :, 1]
    red_channel = color_image[:, :, 2]

    # 计算各个通道的直方图
    blue_hist = cv2.calcHist([blue_channel], [0], None, [256], [0, 256])
    green_hist = cv2.calcHist([green_channel], [0], None, [256], [0, 256])
    red_hist = cv2.calcHist([red_channel], [0], None, [256], [0, 256])

    # 创建子图并绘制颜色直方图
    # 显示原始图像
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 4, 1)
    plt.imshow(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    # 显示蓝色通道图像
    plt.subplot(2, 4, 3)
    plt.imshow(blue_channel, cmap='gray')
    plt.title('Blue Channel')

    # 显示蓝色直方图
    plt.subplot(2, 4, 4)
    plt.plot(blue_hist, color='blue')
    plt.title('Blue Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    # 显示绿色通道图像
    plt.subplot(2, 4, 5)
    plt.imshow(green_channel, cmap='gray')
    plt.title('Green Channel')

    # 显示绿色直方图
    plt.subplot(2, 4, 6)
    plt.plot(green_hist, color='green')
    plt.title('Green Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    # 显示红色通道图像
    plt.subplot(2, 4, 7)
    plt.imshow(red_channel, cmap='gray')
    plt.title('Red Channel')

    # 显示红色直方图
    plt.subplot(2, 4, 8)
    plt.plot(red_hist, color='red')
    plt.title('Red Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    plt.tight_layout()

    # 保存结果
    if not os.path.exists('output'):
        os.mkdir('output')
    output_file_path = 'output/' + name + '-color-hist-calculation' + extension
    plt.savefig(output_file_path)

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
        # 根据文件全路径限定名获取文件名
        full_file_name = os.path.basename(image_path)
        # print(full_file_name)
        # 根据文件全路径限定名获取文件名和扩展名
        file_name, file_extension = os.path.splitext(full_file_name)
        gray_hist_calculation(image_path, file_name, file_extension)
        color_hist_calculation(image_path, file_name, file_extension)
