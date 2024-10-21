import os
from heic2png import HEIC2PNG

def file_name(path):
    name_list = os.listdir(path)
    return name_list

# 自用初级版
# 文件夹位置自己填，保证这个文件和要转换的文件在一个文件夹里且除了它们没有任何别的文件和文件夹，这样后面转换时的调用才能不出错。
name = file_name('XXXXXX') # 文件夹位置
name.remove('heic_png.py')

i = 1
length = len(name)
for n in name:
    heic_img = HEIC2PNG(n)
    heic_img.save()  # it'll show as `test.png`2
    print(f'{i}/{length}')
    i += 1