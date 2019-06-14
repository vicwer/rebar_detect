import os
import numpy as np

def py_nms(dets, thresh, mode="Union"):
    """
    greedily select boxes with high confidence
    keep boxes overlap <= thresh
    rule out overlap > thresh
    :param dets: [[x1, y1, x2, y2 score]]
    :param thresh: retain overlap <= thresh
    :return: indexes to keep
    """
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        if mode == "Union":
            ovr = inter / (areas[i] + areas[order[1:]] - inter)
        elif mode == "Minimum":
            ovr = inter / np.minimum(areas[i], areas[order[1:]])

        inds = np.where(ovr <= thresh)[0]

        order = order[inds + 1]

    return keep

def gen_submit(csv_file, res_file, target_res):
    csv_f = open(csv_file, 'r')
    res_f = open(res_file, 'r')
    tf = open(target_res, 'w')

    res = res_f.readlines()
    csv = csv_f.readlines()

    img_boxes = []
    for i in csv:
        json = {}
        img_name = i.strip().split(',')[:-4]
        json['img'] = img_name
        json['boxes'] = []
        for i in res:
            img = i.strip().split(' ')[0]
            if json['img'] == img:
                scores = float(i.strip().split(' ')[1])
                box = [float(int(float(j))) for j in i.strip().split(' ')[2:]]
                box.append(scores)
                json['boxes'].append(box)
        img_boxes.append(json)

    for i in img_boxes:
        img_name = json['img']
        

def gen_single_submit(res_file, target_res):
    res_f = open(res_file, 'r')
    res = res_f.readlines()

    tf = open(target_res, 'w')
    for i in res:
        img = i.strip().split(' ')[0] + '.jpg'
        scores = float(i.strip().split(' ')[1])
        box = [int(float(j)) for j in i.strip().split(' ')[2:]]
        box = ' '.join([str(j) for j in box])
        if scores >= 0.009:
            tf.write(img + ',' + box + '\n')

if __name__ == '__main__':
    res_file = '../../results/comp4_det_test_rebar.txt'
    target_res = '../../results/rebar_submit/submit_50000.csv'
    gen_single_submit(res_file, target_res)
