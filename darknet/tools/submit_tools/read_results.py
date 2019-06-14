import os
import re
import cv2
import numpy as np

def gen_img_label_list(csv_list):
    csv_f = open(csv_list, 'r')
    lines = csv_f.readlines()
    cnt_img = ''
    cnt_label = ''
    for i in lines:
        img = i.strip().split(' ')[0]
        score = float(i.strip().split(' ')[1])
        b = [int(float(j)) for j in i.strip().split(' ')[2:]]

        if score > 0.5:
            continue
        # if img != 'EBA961BC' or img != 'AD393334':
        #     continue

        print(img)
        img_ = cv2.imread('../../DataFountain/GLODON_objDet/test_dataset/' + img + '.jpg')
        print(score)
        h, w, _ = img_.shape
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(img_, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (0,255,255), 3)
        img_ = cv2.resize(img_, (int(w/2), int(h/2)))
        cv2.imshow('img', img_)
        cv2.waitKey(0)

if __name__ == '__main__':
    csv_list = '../../results/comp4_det_test_rebar.txt'
    gen_img_label_list(csv_list)
