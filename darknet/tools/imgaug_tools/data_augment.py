import cv2
import re
import os
import numpy as np
from tqdm import tqdm

def rot90(img_path, target_img_path_rot90, target_txt_rot90):
    imgs_f = open(img_path, 'r')
    tf_rot90 = open(target_txt_rot90, 'w')
    imgs = imgs_f.readlines()
    print(len(imgs))

    path = '../../DataFountain/GLODON_objDet/train_dataset'
    for i in tqdm(imgs):
        img_p = i.strip().split(' ')[0]
        label = i.strip().split(' ')[1:]
        label = np.array([float(j) for j in label]).reshape(-1, 4)

        img_name_rot90 = 'rot90_' + img_p
        img = cv2.imread(os.path.join(path,img_p))
        h, w, _ = img.shape
        rot90 = np.rot90(img)
        rot90 = rot90.copy()

        # print(label)
        label_rot90 = label[:, (1,2,3,0)]
        label_rot90[:, (1,3)] = w - label_rot90[:, (1,3)]
        # print(label_rot90)

        label_rot90 = [str(int(j)) for j in np.reshape(label_rot90, (-1,)).tolist()]

        tf_rot90.write(os.path.join(target_img_path_rot90, img_name_rot90) + ' ' + ' '.join(label_rot90) + '\n')
        cv2.imwrite(os.path.join(target_img_path_rot90, img_name_rot90), rot90)

def flip_horizontal(img_path, target_img_path, target_txt):
    imgs_f = open(img_path, 'r')
    tf = open(target_txt, 'w')
    imgs = imgs_f.readlines()
    print(len(imgs))

    for i in tqdm(imgs):
        img_p = i.strip().split(' ')[0]
        label = i.strip().split(' ')[1:]
        label = np.array([float(j) for j in label]).reshape(-1, 4)

        img_name = 'flip_h_' + re.findall(r'.*\/(.*)', img_p)[0]
        img = cv2.imread(img_p)
        h, w, _ = img.shape
        flip_h_img = cv2.flip(img, 1)

        # print(label)
        label_flip_h = label[:, (2,1,0,3)]
        label_flip_h[:, (0,2)] = w - label_flip_h[:, (0,2)]
        # print(label_rot90)
        # for b in label_flip_h:
        #     font = cv2.FONT_HERSHEY_SIMPLEX
        #     cv2.rectangle(flip_h_img, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (0,255,255), 3)
        # cnt_img = cv2.resize(flip_h_img, (int(w/3), int(h/3)))
        # cv2.imshow('img', cnt_img)
        # cv2.waitKey(0)

        label_flip_h = [str(int(j)) for j in np.reshape(label_flip_h, (-1,)).tolist()]

        tf.write(os.path.join(target_img_path, img_name) + ' ' + ' '.join(label_flip_h) + '\n')
        cv2.imwrite(os.path.join(target_img_path, img_name), flip_h_img)
        # print(label_flip_h)
        # print(label)

def flip_vertical(img_path, target_img_path, target_txt):
    imgs_f = open(img_path, 'r')
    tf = open(target_txt, 'w')
    imgs = imgs_f.readlines()
    print(len(imgs))

    for i in tqdm(imgs):
        img_p = i.strip().split(' ')[0]
        label = i.strip().split(' ')[1:]
        label = np.array([float(j) for j in label]).reshape(-1, 4)

        img_name = 'flip_h_' + re.findall(r'.*\/(.*)', img_p)[0]
        img = cv2.imread(img_p)
        h, w, _ = img.shape
        flip_v_img = cv2.flip(img, 0)

        # print(label)
        label_flip_v = label[:, (0,3,2,1)]
        label_flip_v[:, (1,3)] = h - label_flip_v[:, (1,3)]
        # for b in label_flip_v:
        #     font = cv2.FONT_HERSHEY_SIMPLEX
        #     cv2.rectangle(flip_v_img, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (0,255,255), 3)
        # cnt_img = cv2.resize(flip_v_img, (int(w/3), int(h/3)))
        # cv2.imshow('img', cnt_img)
        # cv2.waitKey(0)

        label_flip_v = [str(int(j)) for j in np.reshape(label_flip_v, (-1,)).tolist()]

        tf.write(os.path.join(target_img_path, img_name) + ' ' + ' '.join(label_flip_v) + '\n')
        cv2.imwrite(os.path.join(target_img_path, img_name), flip_v_img)

if __name__ == '__main__':
    img_path = '../../data/data_augment/rot90_h.txt'
    target_img_path = '../../DataFountain/GLODON_ObjDet/data_augment/rot90_h_v'
    target_txt = '../../data/data_augment/rot90_h_v.txt'
    flip_vertical(img_path, target_img_path, target_txt)
    # flip_horizontal(img_path, target_img_path, target_txt)
