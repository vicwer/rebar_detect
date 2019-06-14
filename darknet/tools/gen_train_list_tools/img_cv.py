import cv2
import os
import numpy as np
from PIL import Image
from tqdm import tqdm

def cv_img(img_path, target_path, target_txt):
    tf = open(target_txt, 'w')

    imgs_f = open(img_path, 'r')
    imgs = imgs_f.readlines()

    img_count = 70000
    for i in tqdm(imgs):
        path = i.strip().split(' ')[0]
        boxes = np.array([float(j) for j in i.strip().split(' ')[1:]]).reshape(-1, 4)

        img = cv2.imread(path)
        h, w, c = img.shape
        if h < w:
            image = np.array(Image.new("RGB", (2675,2000), (255,255,255)))
            image[0:h, 0:w, :] = img
            for col in range(6):
                for row in range(6):
                    box_list = []
                    img = image[row*208:row*208+960, col*343:col*343+960, :].copy()
                    for b in boxes:
                        if b[2] >= col*343 and b[2] <= col*343+960:
                            if b[3] >= row*208 and b[3] <= row*208+960:
                                box_list.append(b)
                            elif b[1] >= row*208 and b[1] <= row*208+960:
                                box_list.append(b)
                        elif b[0] >= col*343 and b[0] <= col*343+960:
                            if b[3] >= row*208 and b[3] <= row*208+960:
                                box_list.append(b)
                            elif b[1] >= row*208 and b[1] <= row*208+960:
                                box_list.append(b)

                    if len(box_list) == 0:
                        continue

                    box_list = np.array(box_list)
                    new_box_list = box_list.copy()
                    new_box_list[:, (0,2)] = new_box_list[:, (0,2)] - col*343
                    new_box_list[:, (1,3)] = new_box_list[:, (1,3)] - row*208
                    new_box_list = np.clip(new_box_list, 0., 960.)

                    box_keep = []
                    for ori_b, new_b in zip(box_list, new_box_list):
                        ori_w, ori_h = ori_b[2] - ori_b[0], ori_b[3] - ori_b[1]
                        new_w, new_h = new_b[2] - new_b[0], new_b[3] - new_b[1]
                        if new_w / ori_w < 0.5 and new_h / ori_h < 0.5:
                            continue
                        if new_w / ori_w < 0.35:
                            continue
                        if new_h / ori_h < 0.35:
                            continue
                        if new_w >= new_h:
                            if new_w / new_h < 3:
                                box_keep.append(new_b)
                        if new_w < new_h:
                            if new_h / new_w < 3:
                                box_keep.append(new_b)
                    box_keep = ' '.join([str(e) for e in np.array(box_keep).reshape(-1,)])
                    img_name = str(img_count).zfill(7) + '.png'
                    cv2.imwrite(os.path.join(target_path, img_name), img)
                    tf.write(img_name + ' ' + box_keep + '\n')
                    img_count += 1

                    # print(box_keep)
                    # for b in box_keep:
                    #     font = cv2.FONT_HERSHEY_SIMPLEX
                    #     cv2.rectangle(img, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (0,255,255), 3)

                    # cv2.imshow('img', img)
                    # cv2.waitKey(0)
        else:
            image = np.array(Image.new("RGB", (2000,2675), (255,255,255)))
            image[0:h, 0:w, :] = img
            for col in range(6):
                for row in range(6):
                    box_list = []
                    img = image[row*343:row*343+960, col*208:col*208+960, :].copy()
                    for b in boxes:
                        if b[2] >= col*208 and b[2] <= col*208+960:
                            if b[3] >= row*343 and b[3] <= row*343+960:
                                box_list.append(b)
                            elif b[1] >= row*343 and b[1] <= row*343+960:
                                box_list.append(b)
                        elif b[0] >= col*208 and b[0] <= col*208+960:
                            if b[3] >= row*343 and b[3] <= row*343+960:
                                box_list.append(b)
                            elif b[1] >= row*343 and b[1] <= row*343+960:
                                box_list.append(b)

                    if len(box_list) == 0:
                        continue

                    box_list = np.array(box_list)
                    new_box_list = box_list.copy()
                    new_box_list[:, (0,2)] = new_box_list[:, (0,2)] - col*208
                    new_box_list[:, (1,3)] = new_box_list[:, (1,3)] - row*343
                    new_box_list = np.clip(new_box_list, 0., 960.)

                    box_keep = []
                    for ori_b, new_b in zip(box_list, new_box_list):
                        ori_w, ori_h = ori_b[2] - ori_b[0], ori_b[3] - ori_b[1]
                        new_w, new_h = new_b[2] - new_b[0], new_b[3] - new_b[1]
                        if new_w / ori_w < 0.5 and new_h / ori_h < 0.5:
                            continue
                        if new_w / ori_w < 0.35:
                            continue
                        if new_h / ori_h < 0.35:
                            continue
                        if new_w >= new_h:
                            if new_w / new_h < 3:
                                box_keep.append(new_b)
                        if new_w < new_h:
                            if new_h / new_w < 3:
                                box_keep.append(new_b)
                        
                    box_keep = ' '.join([str(e) for e in np.array(box_keep).reshape(-1,)])
                    img_name = str(img_count).zfill(7) + '.png'
                    cv2.imwrite(os.path.join(target_path, img_name), img)
                    tf.write(img_name + ' ' + box_keep + '\n')
                    img_count += 1

                    # print(box_keep)
                    # for b in box_keep:
                    #     font = cv2.FONT_HERSHEY_SIMPLEX
                    #     cv2.rectangle(img, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (0,255,255), 3)

                    # cv2.imshow('img', img)
                    # cv2.waitKey(0)

if __name__ == '__main__':
    img_path = '../../data/original_img/cv0123_and_aug0123.txt'
    target_path = '../../DataFountain/GLODON_objDet/cv_img'
    target_txt = '../../data/img_list/img_label_list.txt'
    cv_img(img_path, target_path, target_txt)

    img_path = '../../data/original_img/cv4_and_aug4.txt'
    target_path = '../../DataFountain/GLODON_objDet/c3s/cv_img'
    target_txt = '../../data/img_list/img_label_list_cv4aug4.txt'
    cv_img(img_path, target_path, target_txt)
