import os
import cv2
import numpy as np

def convert(size, box):
    '''
    convert (xmin, ymin, xmax, ymax) to (cx/w, cy/h, bw/w, bw/h)
    param:
        size: tuple (im_width, im_height)
        box: list [xmin, ymin, xmax, ymax]
    return:
        tuple (cx/w, cy/h, bw/w, bw/h)
    '''
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return [x,y,w,h]

def gen_val_list(imgs_file, target_file):
    tf = open(target_file, 'w')

    imgs_f = open(imgs_file, 'r')
    imgs = imgs_f.readlines()
    for i in imgs:
        path = i.strip().split(' ')[0]
        img = cv2.imread(path)
        h, w, _ = img.shape
        boxes = np.array([float(j) for j in i.strip().split(' ')[1:]]).reshape(-1,4)
        box_list = []
        for b in boxes:
            bb = convert((w, h), b) + [0.0]
            box_list.append(bb)
        box_string = ' '.join([str(j)[:6] for j in np.array(box_list).reshape(-1,)])
        img_label = i.strip().split(' ')[0] + ' ' + box_string
        tf.write(img_label + '\n')

if __name__ == '__main__':
    imgs_file = '../../data/original_img/cv4_and_aug4.txt'
    target_file = '../../data/test_list/test_list.txt'
    gen_val_list(imgs_file, target_file)
