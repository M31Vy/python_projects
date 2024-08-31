# 运行指令示例：py verify.py yolo --src_image .\archive\train_zip\train\apple_1.jpg --label_dir .\archive\train_zip\train\

import os,argparse,json
from PIL import Image, ImageDraw

def main_yolo(args):
    src_image, label_dir = args.src_image, args.label_dir
    basename_stem = os.path.splitext(os.path.basename(src_image))[0]
    src_label_file = os.path.join(label_dir, basename_stem + '.txt')

    if os.path.isfile(src_image) and os.path.isfile(src_label_file):
        im = Image.open(src_image)
        im_w, im_h = im.size
        draw = ImageDraw.Draw(im)

        with open(src_label_file, 'r') as fh:
            text = fh.readlines()
            print(text)

        for item in text:

            label = item.strip().split(' ')

            centerx, centery, width, height = list(map(float, label[1:]))
            width_half = width / 2
            height_half = height / 2

            x0, y0, x1, y1 = (centerx - width_half) * im_w, (centery - height_half) * im_h,\
                (centerx + width_half) * im_w, (centery + height_half) * im_h
            draw.rectangle([x0, y0, x1, y1], outline='red', width=3)
            draw.text((x0, y0), text=label[0])

        im.save('temp.jpg')

    else:
        print(f'{src_image} and/or {src_label_file} does not exist')

def main_yolo_batch(args):
    image_dir, label_dir, des_dir, roi_class = args.image_dir, args.label_dir, args.des_dir, args.roi_class
    image_list = [f for f in os.listdir(image_dir) if os.path.splitext(f)[-1] in ['.jpg', '.jpeg', '.png']]

    n = 0
    for f in image_list:
        image_file = os.path.join(image_dir, f)
        label_file = os.path.join(label_dir, f[:-4] + '.txt')

        with open(label_file, 'r') as fh:
            text = fh.readlines()
            category = text[0].split(' ')[0]
            if category != roi_class:
                continue

        n += 1
        if not (n % 10):
            print(n)

        im = Image.open(image_file)
        im_w, im_h = im.size
        draw = ImageDraw.Draw(im)

        for item in text:

            label = item.strip().split(' ')

            centerx, centery, width, height = list(map(float, label[1:]))
            width_half = width / 2
            height_half = height / 2

            x0, y0, x1, y1 = (centerx - width_half) * im_w, (centery - height_half) * im_h,\
                (centerx + width_half) * im_w, (centery + height_half) * im_h
            draw.rectangle([x0, y0, x1, y1], outline='red', width=3)
            draw.text((x0, y0), text=label[0])

        im.save(os.path.join(des_dir, f))

    print(f'total {n} images were generated at {des_dir}')

def main_ocr(args):
    im = Image.open(args.image)
    im_w, im_h = im.size
    draw = ImageDraw.Draw(im)

    ocr = json.load(open(args.ocr))

    for item in ocr:
        bbox = item['bbox']
        draw.rectangle((bbox[0][0], bbox[0][1], bbox[2][0], bbox[2][1]), outline='red', width=3)
    im.save('temp.jpg')
    print('The results are saved in temp.jpg')



def prase():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='sub command help')

    prase_yolo_label = subparsers.add_parser('yolo', help='verify the yolov image and label')
    prase_yolo_label.add_argument('--src_image', help='source image file', required=True)
    prase_yolo_label.add_argument('--label_dir', help='source label dir', required=True)
    prase_yolo_label.set_defaults(func=main_yolo)

    prase_yolo_batch = subparsers.add_parser('yolo_batch', help='generate the images with labels')
    prase_yolo_batch.add_argument('--image_dir', help='source image dir', required=True)
    prase_yolo_batch.add_argument('--label_dir', help='source label dir', required=True)
    prase_yolo_batch.add_argument('--des_dir', help='destination dir', required=True)
    prase_yolo_batch.add_argument('--roi_class', help='roi class', required=True)
    prase_yolo_batch.set_defaults(func=main_yolo_batch)

    prase_ocr = subparsers.add_parser('ocr', help='verify the ocr position on the image')
    prase_ocr.add_argument('--image', help='image file', required=True)
    prase_ocr.add_argument('--ocr', help='ocr file', required=True)
    prase_ocr.set_defaults(func=main_ocr)

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = prase()
    args.func(args)