import os
import re
import cv2
import numpy as np

def gen_img_label_list(csv_list):
    csv_f = open(csv_list, 'r')
    lines = csv_f.readlines()
    lines = lines[1:]
    cnt_img = ''
    cnt_label = ''
    for i in lines:
        img = i.strip().split(',')[0]
        # if img != 'EBA961BC' or img != 'AD393334':
        #     continue
        label = i.strip().split(',')[1]
        if cnt_img == '':
            cnt_img = img
        elif cnt_img == img:
            if cnt_label == '':
                cnt_label = label
            else:
                cnt_label = cnt_label + ' ' + label
        else:
            print(cnt_img)
            print(cnt_label)
            img_and_label = cnt_img + ' ' + cnt_label
            label_res = np.array([float(j) for j in cnt_label.strip().split(' ')]).reshape(-1,4)
            img_ = cv2.imread('../../DataFountain/GLODON_objDet/test_dataset/' + cnt_img)
            h, w, _ = img_.shape
            for b in label_res:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.rectangle(img_, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (0,255,255), 3)
            img_ = cv2.resize(img_, (int(w/2), int(h/2)))
            cv2.imshow('img', img_)
            cv2.waitKey(0)
            cnt_img = img
            cnt_label = label
    label_res = np.array([float(j) for j in cnt_label.strip().split(' ')])
    img = cv2.imread('../../DataFountain/GLODON_objDet/test_dataset/' + cnt_img)
    for b in label:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(img, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (0,255,255), 3)
    img = cv2.resize(img, (int(w/2), int(h/2)))
    cv2.imshow('img', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    csv_list = '../../results/rebar_submit/submit_50000.csv'
    gen_img_label_list(csv_list)
