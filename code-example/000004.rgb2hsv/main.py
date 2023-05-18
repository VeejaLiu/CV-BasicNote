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

    # 读取图像
    img = cv2.imread(images_path)

    # 将图像从RGB颜色空间转换到HSV颜色空间
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    # 拆分通道
    h, s, v = cv2.split(img_hsv)

    # 在 HSV 颜色空间的图像上加上 H, S, V 三个通道的标签，并保存处理后的图像
    cv2.putText(img_hsv, 'HSV', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(h, 'H', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(s, 'S', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(v, 'V', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

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

    # 打印各个图片的shape和dtype
    print('img.shape: ', img.shape, 'img.dtype: ', img.dtype)
    print('img_hsv.shape: ', img_hsv.shape, 'img_hsv.dtype: ', img_hsv.dtype)
    print('h.shape: ', h.shape, 'h.dtype: ', h.dtype)
    print('s.shape: ', s.shape, 's.dtype: ', s.dtype)
    print('v.shape: ', v.shape, 'v.dtype: ', v.dtype)

    # 拼接所有图片，包括原图，按照上面两张，分别为原图和HSV颜色空间的图片，下面三张，分别是三个通道的图片
    img_compare = cv2.hconcat([img,
                               img_hsv,
                               cv2.cvtColor(h, cv2.COLOR_GRAY2BGR),
                               cv2.cvtColor(s, cv2.COLOR_GRAY2BGR),
                               cv2.cvtColor(v, cv2.COLOR_GRAY2BGR)
                               ])

    # 将灰度图像保存到output文件夹中
    # 如果output文件夹不存在，则创建
    if not os.path.exists('output'):
        os.mkdir('output')
    cv2.imwrite('output/' + file_name + '-hsv' + file_extension, img_compare)

    # # show gray image
    # cv2.imshow('HSV compare', img_compare)
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
