import os
import numpy as np

'''
74094.0
3570.0
233.0 318.0
70.0 51.0
'''

def find_max_box_num(file_path):
    f = open(file_path, 'r')
    lines = f.readlines()
    box_max_area = 0
    box_min_area = 1000000000
    max_box_img = ''
    min_box_img = ''

    count = 0
    for i in lines:
        boxes = np.array([float(j) for j in i.strip().split(' ')[1:]])

        for b in boxes:
            if boxes[2] - boxes[0] > 250 or boxes[3] - boxes[1] > 250:
                count += 1

        areas = (boxes[2] - boxes[0]) * (boxes[3] - boxes[1])
        if box_max_area < areas.max():
            box_max_area = areas.max()
            max_h, max_w = boxes[3] - boxes[1], boxes[2] - boxes[0]
            max_box_img = i.strip().split(' ')[0]
        if box_min_area > areas.min():
            box_min_area = areas.min()
            min_h, min_w = boxes[3] - boxes[1], boxes[2] - boxes[0]
            min_box_img = i.strip().split(' ')[0]

    print(box_max_area)
    print(box_min_area)
    print(max_h, max_w)
    print(min_h, min_w)
    print(max_box_img)
    print(min_box_img)
    print(count)

if __name__ == '__main__':
    file_path = '../data/original_list/img_label.txt'
    find_max_box_num(file_path)
