import os,argparse
import xml.etree.ElementTree as ET
from PIL import Image

def xml2txt(args):
    path_xml, path_txt, path_image = args.path_xml, args.path_txt, args.path_image
    for file in os.listdir(path_xml):
        if file.endswith(".xml"):
            basename_stem = os.path.splitext(file)[0]
            xml_file = os.path.join(path_xml, file)
            image_file = os.path.join(path_image, basename_stem + '.jpg')
            txt_file = os.path.join(path_txt, basename_stem + '.txt')

            im = Image.open(image_file)
            im_w, im_h = im.size
            im.close()

            label = ''

            tree = ET.parse(xml_file)
            root = tree.getroot()
            objects = root.findall('.//object')
            for obj in objects:
                bndbox = obj.find('.//bndbox')
                name = obj.find('.//name')

                x0 = float(bndbox.find('xmin').text)
                y0 = float(bndbox.find('ymin').text)
                x1 = float(bndbox.find('xmax').text)
                y1 = float(bndbox.find('ymax').text)

                centerx = (x0 + x1) / 2 / im_w
                centery = (y0 + y1) / 2 / im_h
                width = (x1 - x0) / im_w
                height = (y1 - y0) / im_h

                if name.text == 'apple':
                    name_num = 0
                elif name.text == 'banana':
                    name_num = 1
                elif name.text == 'orange':
                    name_num = 2

                label += f'{name_num} {centerx} {centery} {width} {height}\n'

            file_txt = open(txt_file, 'w')
            file_txt.write(label)
            file_txt.close()



def prase():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_xml', help='.xml dir', required=True)
    parser.add_argument('--path_txt', help='labels .txt dir', required=True)
    parser.add_argument('--path_image', help='images dir', required=True)

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = prase()
    xml2txt(args)