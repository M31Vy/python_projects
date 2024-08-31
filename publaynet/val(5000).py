import os
import random
import shutil
 
def copy_random_files(images_folder, labels_folder, val_images_folder, train_images_folder, val_labels_folder, train_labels_folder):
    # 获取源文件夹中的所有文件名
    files = os.listdir(images_folder)
    # 打乱文件列表的顺序
    random.shuffle(files)
    # 切片前num_files个文件
    val_files = files[:1000]
    train_files = files[1000:5000]

    folders = [val_images_folder, train_images_folder, val_labels_folder, train_labels_folder]
    for folder in folders:
        # 检查文件夹是否存在
        if not os.path.exists(folder):
            # 如果不存在，创建文件夹
            os.makedirs(folder)
    
    for file in val_files:
        basename_stem = os.path.splitext(file)[0]
        image_path = os.path.join(images_folder, file)
        label_path = os.path.join(labels_folder, basename_stem + '.txt')
        # 移动文件
        shutil.copy(image_path, val_images_folder)
        shutil.copy(label_path, val_labels_folder)

    for file in train_files:
        basename_stem = os.path.splitext(file)[0]
        image_path = os.path.join(images_folder, file)
        label_path = os.path.join(labels_folder, basename_stem + '.txt')
        # 移动文件
        shutil.copy(image_path, train_images_folder)
        shutil.copy(label_path, train_labels_folder)



if __name__ == '__main__':
    images_folder = './image_resources_0'
    labels_folder = './label_resources_whole'
    val_images_folder = './datasets/images/val'
    train_images_folder = './datasets/images/train'
    val_labels_folder = './datasets/labels/val'
    train_labels_folder = './datasets/labels/train'
    copy_random_files(images_folder, labels_folder, val_images_folder, train_images_folder, val_labels_folder, train_labels_folder)