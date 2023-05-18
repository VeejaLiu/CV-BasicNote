import cv2

import os

import cv2


def img_to_gray(images_path):
    # '/Users/liuweijia/IdeaProjects/CV-BasicNote/code-example/example-images/qq-snooker.png'
    print("开始处理 images_path: ", images_path)
    # 根据文件全路径限定名获取文件名
    full_file_name = os.path.basename(images_path)
    # print(full_file_name)
    # 根据文件全路径限定名获取文件名和扩展名
    file_name, file_extension = os.path.splitext(full_file_name)

    # 读取灰度图像
    gray_image = cv2.imread(images_path, cv2.IMREAD_GRAYSCALE)

    # 二值化
    ret, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    # 将二值化图像保存到output文件夹中
    # 如果output文件夹不存在，则创建
    if not os.path.exists('output'):
        os.mkdir('output')
    cv2.imwrite('output/' + file_name + '-binary' + file_extension, binary_image)
    # 打印阈值
    print(ret)

    # # 在一个窗口中显示二值化后的图像
    # cv2.imshow('Binary Image', binary_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


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
        img_to_gray(image_path)
