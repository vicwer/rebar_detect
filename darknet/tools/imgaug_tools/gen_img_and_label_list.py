import os
import re
import cv2

def gen_img_label_list(csv_list, target_file):
    tf = open(target_file, 'w')

    csv_f = open(csv_list, 'r')
    lines = csv_f.readlines()
    lines = lines[1:]
    cnt_img = ''
    cnt_label = ''
    for i in lines:
        img = i.strip().split(',')[0]
        label = i.strip().split(',')[1]
        if cnt_img == '':
            cnt_img = img
        if cnt_img == img:
            if cnt_label == '':
                cnt_label = label
            else:
                cnt_label = cnt_label + ' ' + label
        else:
            img_and_label = cnt_img + ' ' + cnt_label
            tf.write(img_and_label + '\n')
            cnt_img = img
            cnt_label = label
    tf.write(cnt_img + ' ' + cnt_label + '\n')

if __name__ == '__main__':
    csv_list = '../../DataFountain/GLODON_objDet/train_labels.csv'
    target_file = '../../data/original_list/img_label.txt'
    gen_img_label_list(csv_list, target_file)
