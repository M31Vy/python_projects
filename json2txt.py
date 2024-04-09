import json
import os,argparse



def json2txt(args):
    path_json, path_txt = args.path_json, args.path_txt
    # 读取json文件
    with open(path_json, 'r') as f:
        data = json.load(f)

    # 将annotations列表转换为字典（减小后续操作的时间复杂度）
    annotations = {}
    for ann in data['annotations']:
        del ann['segmentation'], ann['area'], ann['iscrowd'], ann['id']
        if ann['image_id'] in annotations:
            annotations[ann['image_id']].append(ann)
        else:
            annotations[ann['image_id']] = [ann]

    images = data['images']
    del data
    for img in images:
        img_id = img['id']
        img_w = img['width']
        img_h = img['height']
        img_name = os.path.splitext(img['file_name'])[0]
        label = ''

        if img_id in annotations:
            for ann in annotations[img_id]:
                bbox = ann['bbox']
                x0, y0, w, h = bbox

                centerx = (x0 + w / 2) / img_w
                centery = (y0 + h / 2) / img_h
                width = w / img_w
                height = h / img_h

                label += f'{ann["category_id"]-1} {centerx} {centery} {width} {height}\n'

        with open(os.path.join(path_txt, img_name + '.txt'), 'w') as file_txt:
            file_txt.write(label)


    
def prase():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_json', help='json file', required=True)
    parser.add_argument('--path_txt', help='labels .txt dir', required=True)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = prase()
    json2txt(args)